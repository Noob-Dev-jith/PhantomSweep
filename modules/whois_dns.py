import subprocess
import os

def run(domain):
    print(f"[+] Running WHOIS and DNS lookup on {domain}...\n")

    output_dir = f"output/{domain}"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    whois_out = f"{output_dir}/whois.txt"
    dns_out = f"{output_dir}/dns.txt"

    try:
        with open(whois_out, "w") as f:
            subprocess.run(["whois", domain], stdout=f, stderr=subprocess.DEVNULL)

        with open(dns_out, "w") as f:
            subprocess.run(["dig", domain, "any", "+noall", "+answer"], stdout=f, stderr=subprocess.DEVNULL)

        print(f"[+] WHOIS saved to {whois_out}")
        print(f"[+] DNS info saved to {dns_out}\n")

    except Exception as e:
        print(f"[-] Error: {e}\n")
