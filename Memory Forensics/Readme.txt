_______________
VolatilityDA.py

Python code to automate the collection of DFIR memory forensics using the Volatility framework:

The script sets the output directory, process name, process ID, Volatility path, profile, and plugin list. The script then creates the output directory and uses the memdump command from Volatility to dump the process memory to a file. The script then iterates over each plugin in the plugin list and runs the plugin against the memory dump file to generate a text output file in the output directory. Finally, the script prints a success message.

___________
Memdump.py:

Python code that prompts the user for the location to save the memory dump and runs the Volatility Framework's imagecopy plugin to collect the memory dump:
Note: The user needs to have Volatility Framework installed on their system and the memory_dump.mem file should be present in the current working directory.
