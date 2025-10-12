import subprocess 
import json 
import os

def execute(command):
    result = subprocess.run(
        command,
        capture_output=True,  
        text=True            
    )
    return result.stdout

def list_ips():
    # Determine network name. 
    network_name = \
        os.environ.get("PROJECT_FULL_NAME") + \
        "_" + \
        "project"

    # Get network info.
    network_info = execute(
        ["docker", "network", "inspect", network_name]
    )
    network_info = json.loads(network_info)[0]

    # Get ip list. 
    containers = network_info["Containers"]
    ip_map = {} 
    name_prefix = os.environ.get("PROJECT_FULL_NAME") + "_"

    for container_id in containers: 
        container_info = containers[container_id]
        shortname = container_info['Name'][len(name_prefix):]
        if container_info['Name'] == "dkhfst-dns": 
            shortname = "dns"
        ip_map[shortname] = container_info['IPv4Address'][:-3]

    return ip_map

def dns_entries(): 
    ip_list = list_ips()
    domain_name = os.environ.get("PROJECT_DOMAIN_NAME")
    mode = os.environ.get("PROJECT_RUNTIME_MODE")
    mode_upper = mode.upper() 
    extension = os.environ.get("PROJECT_DN_EXT_" + mode_upper) 
    full_domain_name = domain_name + extension
    target_ip = ip_list["router"]

    entries = [
        f"address=/{full_domain_name}/{target_ip}", 
        f"address=/*.{full_domain_name}/{target_ip}", 
    ]

    return "\n".join(entries)