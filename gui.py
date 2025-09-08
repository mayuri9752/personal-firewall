import tkinter as tk
from tkinter import ttk
from threading import Thread
from scapy.all import sniff
from firewall_rules import load_rules, match_packet
from logger import log_packet
import time

rules = load_rules()

class FirewallGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Personal Firewall")
        self.tree = ttk.Treeview(root, columns=('Time', 'Action', 'Packet'), show='headings')
        self.tree.heading('Time', text='Time')
        self.tree.heading('Action', text='Action')
        self.tree.heading('Packet', text='Packet Summary')
        self.tree.pack(fill=tk.BOTH, expand=True)
        Thread(target=self.start_sniffing, daemon=True).start()

    def start_sniffing(self):
        sniff(prn=self.process_packet, store=0)

    def process_packet(self, packet):
        action = match_packet(packet, rules)
        now = time.strftime('%H:%M:%S')
        if action == "block":
            log_packet(packet)
        self.tree.insert('', 'end', values=(now, action, packet.summary()))

if __name__ == "__main__":
    root = tk.Tk()
    app = FirewallGUI(root)
    root.mainloop()
