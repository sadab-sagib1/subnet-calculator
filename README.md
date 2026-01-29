# Subnet Calculator (IPv4)

This is a simple Python program that calculates basic subnet information from an IPv4 address.

It is made for beginner networking students and uses easy-to-read code and comments.

---

## What this program does

When you enter an IP address with CIDR notation, the program shows:

- Network address  
- Broadcast address  
- Subnet mask  
- CIDR prefix  
- Total number of IP addresses  
- Number of usable hosts  
- Usable host range  

Example input:
192.168.1.10/24


---

## Why this project exists

Subnetting is a core topic in computer networking.

This project helps practice:
- IPv4 addressing
- CIDR notation
- Understanding usable vs non-usable IP addresses
- Basic Python programming

---

## Requirements

- Python 3.8 or newer
- No external libraries needed (standard Python only)

---

## How to run the program

1. Open a terminal inside the project folder  
2. Run the program:

```bash
python subnet_calc.py

3. Enter an IP address with CIDR when prompted

Example:
IP/CIDR: 192.168.1.10/24

Example output:

IPv4 Subnet Calculator
----------------------
Input IP/CIDR:       192.168.1.10/24
Network Address:     192.168.1.0
Broadcast Address:   192.168.1.255
Subnet Mask:         255.255.255.0
CIDR Prefix:         /24
Total Addresses:     256
Usable Hosts:        254
Usable Host Range:   192.168.1.1 - 192.168.1.254

Author
Sagib Ul Sadab