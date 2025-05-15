import re


def parse_show_vlan_brief(host: str, hostname: str, output: str) -> dict:
    """
    Parses the output of 'show vlan brief' into a dict.
    """
    vlans = []
    parsed_output = output.split("\n")

    for line in parsed_output:
        # Skip headers and empty lines
        if not line.strip() or line.startswith("VLAN") or line.startswith("----"):
            continue

        match = re.match(r"^(\d+)\s+(\S+)", line)
        if match:
            vlan_id = match.group(1)
            vlan_name = match.group(2)
            vlans.append({"vlan_id": vlan_id, "vlan_name": vlan_name})

    dictionary = {
        "switch_ip": host,
        "switch_name": hostname,
        "vlans": vlans
    }
    
    return dictionary


def parse_show_vlan_id(host: str, hostname: str, vlan_id: int, output: str) -> dict:
    """
    Parses the output of 'show vlan id' into a dict.
    """
    vlan_name = ""
    ports = []
    parsed_output = output.split("\n")

    for line in parsed_output:
        # Skip headers and empty lines
        if not line.strip() or line.startswith("VLAN") or line.startswith("----"):
            continue

        match = re.match(rf"^{vlan_id}\s+(\S+)\s+\S+\s+(.*)", line)
        if match:
            vlan_name = match.group(1)
            ports_str = match.group(2).strip()
            if ports_str:
                ports = [port.strip() for port in ports_str.split(",") if port.strip()]
            break

    dictionary = {
        "switch_ip": host,
        "switch_name": hostname,
        "vlan_id": vlan_id,
        "vlan_name": vlan_name,
        "ports": ports
    }
    
    return dictionary