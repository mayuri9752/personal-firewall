import argparse
import os
from main import process_packet
from scapy.all import sniff
from iptables_manager import block_ip, unblock_all

parser = argparse.ArgumentParser(description="Python Personal Firewall CLI")
parser.add_argument('--start', action='store_true', help='Start the firewall')
parser.add_argument('--block-ip', type=str, help='Block an IP using iptables')
parser.add_argument('--unblock-all', action='store_true', help='Clear all iptables rules')
parser.add_argument('--show-log', action='store_true', help='Show log file')

args = parser.parse_args()

if args.start:
    sniff(prn=process_packet, store=0)

if args.block_ip:
    block_ip(args.block_ip)

if args.unblock_all:
    unblock_all()

if args.show_log:
    os.system("cat firewall.log")
