import os

# Prompt user for the location to save the memory dump
output_dir = input("Enter the path to the output directory: ")

# Create the output directory if it does not exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Collect the memory dump using Volatility Framework's imagecopy plugin
dump_name = input("Enter the name for the memory dump file: ")
os.system(f"volatility -f memory_dump.mem imagecopy -O {dump_name} --output-file {os.path.join(output_dir, dump_name)}")
