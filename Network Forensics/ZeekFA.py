import os

import hashlib

import datetime

# Define output directory

output_dir = "network_forensics_output"

# Check if output directory exists, create if not

if not os.path.exists(output_dir):

    os.makedirs(output_dir)

# Capture network traffic with tshark

capture_filename = os.path.join(output_dir, "network_capture.pcap")

os.system(f"tshark -i eth0 -w {capture_filename}")

# Calculate MD5 hash of captured file

with open(capture_filename, 'rb') as f:

    capture_hash = hashlib.md5(f.read()).hexdigest()

# Write capture hash to log file

log_filename = os.path.join(output_dir, "capture_log.txt")

with open(log_filename, 'a') as f:

    f.write(f"Capture File: {capture_filename}\n")

    f.write(f"MD5 Hash: {capture_hash}\n")

    f.write(f"Capture Time: {datetime.datetime.now()}\n\n")

# Analyze captured traffic with Zeek

zeek_output_dir = os.path.join(output_dir, "zeek_output")

os.system(f"zeek -r {capture_filename} -C -U {zeek_output_dir}")

# Calculate MD5 hash of Zeek log files

log_files = os.listdir(zeek_output_dir)

log_hashes = {}

for log_file in log_files:

    if log_file.endswith(".log"):

        with open(os.path.join(zeek_output_dir, log_file), 'rb') as f:

            log_hashes[log_file] = hashlib.md5(f.read()).hexdigest()

# Write log file hashes to log file

with open(log_filename, 'a') as f:

    f.write("Zeek Log File Hashes:\n")

    for log_file, log_hash in log_hashes.items():

        f.write(f"{log_file}: {log_hash}\n")

    f.write("\n")

# Perform file hash analysis on suspicious files

suspicious_files = []

for log_file in log_files:

    if log_file.endswith(".log"):

        with open(os.path.join(zeek_output_dir, log_file), 'r') as f:

            for line in f:

                if "ET POLICY Suspicious inbound to MSSQL port" in line:

                    filename = line.split()[-1]

                    suspicious_files.append(filename)

# Calculate MD5 hash of suspicious files

suspicious_hashes = {}

for filename in suspicious_files:

    with open(os.path.join(zeek_output_dir, "files", filename), 'rb') as f:

        suspicious_hashes[filename] = hashlib.md5(f.read()).hexdigest()

# Write suspicious file hashes to log file

with open(log_filename, 'a') as f:

    f.write("Suspicious File Hashes:\n")

    for filename, file_hash in suspicious_hashes.items():

        f.write(f"{filename}: {file_hash}\n")

    f.write("\n")

