import json
from pathlib import Path

basis_ordner = Path(__file__).resolve().parent.parent
config_datei = basis_ordner / "config.json"


def lade_config():
    with config_datei.open("r", encoding="utf-8") as datei:
        daten = json.load(datei)

    daten["base_dir"] = str(basis_ordner)
    daten["status_file"] = str(basis_ordner / daten["status_file"])
    daten["log_file"] = str(basis_ordner / daten["log_file"])

    return daten
