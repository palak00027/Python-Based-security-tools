
from scapy.all import sniff
from flask import Flask, render_template, jsonify, request
import threading
import pandas as pd
import time

app = Flask(__name__)

# Store captured packets
packets_list = []
LOG_FILE = "network_traffic_log.csv"
COLUMNS = ["Timestamp", "Source IP", "Destination IP", "Protocol", "Source Port", "Destination Port", "Packet Summary"]

# Create CSV file if not exists
def create_log_file():
    pd.DataFrame(columns=COLUMNS).to_csv(LOG_FILE, index=False, mode='w')

# Process captured packets
def process_packet(packet):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    src_ip = packet[0][1].src if packet.haslayer("IP") else "N/A"
    dst_ip = packet[0][1].dst if packet.haslayer("IP") else "N/A"
    protocol = packet[0][1].proto if packet.haslayer("IP") else "N/A"

    src_port = packet[0][2].sport if packet.haslayer("TCP") or packet.haslayer("UDP") else "N/A"
    dst_port = packet[0][2].dport if packet.haslayer("TCP") or packet.haslayer("UDP") else "N/A"

    summary = packet.summary()

    # Store in global list
    packets_list.append({
        "timestamp": timestamp,
        "source_ip": src_ip,
        "destination_ip": dst_ip,
        "protocol": protocol,
        "source_port": src_port,
        "destination_port": dst_port,
        "summary": summary
    })

    # Save packet details to CSV
    df = pd.DataFrame([[timestamp, src_ip, dst_ip, protocol, src_port, dst_port, summary]], columns=COLUMNS)
    df.to_csv(LOG_FILE, mode='a', header=False, index=False)

# Start sniffing in the background
def start_sniffing():
    print("Starting Packet Sniffer... Press Ctrl+C to stop.")
    sniff(prn=process_packet, store=False)

# Flask Routes
@app.route('/')
def home():
    return render_template("index.html")

@app.route('/packets', methods=['GET'])
def get_packets():
    filter_type = request.args.get('filter', 'all').lower()
    filtered_packets = []

    for packet in reversed(packets_list[-50:]):  # Show last 50 packets
        if filter_type == "all" or (
            (filter_type == "tcp" and packet["protocol"] == "6") or
            (filter_type == "udp" and packet["protocol"] == "17") or
            (filter_type == "icmp" and packet["protocol"] == "1")
        ):
            filtered_packets.append(packet)

    return jsonify(filtered_packets)

# Run Flask in a separate thread
if __name__ == "__main__":
    create_log_file()
    sniff_thread = threading.Thread(target=start_sniffing, daemon=True)
    sniff_thread.start()
    app.run(debug=True, port=5000)
