import os

import hashlib

# Set the output directory for collected data

output_dir = "C:/DFIR/RegistryForensics/"

# Create the output directory if it doesn't exist

if not os.path.exists(output_dir):

    os.makedirs(output_dir)

# Collect registry hive files

registry_files = [

    "C:/Windows/System32/config/SYSTEM",

    "C:/Windows/System32/config/SOFTWARE",

    "C:/Users/<username>/NTUSER.DAT"

]

for registry_file in registry_files:

    # Generate a hash of the registry file

    with open(registry_file, "rb") as f:

        registry_file_hash = hashlib.md5(f.read()).hexdigest()

    

    # Copy the registry file to the output directory with its hash appended to the name

    registry_filename = os.path.basename(registry_file)

    registry_filename_hashed = f"{os.path.splitext(registry_filename)[0]}_{registry_file_hash}.hive"

    registry_file_output_path = os.path.join(output_dir, registry_filename_hashed)

    os.system(f"reg save HKLM\\SYSTEM {registry_file_output_path}")

    

    # Analyze the registry file with RegRipper

    regripper_output_dir = os.path.join(output_dir, "RegRipper_Output")

    if not os.path.exists(regripper_output_dir):

        os.makedirs(regripper_output_dir)

    os.system(f"rip.exe -r {registry_file_output_path} -f {regripper_output_dir}")

    

    # Generate a hash of the RegRipper output files

    regripper_output_files = os.listdir(regripper_output_dir)

    for regripper_output_file in regripper_output_files:

        with open(os.path.join(regripper_output_dir, regripper_output_file), "rb") as f:

            regripper_output_file_hash = hashlib.md5(f.read()).hexdigest()

        regripper_output_file_output_path = os.path.join(regripper_output_dir, f"{os.path.splitext(regripper_output_file)[0]}_{regripper_output_file_hash}.txt")

        os.rename(os.path.join(regripper_output_dir, regripper_output_file), regripper_output_file_output_path)

