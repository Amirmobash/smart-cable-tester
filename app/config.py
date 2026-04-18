from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict

BASE_DIR = Path(__file__).resolve().parent.parent
CONFIG_PATH = BASE_DIR / "config.json"


def load_config() -> Dict[str, Any]:
    with CONFIG_PATH.open("r", encoding="utf-8") as f:
        config = json.load(f)

    config["base_dir"] = str(BASE_DIR)
    config["status_file"] = str(BASE_DIR / config["status_file"])
    config["log_file"] = str(BASE_DIR / config["log_file"])
    return config
