from __future__ import annotations

import json
from pathlib import Path

from flask import Flask, jsonify, render_template

from config import load_config

config = load_config()
app = Flask(
    __name__,
    template_folder=str(Path(__file__).parent / "templates"),
    static_folder=str(Path(__file__).parent / "static"),
)


@app.route("/")
def index():
    return render_template("index.html", config=config)


@app.route("/api/status")
def api_status():
    status_path = Path(config["status_file"])
    if not status_path.exists():
        return jsonify(
            {
                "project_name": config["project_name"],
                "author": config["author"],
                "overall_ok": False,
                "message": "Status file not created yet. Start app/main.py first.",
                "channels": [],
            }
        )
    return jsonify(json.loads(status_path.read_text(encoding="utf-8")))


if __name__ == "__main__":
    app.run(host=config["dashboard_host"], port=int(config["dashboard_port"]), debug=False)
