from scapy.all import sniff

def packet_callback(packe):
    print(packet.summary())

print("✅ Starting packet sniffer...")
# Sniff packets on eth0 or change to wlan0 if on Wi-Fi
sniff(prn=packet_callback, store=False)




