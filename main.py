import os
import modules.whois_dns as whois_dns
import modules.subdomains as subdomains
import modules.portscan as portscan
import modules.dir_enum as dir_enum
import modules.vulnscan as vulnscan

def banner():
    print(r"""
__________.__                   __                   _________                             
\______   \  |__ _____    _____/  |_  ____   _____  /   _____/_  _  __ ____   ____ ______  
 |     ___/  |  \\__  \  /    \   __\/  _ \ /     \ \_____  \\ \/ \/ // __ \_/ __ \\____ \ 
 |    |   |   Y  \/ __ \|   |  \  | (  <_> )  Y Y  \/        \\     /\  ___/\  ___/|  |_> >
 |____|   |___|  (____  /___|  /__|  \____/|__|_|  /_______  / \/\_/  \___  >\___  >   __/ 
               \/     \/     \/                  \/        \/             \/     \/|__|    

               🥷 Welcome to PhantomSweep | Recon Framework 🌸
                     Created for stealthy scans & intel
    """)

def show_menu():
    print("\n🧠 === AutoRecon Framework Menu ===")
    print("1. 🔁 Full Recon")
    print("2. 🌐 WHOIS & DNS Lookup")
    print("3. 🔎 Subdomain Enumeration")
    print("4. 🚪 Port Scan (Advanced)")
    print("5. 📁 Directory Brute Force")
    print("6. 🚫 Exit")

def main():
    banner()
    target = input("\n🎯 Enter the target domain (e.g., example.com): ").strip()

    if '.' not in target:
        print("❌ Invalid domain format. Please enter a valid FQDN (e.g., example.com)")
        return

    output_dir = f"output/{target}"
    os.makedirs(output_dir, exist_ok=True)

    while True:
        show_menu()
        choice = input("\n➡️ Choose an option (1-6): ").strip()

        if choice == "1":
            whois_dns.run(target)
            subdomains.run(target)
            portscan.run(target)
            dir_enum.run(target)
            vulnscan.run(target)
        elif choice == "2":
            whois_dns.run(target)
        elif choice == "3":
            subdomains.run(target)
        elif choice == "4":
            portscan.run(target)
        elif choice == "5":
            dir_enum.run(target)
        elif choice == "6":
            print("👋 Exiting PhantomSweep. Stay stealthy, warrior.")
            break
        else:
            print("⚠️ Invalid option. Please choose from 1 to 6.")

if __name__ == "__main__":
    main()
