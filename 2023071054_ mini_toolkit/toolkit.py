import os

os.system("python3 capture_tool.py --iface eth0 --seconds 10 --out traffic.pcap")
os.system("python3 scan_tool.py --target 127.0.0.1 --out scan.xml")
