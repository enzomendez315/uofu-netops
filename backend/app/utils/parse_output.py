import re

from typing import Optional


def parse_show_vlan_brief(host: str, hostname: str, output: str) -> dict:
    """
    Parses the output of 'show vlan brief' into a dict.
    """
    vlans = []
    parsed_output = output.splitlines()

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
    parsed_output = output.splitlines()

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


def parse_show_interface_status(
        host: str, 
        hostname: str, 
        output: str, 
        include_port: Optional[str] = None
    ) -> dict:
    """
    Parses the output of 'show interface status' into a dict.
    """
    ports = []
    parsed_output = output.splitlines()

    for line in parsed_output:
        # Skip headers and empty lines
        if not line.strip() or line.startswith("Port"):
            continue

        match = re.match(r"^(\S+)\s+.{0,20}\s+(\S+)\s+(\S+)", line)
        if match:
            port_id = match.group(1)
            status = match.group(2)
            vlan_str = match.group(3)

            try:
                vlan_id = int(vlan_str)
            except ValueError:
                # For things like "trunk", skip them
                continue

            if include_port is None or port_id == include_port:
                ports.append({
                    "port_id": port_id,
                    "vlan_id": vlan_id,
                    "status": status
                })

    dictionary = {
        "switch_ip": host,
        "switch_name": hostname,
        "ports": ports
    }
    
    return dictionary