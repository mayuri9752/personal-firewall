
import logging

logging.basicConfig(filename='firewall.log', level=logging.INFO, format='%(asctime)s - %(message)s')

def log_packet(packet, reason="Blocked"):
    logging.info(f"{reason}: {packet.summary()}")

