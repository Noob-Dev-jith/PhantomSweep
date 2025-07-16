import subprocess
import os

def run(target):
    print(f"[+] Running Nmap Port Scan on {target}...\n")

    output_dir = f"output/{target}"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    output_file = f"{output_dir}/nmap_scan.txt"

    try:
        subprocess.run([
    "nmap", "-p-", "-sS", "-sV", "-sC", "-T4", "--open",
    "--max-retries", "2", "--min-rate", "1000", "--script", "vuln",
    "-oN", f"output/{target}/nmap_advanced.txt", target ], check=True)
        print(f"[+] Port scan complete. Results saved in {output_file}\n")
    except subprocess.CalledProcessError:
        print("[-] Error running Nmap. Check if it's installed.\n")
