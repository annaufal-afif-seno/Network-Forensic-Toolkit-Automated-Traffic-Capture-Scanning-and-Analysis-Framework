import argparse
import subprocess
import time

def capture(iface, seconds, output):
    print(f"[+] Start capture on {iface} for {seconds} seconds...")

    cmd = ["sudo", "tcpdump", "-i", iface, "-w", output]
    proc = subprocess.Popen(cmd)

    time.sleep(seconds)

    proc.terminate()
    proc.wait()

    print("[+] Capture selesai, file:", output)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--iface", required=True)
    parser.add_argument("--seconds", type=int, default=10)
    parser.add_argument("--out", required=True)

    args = parser.parse_args()
    capture(args.iface, args.seconds, args.out)