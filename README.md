# 🕵️‍♂️ PhantomSweep

An automated reconnaissance framework for bug bounty hunters, CTF players, and penetration testers. Built in Python, this tool performs subdomain enumeration, port scanning, WHOIS lookup, directory brute-forcing, and more.

---

## 🔧 Features

- WHOIS & DNS Lookup
- Subdomain Enumeration (`assetfinder`)
- Advanced Port Scanning (`nmap`)
- Directory Brute Force (`gobuster`)
- Modular design for easy extension

---

## 📁 Folder Structure

PhantomSweep/
├── main.py
├── modules/
│ ├── whois_dns.py
│ ├── subdomains.py
│ ├── portscan.py
│ ├── dir_enum.py
│ └── vulnscan.py
├── output/
└── config/ (optional)

## 🛠️ Requirements

- Python 3
- Tools: `nmap`, `gobuster`, `whois`, `dig`, `assetfinder`

Install tools on Kali:    

```bash
sudo apt install nmap gobuster whois dnsutils -y
go install github.com/tomnomnom/assetfinder@latest
https://github.com/Noob-Dev-jith/PhantomSweep.git
cd PhantomSweep
python3 main.py


