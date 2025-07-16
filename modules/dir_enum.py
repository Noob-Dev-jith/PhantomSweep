import subprocess
import os

def run(target):
    print(f"[+] Running Gobuster Directory Scan on {target}...\n")

    wordlist = "/usr/share/wordlists/dirb/common.txt"  # Use your favorite wordlist here

    output_dir = f"output/{target}"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    output_file = f"{output_dir}/dir_enum.txt"

    url = f"http://{target}"

    try:
        subprocess.run([
    "gobuster", "dir",
    "-u", url,
    "-w", wordlist,
    "-t", "50",
    "-o", output_file,
    "--no-error",
    "--status-codes-blacklist", "301"
], check=True)
        print(f"[+] Directory enumeration complete. Results saved in {output_file}\n")
    except subprocess.CalledProcessError:
        print("[-] Error running Gobuster. Make sure it’s installed.\n")
