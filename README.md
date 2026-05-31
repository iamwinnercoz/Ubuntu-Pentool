# Penetration Testing Tools Installer

This Python script automates the installation of essential cybersecurity, red teaming, web penetration testing, and API hacking tools on Debian/Ubuntu-based Linux distributions. It is designed to configure a robust environment ready for full, professional cybersecurity engagements.

---

## 🚀 Features

*   **45 Industry-Standard Tools** spanning across 10 specialized security domains.
*   **Smart Multi-Method Installer**: Seamlessly handles standard Ubuntu repositories (`apt`), manual repository clones (`git`), Python modules (`pip`), and provides manual instructions for advanced commercial or proprietary software.
*   **Fully Configured**: Bridges the gap for modern cybersecurity testing by including essential wordlists (`seclists`), pivoting setups, and advanced API assessment utilities.

---

## 🛠️ Complete Tools Catalog (45 Tools)

### 1. Fully Automated Installations (`apt`)

The script will automatically update your package index and install the following **32 packages** via the system package manager:

| Category | Tool | Purpose / Description |
| :--- | :--- | :--- |
| **Reconnaissance** | `nmap` | Industry-standard network mapper & port scanner |
| | `theharvester` | OSINT gathering (emails, subdomains, hosts) |
| | `nikto` | Rapid web server vulnerability scanner |
| | `amass` | Active & passive subdomain enumeration |
| **Vulnerability Scanners** | `openvas` | Comprehensive open-source vulnerability assessment suite |
| | `nessus` | Enterprise-grade vulnerability management engine (requires setup) |
| **Exploitation** | `metasploit-framework` | Rapid exploit development and deployment system |
| | `sqlmap` | Automated SQL injection detection and database takeover |
| | `exploitdb` | Local database lookup tool (`searchsploit`) |
| **Password Cracking** | `john` | Fast and flexible password hash cracker |
| | `hydra` | Very fast network login brute-forcing tool |
| **Wireless Analysis** | `aircrack-ng` | Comprehensive suite for 802.11 WEP and WPA-PSK analysis |
| | `kismet` | Wireless network detector, sniffer, and wardriving tool |
| **Web Applications** | `zaproxy` | OWASP Zed Attack Proxy web app scanner |
| | `wfuzz` | Web application fuzzer and payload injector |
| | `ffuf` | Extremely fast web directory & parameter fuzzer (Go-based) |
| | `feroxbuster` | Recursive and fast directory discovery engine |
| | `wpscan` | Black-box WordPress security assessment scanner |
| **Sniffing & Spoofing** | `wireshark` | The world's foremost network protocol analyzer |
| | `ettercap-graphical` | Suite for interactive man-in-the-middle (MITM) attacks |
| | `responder` | LLMNR, NBT-NS and MDNS active poisoner |
| | `bettercap` | Complete modular MITM and network analysis framework |
| | `masscan` | Extremely fast TCP/UDP port scanner |
| **Active Directory** | `bloodhound` | Active Directory relationship map path visualizer |
| | `crackmapexec` | AD domain evaluation post-exploitation tool |
| | `python3-impacket` | Network protocol manipulation library and script suite |
| **API Hacking** | `mitmproxy` | Interactive HTTPS interception proxy for API traffic |
| **Utility & Pivoting** | `dirb` | Standard content scanner |
| | `gobuster` | Fast directory, DNS, and vhost brute-forcer |
| | `seclists` | Mandatory collection of security list payloads and wordlists |
| | `proxychains4` | Dynamic SOCKS chain connection standard for pivoting |
| | `cherrytree` | Hierarchical note-taking for engagement logging |

---

### 2. Script-Assisted Installations (`git` & `pip3`)

These **5 tools** are cloned directly from GitHub or installed via Python package indices, complete with their libraries:

*   **Recon-ng** (OSINT Reconnaissance framework) — Cloned and installed via `git` + `pip3`.
*   **Empire** (Post-exploitation C2 framework) — Cloned and configured via standard installer script.
*   **Shodan** (Search engine API client) — Installed via `pip3`.
*   **Arjun** (HTTP API parameter fuzzer) — Installed via `pip3`.
*   **jwt_tool** (JSON Web Token hacking toolkit) — Cloned and dependencies installed via `pip3`.

---

### 3. Guided Manual Installations

The script provides direct URLs and instruction logs to complete the download and setup of these **8 essential frameworks**:

1.  **Burp Suite** — Local proxy and web app inspection toolkit (Download from [PortSwigger](https://portswigger.net/burp/releases)).
2.  **Hashcat** — Fast GPU-based password recovery engine (Download from [Hashcat.net](https://hashcat.net/hashcat/)).
3.  **Cobalt Strike** — Premium commercial threat emulation and adversary simulation C2 platform ([Cobalt Strike](https://www.cobaltstrike.com/)).
4.  **Nuclei** — Fast and customizable template-based vulnerability scanner ([ProjectDiscovery](https://github.com/projectdiscovery/nuclei)).
5.  **Sliver C2** — Go-based implant C2 framework for adversary simulation ([BishopFox](https://github.com/bishopfox/sliver)).
6.  **Havoc C2** — Modern and evasion-focused C2 system ([Havoc](https://github.com/HavocFramework/Havoc)).
7.  **Mythic C2** — Collaborative cross-platform agent C2 framework ([Mythic](https://github.com/its-a-feature/Mythic)).
8.  **Kiterunner** — Advanced API endpoint and route brute-forcing tool ([Assetnote](https://github.com/assetnote/kiterunner)).

---

## 📋 Requirements

*   **OS**: Debian-based Linux distribution (Ubuntu, Debian, or Linux Mint).
*   **Python**: Python 3.x installed with `pip3` available.
*   **Permissions**: The script must be run with **`sudo`** privileges.

---

## 🚀 Usage

1.  **Clone this repository**:
    ```bash
    git clone <YOUR_REPOSITORY_URL>
    cd Ubuntu-Pentool
    ```

2.  **Make the installation script executable**:
    ```bash
    chmod +x Setup.py
    ```

3.  **Run the script as root**:
    ```bash
    sudo python3 Setup.py
    ```

4.  **Follow the terminal output logs** to complete any manual configurations for C2 frameworks or local proxy installations.

---

## 🤝 Contributing

Contributions are always welcome! If you would like to include support for extra tools or enhance the setup scripts:
1. Fork this Repository.
2. Create a feature branch: `git checkout -b feature/awesome-new-tool`
3. Commit your changes: `git commit -m "Add support for awesome-new-tool"`
4. Push to your branch: `git push origin feature/awesome-new-tool`
5. Open a Pull Request.

---

## ⚠️ Ethical Disclaimer

This repository and the automated installation script are designed **exclusively for educational, authorized penetration testing, and ethical security analysis purposes**. 

Performing security assessments or active network scanning without explicit, written, and authorized consent from the target environment owner is strictly illegal. The author holds absolutely no responsibility or liability for any actions, damage, or misuse stemming from this toolkit. **Always obtain written permission before conducting security assessments.**

---

## 📄 License

This project is licensed under the **MIT License**. Check the `LICENSE` file for more details.