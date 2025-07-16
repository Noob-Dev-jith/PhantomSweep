import subprocess
import os

def run(domain):
    print(f"[+] Running assetfinder on {domain}...\n")

    output_dir = f"output/{domain}"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    output_file = f"{output_dir}/subdomains.txt"

    try:
        with open(output_file, "w") as f:
            subprocess.run(["assetfinder", "--subs-only", domain], stdout=f, check=True)
        print(f"[+] Subdomain enumeration complete. Results saved in {output_file}\n")
    except subprocess.CalledProcessError:
        print("[-] Failed to run assetfinder. Is it installed?\n")
