from __future__ import annotations

import json
import logging
import signal
import sys
import time
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import List

from config import load_config
from gpio_backend import GPIO_BACKEND as GPIO, USING_MOCK


@dataclass
class ChannelStatus:
    channel: int
    connector_1_pin: int
    connector_2_pin: int
    connector_3_pin: int
    connector_2_ok: bool
    connector_3_ok: bool
    passed: bool


class CableTester:
    def __init__(self) -> None:
        self.config = load_config()
        self.connector_1 = self.config["connector_1_pins"]
        self.connector_2 = self.config["connector_2_pins"]
        self.connector_3 = self.config["connector_3_pins"]
        self.led_pin = self.config["led_pin"]
        self.poll_interval = float(self.config.get("poll_interval_seconds", 0.25))
        self.status_path = Path(self.config["status_file"])
        self.log_path = Path(self.config["log_file"])
        self.running = True
        self._validate()
        self._setup_logging()
        self._setup_gpio()

    def _validate(self) -> None:
        lengths = {len(self.connector_1), len(self.connector_2), len(self.connector_3)}
        if len(lengths) != 1:
            raise ValueError("All connectors must have the same number of pins.")

    def _setup_logging(self) -> None:
        self.log_path.parent.mkdir(parents=True, exist_ok=True)
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s | %(levelname)s | %(message)s",
            handlers=[
                logging.FileHandler(self.log_path, encoding="utf-8"),
                logging.StreamHandler(sys.stdout),
            ],
        )
        logging.info("Starting %s by %s", self.config["project_name"], self.config["author"])
        logging.info("GPIO backend: %s", "MockGPIO" if USING_MOCK else "RPi.GPIO")

    def _setup_gpio(self) -> None:
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.led_pin, GPIO.OUT)
        GPIO.output(self.led_pin, GPIO.LOW)

        for pin in self.connector_1:
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, GPIO.HIGH)

        for pin in self.connector_2 + self.connector_3:
            GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    def _write_status(self, payload: dict) -> None:
        self.status_path.parent.mkdir(parents=True, exist_ok=True)
        tmp_path = self.status_path.with_suffix(".tmp")
        tmp_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
        tmp_path.replace(self.status_path)

    def _probe_pair(self, index: int) -> ChannelStatus:
        out_pin = self.connector_1[index]
        in2_pin = self.connector_2[index]
        in3_pin = self.connector_3[index]

        for pin in self.connector_1:
            GPIO.output(pin, GPIO.HIGH)
        GPIO.output(out_pin, GPIO.LOW)
        time.sleep(0.01)

        connector_2_ok = GPIO.input(in2_pin) == GPIO.LOW
        connector_3_ok = GPIO.input(in3_pin) == GPIO.LOW
        passed = connector_2_ok and connector_3_ok

        return ChannelStatus(
            channel=index + 1,
            connector_1_pin=out_pin,
            connector_2_pin=in2_pin,
            connector_3_pin=in3_pin,
            connector_2_ok=connector_2_ok,
            connector_3_ok=connector_3_ok,
            passed=passed,
        )

    def scan_once(self) -> dict:
        results: List[ChannelStatus] = [self._probe_pair(i) for i in range(len(self.connector_1))]
        overall_ok = all(item.passed for item in results)
        GPIO.output(self.led_pin, GPIO.HIGH if overall_ok else GPIO.LOW)

        payload = {
            "project_name": self.config["project_name"],
            "author": self.config["author"],
            "using_mock_gpio": USING_MOCK,
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
            "overall_ok": overall_ok,
            "led_pin": self.led_pin,
            "channels": [asdict(item) for item in results],
        }
        self._write_status(payload)
        logging.info("Scan complete | overall_ok=%s | channels=%s", overall_ok, [r.passed for r in results])
        return payload

    def run(self) -> None:
        def handle_signal(signum, frame):
            logging.info("Received signal %s, shutting down...", signum)
            self.running = False

        signal.signal(signal.SIGINT, handle_signal)
        signal.signal(signal.SIGTERM, handle_signal)

        try:
            while self.running:
                self.scan_once()
                time.sleep(self.poll_interval)
        finally:
            GPIO.output(self.led_pin, GPIO.LOW)
            GPIO.cleanup()
            logging.info("GPIO cleaned up")


if __name__ == "__main__":
    CableTester().run()
