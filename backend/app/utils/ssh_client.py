import netmiko

def ssh_connect(host, username, password):
    """
    Establish SSH connection to a network switch.
    """
    try:
        switch = {
            "device_type": "cisco_ios",
            "host": host,
            "username": username,
            "password": password
        }
        net_connect = netmiko.ConnectHandler(**switch)
        print(f"Successfully connected to {host}")
        return net_connect
    except Exception as e:
        print(f"Failed to connect to {host}: {e}")
        return None
