from app.utils.parse_output import (
    parse_show_interface_status,
    parse_show_vlan_brief, 
    parse_show_vlan_id
)
from app.utils.ssh_client import ssh_connect

class SwitchService:

    @staticmethod
    def get_vlans(host: str, username: str, password: str):
        try:
            net_connect = ssh_connect(host, username, password)
            if net_connect:
                output = net_connect.send_command("show vlan brief")
                hostname_output = net_connect.send_command("show running-config | include hostname")
                hostname = hostname_output.split()[1] if hostname_output.startswith("hostname") else None
                net_connect.disconnect()
                parsed_output = parse_show_vlan_brief(host, hostname, output)
                return parsed_output
            else:
                #return f"Authentication failed to host {host}"
                return {"detail": f"Switch {host} not found"}
        except Exception as e:
            print(f"Switch service failed to get the VLANs on {host}: {e}")

    @staticmethod
    def get_vlan_ports(host: str, username: str, password: str, vlan_id: int):
        try:
            net_connect = ssh_connect(host, username, password)
            if net_connect:
                output = net_connect.send_command(f"show vlan id {vlan_id}")
                hostname_output = net_connect.send_command("show running-config | include hostname")
                hostname = hostname_output.split()[1] if hostname_output.startswith("hostname") else None
                net_connect.disconnect()
                parsed_output = parse_show_vlan_id(host, hostname, vlan_id, output)
                return parsed_output
            else:
                return {"detail": f"Switch {host} not found"}
        except Exception as e:
            print(f"Switch service failed to get the ports on VLAN {vlan_id} on {host}: {e}")

    @staticmethod
    def get_all_ports_status(host: str, username: str, password: str):
        try:
            net_connect = ssh_connect(host, username, password)
            if net_connect:
                output = net_connect.send_command(f"show interface status")
                hostname_output = net_connect.send_command("show running-config | include hostname")
                hostname = hostname_output.split()[1] if hostname_output.startswith("hostname") else None
                net_connect.disconnect()
                parsed_output = parse_show_interface_status(host, hostname, output)
                return parsed_output
            else:
                return {"detail": f"Switch {host} not found"}
        except Exception as e:
            print(f"Switch service failed to get the ports' status on {host}: {e}")

    @staticmethod
    def get_port_config(host: str, username: str, password: str, port: str):
        try:
            net_connect = ssh_connect(host, username, password)
            if net_connect:
                output = net_connect.send_command(f"show run int {port}")
                net_connect.disconnect()
                return output
            else:
                return {"detail": f"Switch {host} not found"}
        except Exception as e:
            print(f"Switch service failed to get the port's ({port}) configuration on {host}: {e}")

    @staticmethod
    def get_port_status(host: str, username: str, password: str, port: str):
        try:
            net_connect = ssh_connect(host, username, password)
            if net_connect:
                output = net_connect.send_command(f"show interface status | i {port}")
                net_connect.disconnect()
                return output
            else:
                return {"detail": f"Switch {host} not found"}
        except Exception as e:
            print(f"Switch service failed to get the port's ({port}) configuration on {host}: {e}")