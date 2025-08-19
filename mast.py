#!/usr/bin/env python3
import os

# ============ قائمة الأدوات (50 أداة) ============
tools = {
    "nmap": {"install": "apt install -y nmap", "example": "nmap -sV target.com"},
    "sqlmap": {"install": "apt install -y sqlmap", "example": 'sqlmap -u "http://target.com/page.php?id=1" --batch --level=2 --risk=2'},
    "hydra": {"install": "apt install -y hydra", "example": "hydra -l admin -P passwords.txt target.com ssh"},
    "wireshark": {"install": "apt install -y wireshark", "example": "wireshark &"},
    "aircrack-ng": {"install": "apt install -y aircrack-ng", "example": "aircrack-ng handshake.cap -w wordlist.txt"},
    "john": {"install": "apt install -y john", "example": "john --wordlist=passwords.txt hashes.txt"},
    "hashcat": {"install": "apt install -y hashcat", "example": "hashcat -m 0 -a 0 hashes.txt wordlist.txt"},
    "metasploit-framework": {"install": "apt install -y metasploit-framework", "example": "msfconsole"},
    "theharvester": {"install": "apt install -y theharvester", "example": "theharvester -d target.com -l 500 -b google"},
    "dnsenum": {"install": "apt install -y dnsenum", "example": "dnsenum target.com"},
    "whois": {"install": "apt install -y whois", "example": "whois target.com"},
    "ettercap": {"install": "apt install -y ettercap-text-only", "example": "ettercap -T -M arp:remote /target1/ /target2/"},
    "setoolkit": {"install": "apt install -y set", "example": "setoolkit"},
    "beef": {"install": "apt install -y beef-xss", "example": "beef-xss"},
    "nikto": {"install": "apt install -y nikto", "example": "nikto -h target.com"},
    "wpscan": {"install": "apt install -y wpscan", "example": "wpscan --url target.com"},
    "netcat": {"install": "apt install -y netcat", "example": "nc -lvp 4444"},
    "smbmap": {"install": "apt install -y smbmap", "example": "smbmap -H target.com"},
    "enum4linux": {"install": "apt install -y enum4linux", "example": "enum4linux target.com"},
    "crackmapexec": {"install": "apt install -y crackmapexec", "example": "cme smb target.com -u user -p pass"},
    "recon-ng": {"install": "apt install -y recon-ng", "example": "recon-ng"},
    "amass": {"install": "apt install -y amass", "example": "amass enum -d target.com"},
    "gobuster": {"install": "apt install -y gobuster", "example": "gobuster dir -u http://target.com -w wordlist.txt"},
    "dirb": {"install": "apt install -y dirb", "example": "dirb http://target.com /usr/share/wordlists/dirb/common.txt"},
    "feroxbuster": {"install": "apt install -y feroxbuster", "example": "feroxbuster -u http://target.com -w wordlist.txt"},
    "sublist3r": {"install": "apt install -y sublist3r", "example": "sublist3r -d target.com"},
    "sslscan": {"install": "apt install -y sslscan", "example": "sslscan target.com"},
    "whatweb": {"install": "apt install -y whatweb", "example": "whatweb target.com"},
    "maltego": {"install": "apt install -y maltego", "example": "maltego"},
    "exploitdb": {"install": "apt install -y exploitdb", "example": "searchsploit apache"},
    "openvas": {"install": "apt install -y openvas", "example": "openvas-start"},
    "lynis": {"install": "apt install -y lynis", "example": "lynis audit system"},
    "chkrootkit": {"install": "apt install -y chkrootkit", "example": "chkrootkit"},
    "rkhunter": {"install": "apt install -y rkhunter", "example": "rkhunter --check"},
    "tcpdump": {"install": "apt install -y tcpdump", "example": "tcpdump -i eth0"},
    "ngrep": {"install": "apt install -y ngrep", "example": "ngrep -d eth0"},
    "tshark": {"install": "apt install -y tshark", "example": "tshark -i eth0"},
    "yara": {"install": "apt install -y yara", "example": "yara rule.yar file.exe"},
    "volatility": {"install": "apt install -y volatility", "example": "volatility -f memory.dump pslist"},
    "ghidra": {"install": "apt install -y ghidra", "example": "ghidra"},
    "radare2": {"install": "apt install -y radare2", "example": "r2 /bin/ls"},
    "apktool": {"install": "apt install -y apktool", "example": "apktool d app.apk"},
    "dex2jar": {"install": "apt install -y dex2jar", "example": "d2j-dex2jar app.apk"},
    "burpsuite": {"install": "apt install -y burpsuite", "example": "burpsuite"},
    "tor": {"install": "apt install -y tor", "example": "tor"},
    "proxychains": {"install": "apt install -y proxychains", "example": "proxychains firefox target.com"},
    "httrack": {"install": "apt install -y httrack", "example": "httrack http://target.com -O ./mirror"},
    "dsniff": {"install": "apt install -y dsniff", "example": "arpspoof -i eth0 -t target gateway"}
}

# ============ الواجهة ============
def show_menu():
    print("\n" + "="*50)
    print("🔥      MAST - Tool Manager (50 Tools)      🔥")
    print("="*50)
    print("[1] Install a tool")
    print("[2] Show example command")
    print("[3] Show supported tools")
    print("[4] Exit")
    print("="*50)

def install_tool():
    name = input("Enter the tool name to install: ").strip()
    if name in tools:
        print(f"⚙️  Installing {name}...\n")
        os.system(tools[name]["install"])
    else:
        print("❌ Tool not supported or name incorrect.")

def show_example():
    name = input("Enter the tool name: ").strip()
    if name in tools:
        print(f"\n💡 Example command for {name}:")
        print(tools[name]["example"])
    else:
        print("❌ Tool not supported or name incorrect.")

def show_supported():
    print("\n✅ Supported tools (50):")
    for t in tools.keys():
        print("-", t)

def main():
    while True:
        show_menu()
        choice = input("Choose an option: ").strip()
        if choice == "1":
            install_tool()
        elif choice == "2":
            show_example()
        elif choice == "3":
            show_supported()
        elif choice == "4":
            print("👋 Bye from MAST!")
            break
        else:
            print("❌ Invalid choice, try again.")

if __name__ == "__main__":
    main()
