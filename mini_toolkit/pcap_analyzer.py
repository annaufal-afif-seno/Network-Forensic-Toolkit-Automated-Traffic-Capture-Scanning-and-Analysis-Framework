from scapy.all import rdpcap, IP, TCP, UDP, ICMP, DNS
from collections import Counter

def analyze(pcap_file):
    packets = rdpcap(pcap_file)
    
    print(f"Total Packets: {len(packets)}")
    
    src_ips = []
    protocols = Counter()
    dns_queries = []
    
    for pkt in packets:
        if IP in pkt:
            src_ips.append(pkt[IP].src)
            
            if TCP in pkt:
                protocols["TCP"] += 1
            elif UDP in pkt:
                protocols["UDP"] += 1
            elif ICMP in pkt:
                protocols["ICMP"] += 1
        
        if pkt.haslayer(DNS) and pkt[DNS].qd:
            dns_queries.append(pkt[DNS].qd.qname.decode())
    
    print(f"Unique IPs: {len(set(src_ips))}")
    
    top = Counter(src_ips).most_common(5)
    print("Top Talkers:", top)
    
    print("Protocol Distribution:", protocols)
    
    print("DNS Queries:")
    for d in dns_queries:
        print("-", d)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", required=True)
    
    args = parser.parse_args()
    analyze(args.file)
