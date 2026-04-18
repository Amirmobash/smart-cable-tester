from __future__ import annotations

import logging
from typing import Dict

LOGGER = logging.getLogger(__name__)


class MockGPIO:
    BCM = "BCM"
    OUT = "OUT"
    IN = "IN"
    LOW = 0
    HIGH = 1
    PUD_UP = "PUD_UP"

    def __init__(self) -> None:
        self.pin_modes: Dict[int, str] = {}
        self.pin_values: Dict[int, int] = {}
        self.input_defaults: Dict[int, int] = {}

    def setmode(self, mode: str) -> None:
        LOGGER.info("MockGPIO set mode: %s", mode)

    def setup(self, pin: int, mode: str, pull_up_down: str | None = None) -> None:
        self.pin_modes[pin] = mode
        if mode == self.OUT:
            self.pin_values[pin] = self.LOW
        else:
            self.input_defaults[pin] = self.HIGH if pull_up_down == self.PUD_UP else self.LOW
            self.pin_values.setdefault(pin, self.input_defaults[pin])

    def output(self, pin: int, value: int) -> None:
        self.pin_values[pin] = value

    def input(self, pin: int) -> int:
        return self.pin_values.get(pin, self.input_defaults.get(pin, self.HIGH))

    def cleanup(self) -> None:
        LOGGER.info("MockGPIO cleanup called")


try:
    import RPi.GPIO as GPIO  # type: ignore
    GPIO_BACKEND = GPIO
    USING_MOCK = False
except Exception:
    GPIO_BACKEND = MockGPIO()
    USING_MOCK = True
