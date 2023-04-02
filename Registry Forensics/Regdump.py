import os

import hashlib

# Set output directory for collected artifacts

output_dir = "/path/to/output/directory"

# Create output directory if it does not exist

if not os.path.exists(output_dir):

    os.makedirs(output_dir)

# List of registry hives to collect

registry_hives = [

    "HKEY_LOCAL_MACHINE\\SYSTEM",

    "HKEY_LOCAL_MACHINE\\SAM",

    "HKEY_LOCAL_MACHINE\\SOFTWARE",

    "HKEY_LOCAL_MACHINE\\SECURITY",

    "HKEY_USERS\\.DEFAULT",

    "HKEY_USERS\\S-1-5-18",

    "HKEY_USERS\\S-1-5-19",

    "HKEY_USERS\\S-1-5-20"

]

# Hashing algorithm to use

hash_algorithm = "sha256"

# Collect registry hives and calculate hashes

for hive in registry_hives:

    # Set output file path

    hive_filename = os.path.join(output_dir, "{}.reg".format(hive.replace("\\", "_")))

    

    # Collect registry hive and write to file

    os.system("reg save {} {} > {}".format(hive, hive_filename, os.path.join(output_dir, hive_filename)))

    

    # Calculate hash of output file

    with open(hive_filename, "rb") as f:

        file_hash = hashlib.new(hash_algorithm, f.read()).hexdigest()

    

    # Append hash to filename

    hash_filename = "{}_{}.reg".format(hive.replace("\\", "_"), file_hash)

    

    # Rename output file to include hash

    os.rename(hive_filename, os.path.join(output_dir, hash_filename))

