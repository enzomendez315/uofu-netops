from app.utils.ssh_client import ssh_connect

class SwitchService:

    @staticmethod
    def get_all_vlans(host: str, username: str, password: str):
        try:
            net_connect = ssh_connect(host, username, password)

            if net_connect:
                output = net_connect.send_command("show vlan br")
                return output
            else:
                return f"Authentication failed to host {host}"
            #return f"Here are all the VLANs for switch {host}"
        except Exception as e:
            print(f"Switch service failed to connect to {host}: {e}") 