from app.utils.ssh_client import ssh_connect

class SwitchService:

    @staticmethod
    def get_vlans(host: str, username: str, password: str):
        try:
            net_connect = ssh_connect(host, username, password)
            if net_connect:
                output = net_connect.send_command("show vlan br")
                net_connect.disconnect()
                return output
            else:
                return f"Authentication failed to host {host}"
        except Exception as e:
            print(f"Switch service failed to get the VLANs on {host}: {e}")

    @staticmethod
    def get_vlan_ports(host: str, username: str, password: str, vlan_id: int):
        try:
            net_connect = ssh_connect(host, username, password)
            if net_connect:
                output = net_connect.send_command(f"show vlan id {vlan_id}")
                net_connect.disconnect()
                return output
            else:
                return f"Authentication failed to host {host}"
        except Exception as e:
            print(f"Switch service failed to get the ports on VLAN {vlan_id} on {host}: {e}")