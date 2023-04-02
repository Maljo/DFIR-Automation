import os

import subprocess

import hashlib

# define output directory

output_dir = "/path/to/output/dir"

# define capture interface

capture_interface = "eth0"

# define capture duration

capture_duration = "60"

# define capture filter

capture_filter = "port 80"

# define Zeek log file path

zeek_http_log = os.path.join(output_dir, "http.log")

# define tshark output file path

tshark_http_pcap = os.path.join(output_dir, "http.pcap")

# capture HTTP traffic with tshark

os.system(f"sudo tshark -i {capture_interface} -a duration:{capture_duration} -w {tshark_http_pcap} {capture_filter}")

# extract HTTP metadata with Zeek

os.system(f"sudo zeek -r {tshark_http_pcap} http > {zeek_http_log}")

# compute hash values of captured files

with open(zeek_http_log, "r") as f:

    for line in f:

        if line.startswith("#close_time"):

            # extract file path from Zeek log

            file_path = line.split("\t")[7]

            # compute hash value of file

            with open(file_path, "rb") as f2:

                file_content = f2.read()

                file_hash = hashlib.sha256(file_content).hexdigest()

            # print file path and hash value

            print(f"File path: {file_path} | Hash value: {file_hash}")

