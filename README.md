# 🔶 Smart Cable Tester for Raspberry Pi

A modern, lightweight and reliable cable tester based on Raspberry Pi GPIO.

Developed and optimized by **Amir Mobasheraghdam**

---

## 🚀 Overview

**Smart Cable Tester** is an open-source Raspberry Pi project for checking cable connections quickly and clearly through GPIO pins.

The project is designed for practical cable testing, simple wiring verification and small workshop or laboratory environments. It can be used to detect whether lines are correctly connected, missing, swapped or interrupted.

This project is suitable for:

* 🔌 Ethernet / LAN cable testing
* 🔧 Cable harness testing
* ⚡ General continuity testing
* 🧪 Electronics labs
* 🏭 Workshop and prototyping environments
* 🎓 Learning Raspberry Pi GPIO input and output control

---

## ✨ Features

* Automatic cable connection testing
* GPIO-based signal reading
* Clear pass/fail status output
* Optional LED status display
* Web dashboard with orange/white interface
* Real-time test results
* Simple and expandable project structure
* Easy configuration for different connector layouts
* Suitable for custom cable harnesses
* Lightweight Python and Flask implementation

---

## 🧠 How It Works

The cable tester activates output pins one by one and reads the corresponding input pins.
By comparing the expected connections with the measured connections, the system can detect correct wiring and possible connection errors.

Basic workflow:

1. One GPIO output pin is activated
2. All configured input pins are checked
3. The detected connection is compared with the expected wiring
4. The result is shown in the web dashboard
5. Optional LEDs can display the status directly on the device

Possible test results:

* Correct connection
* Open wire
* Wrong connection
* Swapped wire
* Short circuit indication, depending on configuration

---

## 🧰 Hardware Requirements

* Raspberry Pi 3, Raspberry Pi 4 or compatible Raspberry Pi board
* Jumper wires
* Test cable or cable harness
* Optional LEDs
* Optional 220 Ω resistors
* Breadboard or custom PCB
* Stable 5 V Raspberry Pi power supply

---

## ⚠️ Safety Notice

This project is only intended for **low-voltage signal testing**.

Do not connect the tester to:

* Mains voltage
* High-voltage systems
* Powered industrial lines
* Unknown external circuits
* Automotive or machine wiring while powered

Always test only unpowered cables.
Wrong wiring or external voltage can damage the Raspberry Pi GPIO pins.

---

## 🔌 Example GPIO Configuration

```python
Connector1Pins = [4, 17, 27, 22, 10, 9]
Connector2Pins = [11, 5, 6, 13, 19, 26]
Connector3Pins = [18, 23, 24, 25, 8, 7]
```

The pin configuration can be changed depending on your cable type, connector layout or test adapter.

---

## 📦 Installation

Update the Raspberry Pi:

```bash
sudo apt update
sudo apt upgrade -y
```

Install Python and required packages:

```bash
sudo apt install python3 python3-pip -y
pip3 install flask
```

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/smart-cable-tester.git
cd smart-cable-tester
```

Start the application:

```bash
python3 app.py
```

---

## 🖥️ Web Interface

After starting the application, open the dashboard in a browser:

```text
http://<RASPBERRY-PI-IP>:5000
```

Example:

```text
http://192.168.178.50:5000
```

The dashboard shows the current cable test status and makes the system easy to use from a laptop, tablet or smartphone in the same network.

---

## 📁 Project Structure

```text
smart-cable-tester/
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

## 🔄 Optional Autostart with systemd

Copy the service file:

```bash
sudo cp service/cable_tester.service /etc/systemd/system/
```

Reload systemd:

```bash
sudo systemctl daemon-reload
```

Enable autostart:

```bash
sudo systemctl enable cable_tester
```

Start the service:

```bash
sudo systemctl start cable_tester
```

Check the status:

```bash
sudo systemctl status cable_tester
```

---

## 🎨 Web Dashboard Design

The dashboard is designed with a clean orange and white style.

Design goals:

* Simple layout
* Clear status output
* Mobile-friendly interface
* Fast readability in workshop environments
* Minimal and modern appearance

---

## 🔧 Configuration Ideas

The project can be adapted for many different connector types.

Possible extensions:

* RJ45 Ethernet cable adapter
* Custom cable harness adapter
* DB9 / DB25 connector tester
* Automotive connector testing
* Industrial control cabinet wiring test
* LED matrix for hardware status display
* Export of test results as CSV
* Test history logging
* QR code or barcode scan for cable IDs

---

## 🧪 Example Use Cases

### LAN Cable Testing

Check whether all conductors of an Ethernet cable are connected correctly.

### Cable Harness Testing

Verify custom wiring harnesses before installation.

### Workshop Testing Station

Use the Raspberry Pi as a small cable test station with web interface.

### Education

Learn how GPIO input and output pins can be used for signal testing and automation.

---

## 🛠️ Technologies Used

* Raspberry Pi
* Python
* Flask
* GPIO control
* HTML
* CSS
* JavaScript
* Optional LED indicators

---

## 📜 License

MIT License

---

## 🙌 Credits

Based on practical ideas from the open-source and maker community.
Further developed, structured and modernized by:

**Amir Mobasheraghdam**

---

## 🔍 Keywords

Raspberry Pi cable tester, GPIO cable tester, smart cable tester, LAN cable tester, Ethernet cable tester, cable harness tester, Python cable tester, Flask dashboard, Raspberry Pi GPIO project, wire continuity tester, open source cable tester, workshop cable tester, electronics lab tool, smart wiring test, cable test web dashboard, low voltage cable tester
