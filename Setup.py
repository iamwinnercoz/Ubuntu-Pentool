#!/usr/bin/env python3
import subprocess
import sys
import os
import shutil

OPT_DIR = "/opt"

# Tools available via apt
apt_tools = [
    "nmap",
    "nikto",
    "openvas",
    "sqlmap",
    "john",
    "hydra",
    "hashcat",
    "aircrack-ng",
    "wfuzz",
    "wireshark",
    "ettercap-graphical",
    "dirb",
    "gobuster",
]

# Python-module packages for system-wide install
python3_pkgs = [
    "python3-pip",          # pip itself
    "python3-dnspython",    # theHarvester
    "python3-bs4",          # BeautifulSoup4
    "python3-requests",     # Recon-ng, modules
    "python3-validators",   # Recon-ng
    "python3-netaddr",      # Recon-ng
    "python3-jinja2",       # Recon-ng
    "python3-chardet",      # Recon-ng
    "python3-shodan",       # Shodan
]


def run_cmd(cmd, cwd=None):
    try:
        subprocess.run(cmd, check=True, cwd=cwd)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error running {' '.join(cmd)}:\n  {e}\n")
        return False


def ensure_curl():
    if shutil.which("curl") is None:
        print("curl not found. Installing curl…")
        run_cmd(["sudo", "apt", "update"])
        run_cmd(["sudo", "apt", "install", "-y", "curl"])


def install_system_packages():
    print("Updating apt and installing core tools…")
    run_cmd(["sudo", "apt", "update"])
    # core tools
    for pkg in apt_tools:
        print(f"Installing {pkg}…")
        run_cmd(["sudo", "apt", "install", "-y", pkg])
    # python modules
    print("Installing Python modules via apt…")
    run_cmd(["sudo", "apt", "install", "-y"] + python3_pkgs)


def clone_repo(name, repo_url):
    dest = os.path.join(OPT_DIR, name)
    if not os.path.isdir(dest):
        print(f"Cloning {name} into {dest}…")
        run_cmd(["sudo", "git", "clone", repo_url, dest])
    return dest


def install_theharvester():
    print("\n→ Setting up theHarvester")
    clone_repo("theHarvester", "https://github.com/laramies/theHarvester.git")
    # dependencies installed via apt


def install_recon_ng():
    print("\n→ Setting up Recon-ng")
    clone_repo("recon-ng", "https://github.com/lanmaster53/recon-ng.git")
    # dependencies installed via apt


def install_metasploit():
    print("\n→ Installing Metasploit Framework from a release archive")
    ensure_curl()
    install_dir = os.path.join(OPT_DIR, "metasploit-framework")
    # Remove any existing install to ensure clean setup
    if os.path.isdir(install_dir):
        print(f"Removing existing directory {install_dir}…")
        run_cmd(["sudo", "rm", "-rf", install_dir])
    # Download the official release tarball (master branch snapshot)
    archive = "/tmp/msf.tar.gz"
    print("Downloading Metasploit archive…")
    run_cmd(["curl", "-L",
             "https://github.com/rapid7/metasploit-framework/archive/refs/heads/master.tar.gz",
             "-o", archive])
    # Extract into /opt/metasploit-framework
    run_cmd(["sudo", "mkdir", "-p", install_dir])
    run_cmd(["sudo", "tar", "-xzf", archive,
            "--strip-components=1", "-C", install_dir])
    # Install system dependencies
    deps = ["build-essential", "libssl-dev", "libpq-dev",
            "libreadline-dev", "ruby-dev", "libyaml-dev"]
    print("Installing system dependencies…")
    run_cmd(["sudo", "apt", "update"])
    run_cmd(["sudo", "apt", "install", "-y"] + deps)
    # Install Bundler and Ruby gems and Ruby gems
    print("Installing Ruby bundler and Metasploit gems…")
    run_cmd(["sudo", "gem", "install", "bundler"])
    run_cmd(["sudo", "bundle", "install", "--without",
            "development", "test"], cwd=install_dir)


def install_zaproxy():
    print("\n→ Installing OWASP ZAP")
    dest = os.path.join(OPT_DIR, "zap")
    os.makedirs(dest, exist_ok=True)
    tarball = os.path.join(dest, "zap.tar.gz")
    run_cmd(["wget",
             "https://github.com/zaproxy/zaproxy/releases/download/v2.15.0/ZAP_2.15.0_Linux.tar.gz",
             "-O", tarball])
    run_cmd(["tar", "-xzf", tarball, "-C", dest])


def install_burp_suite():
    print("\n→ Installing Burp Suite")
    dest = os.path.join(OPT_DIR, "burp")
    os.makedirs(dest, exist_ok=True)
    installer = os.path.join(dest, "burpsuite.sh")
    run_cmd(["wget",
             "https://portswigger-cdn.net/burp/releases/download?product=community&version=2024.4.1&type=Linux",
             "-O", installer])
    run_cmd(["chmod", "+x", installer])
    run_cmd([installer])


def install_empire():
    print("\n→ Installing Empire")
    path = clone_repo("Empire", "https://github.com/BC-SECURITY/Empire.git")
    run_cmd(["sudo", "./setup/install.sh"], cwd=path)


def show_manual():
    print("\n★ Manual‑install tools:")
    print("   • Nessus:        https://www.tenable.com/downloads/nessus")
    print("   • Cobalt Strike: https://www.cobaltstrike.com/")
    print("   • Kismet:        https://www.kismetwireless.net/")


def main():
    if os.geteuid() != 0:
        print("Run this script with sudo or as root.")
        sys.exit(1)

    os.makedirs(OPT_DIR, exist_ok=True)
    # install_system_packages()
    # install_theharvester()
    # install_recon_ng()
    # install_metasploit()

    install_zaproxy()
    # install_burp_suite()
    # install_empire()
    show_manual()
    print("\nAll set (or next steps shown above).")


if __name__ == "__main__":
    main()
