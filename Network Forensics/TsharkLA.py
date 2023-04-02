import subprocess

# Path to directory to store PCAP files
output_dir = "/path/to/output/dir"

# Run Tshark to capture network traffic and save to PCAP file
pcap_filename = os.path.join(output_dir, "network_capture.pcap")
subprocess.run(["tshark", "-i", "eth0", "-w", pcap_filename])

# Run Tshark to extract metadata from PCAP file
metadata_filename = os.path.join(output_dir, "network_metadata.txt")
subprocess.run(["tshark", "-r", pcap_filename, "-T", "fields", "-E", "separator=,", "-E", "header=y", "-e", "frame.time_epoch", "-e", "ip.src", "-e", "ip.dst", "-e", "tcp.srcport", "-e", "tcp.dstport", "-E", "occurrence=f", "-E", "aggregator=,count()", "-E", "aggregator=,unique(ip.src)", "-E", "aggregator=,unique(ip.dst)", "-E", "aggregator=,unique(tcp.srcport)", "-E", "aggregator=,unique(tcp.dstport)", "-E", "aggregator=,sum(tcp.len)", "-E", "aggregator=,sum(ip.len)", "-E", "aggregator=,sum(ip.flags.mf)", "-E", "aggregator=,sum(tcp.flags.fin)", "-E", "aggregator=,sum(tcp.flags.syn)", "-E", "aggregator=,sum(tcp.flags.ack)", "-E", "aggregator=,sum(tcp.flags.push)", "-E", "aggregator=,sum(tcp.flags.reset)", "-E", "aggregator=,sum(tcp.flags.urg)", "-E", "aggregator=,sum(tcp.analysis.ack_rtt)", "-E", "aggregator=,sum(tcp.analysis.bytes_in_flight)", "-E", "aggregator=,sum(tcp.analysis.retransmitted_packets)"], stdout=open(metadata_filename, "w"))
