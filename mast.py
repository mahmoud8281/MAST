import os
import time

# قائمة الأدوات مع شرحها
tools = {
    "nmap": "أداة لفحص الشبكات واكتشاف الأجهزة والخدمات عليها. مثال: nmap -sV 192.168.1.1",
    "sqlmap": "أداة لاختبار قواعد البيانات ضد ثغرات SQL Injection. مثال: sqlmap -u 'http://site.com/index.php?id=1'",
    "hydra": "أداة هجوم تخمين كلمات المرور (Brute Force). مثال: hydra -l admin -P pass.txt ssh://192.168.1.5",
    "john": "John the Ripper لكسر كلمات المرور من ملفات هاش. مثال: john hash.txt",
    "hashcat": "أداة قوية لكسر كلمات المرور باستخدام كروت الشاشة. مثال: hashcat -m 0 hash.txt wordlist.txt",
    "aircrack-ng": "أداة لاختبار شبكات الواي فاي وكسر التشفير. مثال: aircrack-ng -w wordlist.txt capture.cap",
    "wireshark": "أداة رسومية لتحليل حركة الشبكة (Packet Sniffer).",
    "metasploit-framework": "إطار عمل للاختراق واستغلال الثغرات.",
    "set": "Social Engineering Toolkit لاختبار هجمات الهندسة الاجتماعية.",
    "beef": "أداة لاختبار أمان المتصفحات من خلال استغلال JavaScript.",
    "bettercap": "أداة متقدمة لعمل هجمات MITM وتحليل الشبكة.",
    "dnsenum": "أداة لجمع معلومات عن الـ DNS. مثال: dnsenum example.com",
    "theharvester": "أداة لاستخراج الإيميلات والدومينات من الإنترنت. مثال: theharvester -d example.com -l 100 -b google",
    "whois": "أداة لعرض معلومات تسجيل الدومينات. مثال: whois example.com",
    "enum4linux": "أداة لاستخراج معلومات من سيرفرات ويندوز (SMB/NetBIOS).",
    "dirb": "أداة لاكتشاف الملفات والمجلدات المخفية في المواقع. مثال: dirb http://site.com",
    "nikto": "أداة لاختبار أمان السيرفرات وكشف الثغرات. مثال: nikto -h http://site.com",
    "wpscan": "أداة لاختبار ثغرات ووردبريس. مثال: wpscan --url http://site.com",
    "gobuster": "أداة لاكتشاف المجلدات والـ DNS subdomains. مثال: gobuster dir -u http://site.com -w wordlist.txt",
    "recon-ng": "إطار عمل لجمع معلومات الاستطلاع عن الأهداف.",
    "netcat": "أداة قوية للتعامل مع الشبكات، فحص أو فتح اتصالات. مثال: nc -lvnp 4444",
    "openvas": "ماسح ثغرات متقدم للشبكات والخوادم.",
    "burpsuite": "أداة رسومية لاختبار تطبيقات الويب واعتراض الترافيك.",
    "angryip": "أداة مسح سريعة للشبكات. مثال: ipscan 192.168.1.0/24",
    "sublist3r": "أداة لجمع Subdomains. مثال: sublist3r -d example.com",
    "amass": "أداة لاكتشاف Subdomains بشكل متقدم.",
    "sslscan": "أداة لفحص إعدادات SSL. مثال: sslscan example.com",
    "whatweb": "أداة للتعرف على تقنيات المواقع. مثال: whatweb example.com",
    "curl": "أداة لإرسال واستقبال طلبات HTTP. مثال: curl http://example.com",
    "wget": "أداة لتحميل الملفات من الإنترنت. مثال: wget http://site.com/file.zip",
    "proxychains": "أداة لتشغيل البرامج خلف بروكسي أو Tor. مثال: proxychains firefox",
    "tor": "شبكة لتجاوز الحجب والتخفي على الإنترنت.",
    "masscan": "ماسح منافذ سريع جدًا. مثال: masscan -p1-65535 192.168.1.0/24",
    "netdiscover": "أداة لاكتشاف الأجهزة على الشبكة. مثال: netdiscover -r 192.168.1.0/24",
    "arp-scan": "أداة لاكتشاف الأجهزة عبر بروتوكول ARP.",
    "msfpc": "أداة لتوليد بايلودات بسرعة.",
    "responder": "أداة لالتقاط Hashes عبر SMB/NTLM.",
    "smbmap": "أداة للتعامل مع SMB ومشاركة الملفات.",
    "crunch": "مولد قوائم كلمات مرور مخصصة. مثال: crunch 8 8 abc123 -o pass.txt",
    "medusa": "أداة هجوم تخمين كلمات المرور مثل Hydra.",
    "ettercap": "أداة لعمل MITM وتحليل الشبكة.",
    "snort": "نظام كشف التسلل IDS.",
    "yara": "أداة لتحليل البرمجيات الخبيثة.",
    "volatility": "أداة تحليل الذاكرة RAM.",
    "radare2": "إطار عمل لتحليل الملفات التنفيذية (Reverse Engineering).",
    "ghidra": "أداة قوية من NSA لعمل Reverse Engineering.",
    "strings": "أداة لعرض النصوص من الملفات الثنائية. مثال: strings file.exe",
    "binwalk": "أداة لتحليل ملفات الفيرموير.",
    "apktool": "أداة لتفكيك تطبيقات أندرويد.",
    "jadx": "أداة لتحويل ملفات APK إلى كود Java مقروء."
}

# دالة التنصيب (مع إعادة المحاولة)
def install_tool(tool):
    print(f"\n[*] Trying to install: {tool}")
    while True:
        exit_code = os.system(f"apt install {tool} -y > /dev/null 2>&1")
        if exit_code == 0:
            print(f"[+] {tool} installed successfully!\n")
            break
        else:
            print(f"[-] Failed to install {tool}, retrying...")
            time.sleep(2)

# شرح الأداة
def explain_tool(tool_name):
    if tool_name in tools:
        print(f"\n[شرح] {tool_name}:")
        print(tools[tool_name])
    else:
        print("[-] الأداة غير موجودة في القائمة.")

# عرض الأدوات + البحث
def list_tools():
    print("\n[+] الأدوات المدعومة:\n")
    for i, tool in enumerate(tools.keys(), 1):
        print(f"{i}. {tool}")

    q = input("\nابحث عن أداة (أو اضغط Enter للخروج): ")
    if q:
        found = False
        for tool in tools.keys():
            if q.lower() in tool.lower():
                print(f"[+] Found: {tool}")
                found = True
        if not found:
            print("[-] لم يتم العثور على أداة بهذا الاسم.")

# القائمة الرئيسية
def main():
    while True:
        print("""
==========================
 MAST - Multi Tool Script
==========================
1) تنصيب أداة
2) شرح أداة
3) عرض/بحث الأدوات
4) خروج
""")
        choice = input("اختر: ")
        if choice == "1":
            tool = input("أدخل اسم الأداة: ")
            install_tool(tool)
        elif choice == "2":
            tool = input("أدخل اسم الأداة: ")
            explain_tool(tool)
        elif choice == "3":
            list_tools()
        elif choice == "4":
            break
        else:
            print("[-] خيار غير صحيح.")

if __name__ == "__main__":
    main()