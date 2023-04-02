__________
Regdump.py
Python code to automate the collection of DFIR registry forensics:
This code will collect the specified registry hives and save them as individual files in the specified output directory. It will also calculate the hash of each file using the specified hash algorithm and append it to the filename


________
RegDA.py

Python code to automate the collection and analysis of DFIR registry forensics with file hash details:

This code collects registry hive files, generates a hash of each file, and copies it to the output directory with the hash appended to the name. The code then analyzes each registry file with RegRipper, saves the output files to a separate directory, generates a hash of each output file, and renames it with the hash appended to the name. This ensures that each collected and analyzed file has a unique name and can be easily referenced.
