# 🌐 Network Packet Sniffer & Traffic Analyzer

<p align="center">

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python)
![Scapy](https://img.shields.io/badge/Scapy-Packet%20Analysis-orange?style=for-the-badge)
![Flask](https://img.shields.io/badge/Flask-Web%20Dashboard-black?style=for-the-badge&logo=flask)
![Cybersecurity](https://img.shields.io/badge/Cybersecurity-Network%20Monitoring-red?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

</p>

> A real-time **Network Packet Sniffer and Traffic Monitoring Tool** built using **Python**, **Scapy**, and **Flask** that captures live network traffic, extracts packet metadata, logs captured packets, and provides a web interface for monitoring network activity.

Designed as a cybersecurity learning project, this application demonstrates fundamental concepts of **network traffic analysis**, **packet inspection**, and **real-time monitoring**.

---

# 🌟 Features

- 📡 Real-Time Packet Capture
- 🌐 Live Network Traffic Monitoring
- 📍 Source & Destination IP Extraction
- 🔢 TCP, UDP & ICMP Protocol Identification
- 🔌 Source & Destination Port Detection
- 📄 Packet Summary Generation
- 📊 Live Packet Dashboard
- 💾 Automatic CSV Logging
- 🔄 Real-Time Packet Updates
- 🧵 Background Packet Sniffing using Multithreading

---

# 💡 Why This Project?

Network monitoring is an essential component of cybersecurity, helping analysts detect suspicious traffic, troubleshoot connectivity issues, and investigate potential attacks.

This project demonstrates how packet sniffing tools can collect and analyze live network traffic to improve network visibility and security awareness.

---

# 🔍 Packet Information Captured

For every captured packet, the application extracts:

- Timestamp
- Source IP Address
- Destination IP Address
- Network Protocol
- Source Port
- Destination Port
- Packet Summary

All captured packets are stored in memory and simultaneously exported to a CSV log file for later analysis.

---

# 🏗️ System Architecture

```text
               Network Interface
                      │
                      ▼
              Scapy Packet Sniffer
                      │
                      ▼
            Packet Processing Engine
                      │
        ┌─────────────┼─────────────┐
        ▼             ▼             ▼
 Packet Parsing   CSV Logging   Memory Storage
        │             │             │
        └─────────────┼─────────────┘
                      ▼
              Flask Web Server
                      │
                      ▼
          Live Monitoring Dashboard
```

---

# 🔄 Application Workflow

```text
Start Application
        │
        ▼
Initialize Packet Sniffer
        │
        ▼
Capture Network Packets
        │
        ▼
Extract Packet Metadata
        │
        ▼
Store Packet Information
        │
        ├────────► Save to CSV
        │
        ▼
Display on Flask Dashboard
```

---

# 📂 Project Structure

```text
Python-Based-security-tools-packet-sniffer/

├── packet_sniffer.py
├── network_traffic_log.csv
└── templates/
    └── index.html
```

---

# ⚙️ Technology Stack

## Programming Language

- Python

## Networking

- Scapy
- Socket Programming

## Backend

- Flask
- Threading

## Data Handling

- Pandas
- CSV

---

# 🧠 Networking Concepts Demonstrated

- Packet Sniffing
- Network Monitoring
- TCP/IP
- UDP
- ICMP
- Source & Destination Ports
- Packet Inspection
- Network Protocol Analysis
- Real-Time Monitoring
- Multithreading
- HTTP APIs
- Logging

---

# 📊 Captured Packet Details

Each packet includes:

| Field | Description |
|--------|-------------|
| Timestamp | Packet capture time |
| Source IP | Sender address |
| Destination IP | Receiver address |
| Protocol | TCP / UDP / ICMP |
| Source Port | Sender port |
| Destination Port | Receiver port |
| Packet Summary | Scapy packet summary |

---

# 🌐 Web Dashboard

The Flask dashboard provides:

- Live Packet Feed
- Recent Packet History
- Protocol Filtering
- JSON API
- Real-Time Updates

Supported Filters:

- All
- TCP
- UDP
- ICMP

---

# 🚀 Installation

## Clone Repository

```bash
git clone https://github.com/palak00027/Python-Based-security-tools.git

cd Python-Based-security-tools
```

---

## Install Dependencies

```bash
pip install flask pandas scapy
```

---

## Run the Application

```bash
python packet_sniffer.py
```

Open:

```
http://127.0.0.1:5000
```

---

# 📡 API

## Get Recent Packets

```http
GET /packets
```

### Filter by Protocol

```http
GET /packets?filter=tcp
```

```http
GET /packets?filter=udp
```

```http
GET /packets?filter=icmp
```

Returns the latest captured packets in JSON format.

---

# 📸 Screenshots

<img width="1080" height="1170" alt="image" src="https://github.com/user-attachments/assets/9771a3f5-18f3-4e38-a0d4-511e6468e289" />


---

# 📈 Current Capabilities

| Feature | Status |
|----------|--------|
| Live Packet Capture | ✅ |
| TCP Monitoring | ✅ |
| UDP Monitoring | ✅ |
| ICMP Monitoring | ✅ |
| CSV Logging | ✅ |
| Flask Dashboard | ✅ |
| JSON API | ✅ |
| Protocol Filtering | ✅ |

---

# 🚀 Future Enhancements

- Deep Packet Inspection (DPI)
- HTTP Header Analysis
- DNS Packet Analysis
- ARP Monitoring
- Packet Search
- GeoIP Lookup
- Network Traffic Statistics
- Threat Detection Rules
- Suspicious Traffic Alerts
- PCAP File Export
- Authentication Dashboard
- Docker Deployment

---

# ⚠️ Disclaimer

This project is intended **strictly for educational purposes and authorized network monitoring**.

Use only on networks you own or have explicit permission to analyze. Unauthorized packet capture may violate privacy laws and organizational security policies.

---

# 📚 Learning Outcomes

This project demonstrates practical knowledge of:

- Network Security
- Packet Analysis
- Scapy
- Flask Development
- Multithreading
- Network Protocols
- Traffic Monitoring
- CSV Logging
- REST APIs
- Cybersecurity Fundamentals

---

# 👩‍💻 Author

**Palak Upadhyay**

🎓 B.E. Computer Science & Engineering (Cyber Security)

💡 Passionate about Cybersecurity, Network Security, Cloud Computing, Secure Software Development, and Artificial Intelligence.

**GitHub:**  
https://github.com/palak00027

---

# ⭐ Show Your Support

If you found this project useful, consider giving it a **⭐ Star** on GitHub. Your support encourages future improvements and helps others discover the project.
