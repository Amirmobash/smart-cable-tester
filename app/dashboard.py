import json
from pathlib import Path

from flask import Flask, jsonify, render_template

from config import lade_config

einstellungen = lade_config()

app = Flask(
    __name__,
    template_folder=str(Path(__file__).parent / "templates"),
    static_folder=str(Path(__file__).parent / "static"),
)


@app.route("/")
def startseite():
    return render_template("index.html", config=einstellungen)


@app.route("/api/status")
def status_abrufen():
    status_datei = Path(einstellungen["status_file"])

    if not status_datei.exists():
        return jsonify(
            {
                "project_name": einstellungen["project_name"],
                "author": einstellungen["author"],
                "overall_ok": False,
                "message": "Noch keine Statusdatei gefunden. Bitte zuerst app/main.py starten.",
                "channels": [],
            }
        )

    with status_datei.open("r", encoding="utf-8") as datei:
        daten = json.load(datei)

    return jsonify(daten)


if __name__ == "__main__":
    app.run(
        host=einstellungen["dashboard_host"],
        port=int(einstellungen["dashboard_port"]),
        debug=False,
    )
