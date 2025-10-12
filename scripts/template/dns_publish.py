from helpers.python import dns_entries 
import os

dns_entries = dns_entries()
data_dir = os.environ.get("DKHFST_DATA_DIR")
dns_dir = data_dir + "/dns/"
filename = os.environ.get("PROJECT_FULL_NAME") + ".conf"
file_path = dns_dir + filename

open(file_path, "w").write(dns_entries)

