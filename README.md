<HEAD
## personal-firewall
## Personal Firewall using Python

A lightweight Python-based personal firewall using Scapy for packet sniffing, JSON rules for traffic filtering, and optional iptables + GUI support.
🚀 Features
- Real-time packet monitoring
- IP/Port/Protocol-based filtering
- Logging of blocked/suspicious packets
- CLI interface
- Optional GUI (Tkinter)
- iptables integration (Linux)

📁 Project Structure
- `main.py` – Runs the firewall
- `cli.py` – Command-line interface
- `gui.py` – GUI for monitoring (optional)
- `firewall_rules.py` – Rule matcher
- `logger.py` – Logs blocked packets
- `iptables_manager.py` – System-level blocking
- `rules.json` – Custom filtering rules

🛠️ Requirements
- Python 3.x
- Linux OS

-Methodology
-The firewall was developed step by step as follows:

1. Packet Sniffing
- Used Scapy to capture live packets.
- Displayed packet summaries in real-time.
2. Rule Definition
- Rules were defined in a JSON configuration file (rules.json).
- Example rules include blocked IPs, blocked ports (e.g., SSH/Telnet), and blocked protocols (e.g., ICMP).
3. Rule Application & Filtering
- Each captured packet is checked against the rule set.
- If a rule matches, the packet is marked as BLOCKED; otherwise, it is ALLOWED.
4. Logging
- All packet actions are logged into firewall.log with timestamps for auditing.
5. System-Level Enforcement (Optional)
- Using iptables, matching packets are dropped at the kernel level.
- The script creates a dedicated chain (FW_PY) to avoid interfering with other rules.
6. Graphical User Interface (Optional)
- Tkinter-based GUI displays live packets.
- Provides an option to add a blocked IP dynamically.


- System Archietecture:
- workflow:
          ┌────────────┐
          │  Packets   │
          └─────┬──────┘
                │
          ┌─────▼──────┐
          │  Scapy     │   (Packet Sniffing)
          └─────┬──────┘
                │
        ┌───────▼────────┐
        │ Rule Engine     │ (Check IPs, Ports, Protocols)
        └───────┬────────┘
     ┌───────────┼───────────┐
     │                           │
┌────▼────┐                 ┌────▼──────┐
│ ALLOWED │                 │ BLOCKED   │
└────┬────┘                 └────┬──────┘
     │                           │
     ▼                           ▼
 Logging File                Logging File + iptables DROP

## Implementation
Configuration File (rules.json)
{
  "block_ips": ["192.168.1.10"],
  "block_ports": [22, 23],
  "block_protocols": ["ICMP"]
}

# Execution Command:
sudo python3 firewall.py --config rules.json
# Run with iptables enforcement:
sudo python3 firewall.py --config rules.json --iptables
# Run GUI:
sudo python3 firewall.py --config rules.json --gui --iptables

## Results
1. Successfully captured and analyzed packets using Scapy.
2. Implemented a rule-based filtering engine.
3. Logged all packet activity with clear status (ALLOWED / BLOCKED).
4. Integrated iptables to enforce real-time blocking at the system level.
5. Developed a Tkinter GUI for live monitoring and interactive rule addition.

## Conclusion
The project successfully demonstrates how a personal firewall can be built using Python. It provides both monitoring and enforcement features, along with a GUI for ease of use.

# Key achievements:
1. Lightweight and customizable firewall.
2. Effective logging of suspicious activity.
3. Optional integration with system-level blocking (iptables).
4. Extendable architecture (new rules or protocols can be added easily).
