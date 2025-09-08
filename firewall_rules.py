
import json

def load_rules(filename="rules.json"):
    with open(filename, "r") as file:
        return json.load(file)

def match_packet(packet, rules):
    if packet.haslayer("IP"):
        ip_layer = packet["IP"]
        for rule in rules:
            if rule.get("ip") and (ip_layer.src == rule["ip"] or ip_layer.dst == rule["ip"]):
                return rule["action"]
            if rule.get("protocol") and rule["protocol"].lower() in packet:
                return rule["action"]
            if rule.get("port") and hasattr(packet.payload, "dport"):
                if packet.payload.dport == rule["port"]:
                    return rule["action"]
    return "allow"
