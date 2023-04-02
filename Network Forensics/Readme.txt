_________
ZeekFA.py
This script captures network traffic with tshark, calculates the MD5 hash of the capture file, and logs the capture file's filename, hash, and capture time. It then analyzes the captured traffic with Zeek, calculates the MD5 hash of each Zeek log file, and logs each log file's filename and hash. The script also performs file hash analysis on any suspicious files found in the Zeek logs and logs the filenames and hashes of any suspicious files. All log entries are written to a log file in the output directory.



