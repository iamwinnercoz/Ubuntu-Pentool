# Penetration Testing Tools Installer

This Python script automates the installation of essential penetration testing tools on Debian-based Linux distributions (e.g., Ubuntu). It installs tools for reconnaissance, vulnerability scanning, exploitation, password cracking, wireless network analysis, and more.

---

## Features

- Installs over 20 popular penetration testing tools.
- Handles tools available in default repositories and provides instructions for manual installation of others.
- Easy to use and customizable.

---

## Tools Included

### Reconnaissance Tools

- **Nmap** - Network mapper for discovering hosts and services.
- **Recon-ng** - Web reconnaissance framework.
- **theHarvester** - Gathers emails, subdomains, and other information from public sources.

### Vulnerability Scanners

- **Nessus** - Comprehensive vulnerability scanner.
- **OpenVAS** - Open-source vulnerability assessment tool.
- **Nikto** - Web server vulnerability scanner.

### Exploitation Tools

- **Metasploit Framework** - Tool for developing and executing exploits.
- **SQLmap** - Automates SQL injection detection and exploitation.
- **Burp Suite** - Web application security testing tool.

### Password Cracking Tools

- **John the Ripper** - Fast password cracker.
- **Hashcat** - Advanced password recovery tool (GPU-based).
- **Hydra** - Network login cracker.

### Wireless Network Tools

- **Aircrack-ng** - Suite for assessing Wi-Fi network security.
- **Kismet** - Wireless network detector and sniffer.

### Post-Exploitation Tools

- **Cobalt Strike** - Advanced threat emulation tool.
- **Empire** - Post-exploitation framework for PowerShell and Python.

### Web Application Tools

- **OWASP ZAP** - Open-source web application security scanner.
- **Wfuzz** - Web application fuzzing tool.

### Network Sniffing and Spoofing

- **Wireshark** - Network protocol analyzer.
- **Ettercap** - Suite for man-in-the-middle (MITM) attacks.

### Bonus Tools

- **Dirb/Dirbuster** - Directory brute-forcing tools.
- **Gobuster** - Fast directory/file and DNS brute-forcing tool.
- **Shodan** - Search engine for discovering exposed devices and services.

---

## Requirements

- **Operating System**: Debian-based Linux (e.g., Ubuntu).
- **Python**: Python 3.x installed.
- **Permissions**: Run the script with `sudo` privileges.

---

## Usage

1. Clone the repository:
   **git clone**

2. Make the script executable:
   **chmod +x install_tools.py**

3. Run the script:
   **sudo python3 install_tools.py**

4. Follow the on-screen instructions for tools that require manual installation.

## Manual Installation Instructions

Some tools are not available in the default repositories and require manual installation. The script will guide you through the process for the following tools:

- **Nessus:** Download from Tenable.

- **Burp Suite:** Download from PortSwigger.

- **Hashcat:** Download from Hashcat.

- **Cobalt Strike:** Purchase and download from Cobalt Strike.

- **Empire:** Installed automatically via Git.

- **Shodan:** Installed automatically via pip.

## Contributing

Contributions are welcome! If you’d like to add more tools or improve the script, follow these steps:

1. Fork the repository.

2. Create a new branch:
   **git checkout -b feature/new-tool**

3. Make your changes and commit them:
   **git commit -m "Added support for new-tool"**

4. Push to the branch:
   **git push origin feature/new-tool**

5. Open a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Disclaimer

This script is intended for educational and ethical purposes only. Do not use it for illegal or malicious activities. The author is not responsible for any misuse of this tool.

## Support

If you encounter any issues or have questions, feel free to open an issue on GitHub or reach out to me directly.

## Enjoy Hacking Responsibly! 😎🔥
