# Python Port Scanner

A simple TCP SYN Port Scanner and DNS Scanner built with Python and Scapy.

## Description

This project is a lightweight network scanner written in Python using the Scapy library.

The scanner can:

* Detect open TCP ports using the SYN Scan technique
* Detect DNS services running on port 53 using UDP DNS requests

The program takes a target IP address as input and analyzes the responses returned by the target machine.

---

# How the SYN Scan Works

TCP connections normally follow the famous 3-way handshake:

1. SYN
2. SYN-ACK
3. ACK

This scanner performs a SYN Scan by sending only a SYN packet to the target port.

## Response Analysis

* If the target responds with **SYN-ACK**, the port is considered **OPEN**
* If the target responds with **RST**, the port is considered **CLOSED**

After receiving a SYN-ACK response, the scanner sends a RST packet to avoid completing the full TCP connection.

This technique is commonly known as a **Half-Open Scan**.

---

# How the DNS Scan Works

The DNS scan uses UDP packets on port 53.

Instead of sending an empty UDP packet, the scanner sends a real DNS query containing:

* Query Name: `google.com`
* `rd = 1` (Recursion Desired)

This tells the DNS server:

> "If you do not already know the answer, recursively search for it and return the IP address."

If the target responds to the DNS query, the scanner concludes that a DNS service is running on port 53.

---

# Technologies Used

* Python 3
* Scapy

---

# Installation

Clone the repository:

```bash
git clone https://github.com/landrytchakui-dot/Port_Scanner.git
cd Port_Scanner
```

Install Scapy:

```bash
pip install scapy
```

---

# Usage

Run the program with root privileges:

```bash
sudo python3 Port_Scanner.py
```

# Features

* TCP SYN Port Scanning
* UDP DNS Detection
* Open Port Identification
* DNS Query Testing
* Lightweight and Fast

---

# Educational Purpose

This project was created for educational purposes to better understand:

* TCP/IP networking
* TCP Handshake
* SYN Scanning
* DNS Protocol
* Packet crafting with Scapy
* Basic network reconnaissance

---

# Warning

Use this tool only on systems you own or have permission to test.

Unauthorized scanning may violate laws or network policies.

---

# Author

Kyro  
Cybersecurity Enthusiast
 
