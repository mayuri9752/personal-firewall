from scapy.all import sniff
from firewall_rules import load_rules, match_packet
from logger import log_packet

rules = load_rules()

def process_packet(packet):
    action = match_packet(packet, rules)
    if action == "block":
        log_packet(packet)
    else:
        print("Allowed:", packet.summary())

sniff(prn=process_packet, store=False)
