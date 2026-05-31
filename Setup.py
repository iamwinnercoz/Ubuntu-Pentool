import subprocess
import sys
import os

# List of tools to install (available in default repositories)
tools = [
    # Reconnaissance Tools
    "nmap",                # Nmap
    "theharvester",         # theHarvester
    "nikto",               # Nikto
    "amass",               # Subdomain Enumeration

    # Vulnerability Scanners
    "openvas",             # OpenVAS
    "nessus",              # Nessus (requires manual setup)

    # Exploitation Tools
    "metasploit-framework", # Metasploit Framework
    "sqlmap",              # SQLmap
    "exploitdb",           # Local Exploit Database (searchsploit)

    # Password Cracking Tools
    "john",                # John the Ripper
    "hydra",               # Hydra

    # Wireless Network Tools
    "aircrack-ng",         # Aircrack-ng
    "kismet",              # Kismet

    # Web Application Tools
    "zaproxy",             # OWASP ZAP
    "wfuzz",               # Wfuzz
    "ffuf",                # Ffuf (Fuzzing)
    "feroxbuster",         # Feroxbuster
    "wpscan",              # WordPress Scanner

    # Network Sniffing and Spoofing
    "wireshark",           # Wireshark
    "ettercap-graphical",  # Ettercap
    "responder",           # Responder (LLMNR/NBT-NS Poisoning)
    "bettercap",           # Bettercap (MITM)
    "masscan",             # Masscan (Fast Port Scanner)

    # Active Directory & Red Teaming
    "bloodhound",          # BloodHound
    "crackmapexec",        # CrackMapExec (AD Enum)
    "python3-impacket",    # Impacket tools

    # API Hacking
    "mitmproxy",           # Mitmproxy (API Interception)

    # Bonus Tools
    "dirb",                # Dirb
    "gobuster",            # Gobuster
    "seclists",            # Mandatory Wordlists
    "proxychains4",        # Network Pivoting
    "cherrytree",          # Note taking & Reporting
]

def install_tools():
    print("Starting installation of tools...\n")
    
    # Update package list
    print("Updating package list...")
    subprocess.run(["sudo", "apt", "update"], check=True)
    
    # Install each tool
    for tool in tools:
        print(f"Installing {tool}...")
        try:
            subprocess.run(["sudo", "apt", "install", "-y", tool], check=True)
            print(f"{tool} installed successfully!\n")
        except subprocess.CalledProcessError as e:
            print(f"Failed to install {tool}. Error: {e}\n")
    
    print("Tools available in the default repositories have been installed.")
    print("\nAdditional steps for tools not in the default repositories:")

    # Install Recon-ng (via git and pip)
    print("\n1. Installing Recon-ng...")
    try:
        subprocess.run(["sudo", "apt", "install", "-y", "git", "python3-pip"], check=True)
        subprocess.run(["git", "clone", "https://github.com/lanmaster53/recon-ng.git"], check=True)
        os.chdir("recon-ng")
        subprocess.run(["pip3", "install", "-r", "requirements.txt"], check=True)
        print("Recon-ng installed successfully!\n")
    except subprocess.CalledProcessError as e:
        print(f"Failed to install Recon-ng. Error: {e}\n")

    # Install Nessus (manual download)
    print("\n2. Nessus is not in the default repositories.")
    print("   Download it from https://www.tenable.com/downloads/nessus and install manually.")

    # Install Burp Suite (manual download)
    print("\n3. Burp Suite is not in the default repositories.")
    print("   Download it from https://portswigger.net/burp/releases and install manually.")

    # Install Hashcat (manual download for latest version)
    print("\n4. Hashcat is not in the default repositories.")
    print("   Download it from https://hashcat.net/hashcat/ and install manually.")

    # Install Cobalt Strike (manual download)
    print("\n5. Cobalt Strike is a commercial tool.")
    print("   Purchase and download it from https://www.cobaltstrike.com/.")

    # Install Empire (via git)
    print("\n6. Installing Empire...")
    try:
        subprocess.run(["git", "clone", "https://github.com/BC-SECURITY/Empire.git"], check=True)
        os.chdir("Empire")
        subprocess.run(["sudo", "./setup/install.sh"], check=True)
        print("Empire installed successfully!\n")
    except subprocess.CalledProcessError as e:
        print(f"Failed to install Empire. Error: {e}\n")

    # Install Shodan (via pip)
    print("\n7. Installing Shodan...")
    try:
        subprocess.run(["pip3", "install", "shodan"], check=True)
        print("Shodan installed successfully!\n")
    except subprocess.CalledProcessError as e:
        print(f"Failed to install Shodan. Error: {e}\n")

    # Install Arjun (via pip)
    print("\n8. Installing Arjun (API Parameter Fuzzer)...")
    try:
        subprocess.run(["pip3", "install", "arjun"], check=True)
        print("Arjun installed successfully!\n")
    except subprocess.CalledProcessError as e:
        print(f"Failed to install Arjun. Error: {e}\n")

    # Install jwt_tool (via git)
    print("\n9. Installing jwt_tool...")
    try:
        subprocess.run(["git", "clone", "https://github.com/ticarpi/jwt_tool.git"], check=True)
        subprocess.run(["pip3", "install", "-r", "jwt_tool/requirements.txt"], check=True)
        print("jwt_tool installed successfully!\n")
    except subprocess.CalledProcessError as e:
        print(f"Failed to install jwt_tool. Error: {e}\n")

    # Additional manual tools instructions
    print("\n10. Nuclei is a powerful vulnerability scanner.")
    print("    Download it from https://github.com/projectdiscovery/nuclei or install via Go.")

    print("\n11. Advanced C2 Frameworks (Sliver, Havoc, Mythic) require manual setup.")
    print("    Check their respective GitHub repositories for installation instructions.")

    print("\n12. Kiterunner (API Discovery tool) requires manual download.")
    print("    Download releases from https://github.com/assetnote/kiterunner")

    print("\nAll tools installed or instructions provided!")

if __name__ == "__main__":
    # Check if the script is running with sudo privileges
    if not 'SUDO_UID' in os.environ.keys():
        print("Please run this script with sudo.")
        sys.exit(1)
    
    install_tools()