# 🔶 smart-cable-tester

Ein moderner und zuverlässiger Kabeltester auf Basis von Raspberry Pi GPIO.

👨‍💻 Entwickelt und optimiert von **Amir Mobasheraghdam**

---

## 🚀 Übersicht

Der **amir-rpi-cable-tester** ist ein leichtgewichtiges Open-Source-Projekt zur Prüfung von Kabelverbindungen.
Er ermöglicht eine schnelle und präzise Analyse von Leitungen direkt über die GPIO-Pins eines Raspberry Pi.

Das System eignet sich besonders für:

* 🔌 Netzwerkkabel (LAN / Ethernet)
* 🔧 Kabelbäume (Harness Testing)
* ⚡ Allgemeine Leitungsprüfungen

---

## ⚙️ Funktionen

* ✅ Automatische Kabelprüfung
* ✅ GPIO-basierte Signalverarbeitung
* ✅ LED-Statusanzeige (optional)
* ✅ Web-Dashboard (Orange/Weiß Design)
* ✅ Echtzeit-Statusanzeige
* ✅ Einfach erweiterbar

---

## 🧰 Hardware Anforderungen

* Raspberry Pi (empfohlen: Pi 3 / Pi 4)
* Jumper Kabel
* LEDs (optional)
* Widerstände (ca. 220Ω)
* Testkabel oder Kabelbaum

---

## 🔌 GPIO Konfiguration

```python
Connector1Pins = [4, 17, 27, 22, 10, 9]
Connector2Pins = [11, 5, 6, 13, 19, 26]
Connector3Pins = [18, 23, 24, 25, 8, 7]
```

---

## 📦 Installation

```bash
sudo apt update
sudo apt install python3 python3-pip
pip3 install flask
```

Repository klonen:

```bash
git clone https://github.com/YOUR_USERNAME/amir-rpi-cable-tester.git
cd amir-rpi-cable-tester
```

Anwendung starten:

```bash
python3 app.py
```

---

## 🖥️ Web Interface

Im Browser öffnen:

```
http://<RASPBERRY-PI-IP>:5000
```

---

## 📁 Projektstruktur

```
├── app.py
├── tester.py
├── config.json
├── templates/
│   └── index.html
├── static/
│   └── style.css
├── starter.sh
├── service/
│   └── cable_tester.service
└── README.md
```

---

## 🔄 Autostart (optional)

```bash
sudo cp service/cable_tester.service /etc/systemd/system/
sudo systemctl enable cable_tester
sudo systemctl start cable_tester
```

---

## 🧠 Funktionsweise

1. Output-Pins werden nacheinander aktiviert
2. Input-Pins werden ausgelesen
3. Verbindungen werden überprüft
4. Ergebnis wird angezeigt:

* LED (Hardware)
* Web-Dashboard

---

## 🎨 Design

* Orange / Weiß Theme
* Klar und minimalistisch
* Auch für mobile Geräte geeignet

---

## ⚠️ Hinweise

❗ Nur für Niederspannung geeignet
❗ Nicht für Hochspannung verwenden

---

## 📜 Lizenz

MIT License

---

## 🙌 Credits

Basierend auf Ideen aus der Open-Source-Community
Weiterentwickelt und modernisiert von:

👉 **Amir Mobasheraghdam**
