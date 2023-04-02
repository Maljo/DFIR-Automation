_________
ZeekFA.py zeek file analysis 
This script captures network traffic with tshark, calculates the MD5 hash of the capture file, and logs the capture file's filename, hash, and capture time. It then analyzes the captured traffic with Zeek, calculates the MD5 hash of each Zeek log file, and logs each log file's filename and hash. The script also performs file hash analysis on any suspicious files found in the Zeek logs and logs the filenames and hashes of any suspicious files. All log entries are written to a log file in the output directory.

___________
ZeekHTTP.py
This code uses the tshark utility to capture HTTP traffic on the specified interface for the specified duration, and the Zeek network security monitor to extract HTTP metadata from the captured traffic and write it to a log file. The code then reads the Zeek log file to identify the file paths of any files that were transferred over HTTP, and computes the SHA-256 hash value of each file using the hashlib module. Finally, the code prints the file path and hash value of each file to the console.

___________
TsharkLA.py
This code captures network traffic on interface eth0 using Tshark and saves it to a PCAP file in the specified output directory. It then runs Tshark again to extract metadata from the PCAP file, including source and destination IP addresses and ports, packet counts, and various TCP analysis fields, and saves it to a text file in the same output directory.
