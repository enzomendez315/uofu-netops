import re

def parse_show_vlan_brief(host: str, output: str) -> dict:
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

    dictionary = {"switch_ip": host,
                  "vlans": vlans}
    
    return dictionary

def parse_show_vlan_id():
    pass