import json
from pathlib import Path

projekt_ordner = Path(__file__).resolve().parent.parent
pfad_zur_config = projekt_ordner / "config.json"


def lade_config():
    with pfad_zur_config.open("r", encoding="utf-8") as datei:
        einstellungen = json.load(datei)

    einstellungen["base_dir"] = str(projekt_ordner)
    einstellungen["status_file"] = str(projekt_ordner / einstellungen["status_file"])
    einstellungen["log_file"] = str(projekt_ordner / einstellungen["log_file"])

    return einstellungen
