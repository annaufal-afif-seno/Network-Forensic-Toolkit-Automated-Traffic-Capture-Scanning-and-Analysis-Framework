import argparse
import subprocess
import re

def valid_target(target):
    return re.match(r"^[\w\.\-]+$", target)

def scan(target, output):
    if not valid_target(target):
        print("[-] Target tidak valid")
        return
    
    print(f"[+] Scanning {target}...")
    cmd = ["nmap", "-oX", output, target]
    subprocess.run(cmd)
    print("[+] Scan selesai")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--target", required=True)
    parser.add_argument("--out", required=True)
    
    args = parser.parse_args()
    scan(args.target, args.out)
