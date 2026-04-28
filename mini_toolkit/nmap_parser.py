import subprocess
import argparse

def run_nmap(target, output_file):
    print(f"[+] Scanning {target}...")
    cmd = ["nmap", "-sV", "-oX", output_file, target]

    try:
        subprocess.run(cmd, check=True)
        print(f"[+] Scan selesai. File tersimpan: {output_file}")
    except subprocess.CalledProcessError:
        print("[-] Terjadi error saat menjalankan Nmap.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simple Nmap Scanner")
    parser.add_argument("--target", required=True, help="Target IP/domain")
    parser.add_argument("--out", required=True, help="Output XML file")
    args = parser.parse_args()

    run_nmap(args.target, args.out)
