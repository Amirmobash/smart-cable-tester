# 🔶 RPi Cable Tester

Ein intelligenter Kabeltester basierend auf Raspberry Pi GPIO.

👨‍💻 Entwickelt und überarbeitet von **Amir Mobasheraghdam**

---

## 📌 Beschreibung

Dieses Projekt ist ein **einfacher, aber leistungsfähiger Kabeltester**, der mit einem Raspberry Pi betrieben wird.  
Er prüft die **Verbindungen (Continuity)** zwischen mehreren Pins und zeigt den Status über LEDs und ein Web-Dashboard an.

Das System eignet sich für:
- Netzwerkkabel (LAN / Ethernet)
- Kabelbäume (Harness)
- Allgemeine Leitungsprüfungen

---

## ⚙️ Features

- ✅ Automatische Kabelprüfung
- ✅ GPIO-basierte Pin-Erkennung
- ✅ LED-Statusanzeige
- ✅ Web-Interface (Orange/Weiß Design)
- ✅ Echtzeit-Überwachung
- ✅ Einfach erweiterbar

---

## 🧰 Hardware Anforderungen

- Raspberry Pi (empfohlen: Pi 3 oder Pi 4)
- Jumper Kabel
- LEDs (optional)
- Widerstände (220Ω empfohlen)
- Testkabel / Harness

---

## 🔌 GPIO Belegung

```python
Connector1Pins = [4, 17, 27, 22, 10, 9]   # Output
Connector2Pins = [11, 5, 6, 13, 19, 26]   # Input
Connector3Pins = [18, 23, 24, 25, 8, 7]   # Input
````

---

## 🚀 Installation

```bash
sudo apt update
sudo apt install python3 python3-pip
pip3 install flask
```

Projekt klonen:

```bash
git clone https://github.com/YOUR_USERNAME/amir-rpi-cable-tester.git
cd amir-rpi-cable-tester
```

Starten:

```bash
python3 app.py
```

---

## 🖥️ Web Interface

Öffne im Browser:

```
http://<IP-DEINES-RASPBERRY-PI>:5000
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

## 📊 Funktionsweise

Das System:

1. Setzt Output-Pins HIGH/LOW
2. Liest Input-Pins
3. Prüft korrekte Verbindungen
4. Zeigt Ergebnis:

   * LED (Hardware)
   * Web Dashboard

---

## 🎨 Design

* Theme: **Orange / Weiß**
* Minimalistisch & übersichtlich
* Mobile kompatibel

---

## ⚠️ Hinweise

* Nicht für Hochspannung verwenden!
* Nur für Niederspannungs-Test (GPIO)

---

## 📜 Lizenz

MIT License

---

## 🙌 Credits

Original Idee basierend auf einem Open-Source Projekt
Weiterentwickelt und redesigned von:

👉 **Amir Mobasheraghdam**
