from fastapi import APIRouter

from app.core.config import settings
from app.service.switch_service import SwitchService

# FOR TESTING
username = settings.FIRST_SUPERUSER_UID
password = settings.FIRST_SUPERUSER_PASSWORD

router = APIRouter(prefix="/switches", tags=["switches"])

@router.get("/")
async def get_switches():
    """
    Retrieve all switches from the database.

    ### Returns:
    - **dict**: A JSON object containing:
        - `switches` **(list[dict])**: A list of switches, where each switch object includes:
            - `switch_ip` **(str)**: The IP address of the switch.
            - `switch_name` **(str)**: The hostname of the switch.

    ### Example Response:
    ```json
    {
        "switches": [
            {
                "switch_ip": "192.168.1.1",
                "switch_name": "Switch-1"
            },
            {
                "switch_ip": "192.168.1.2",
                "switch_name": "Switch-2"
            }
        ]
    }
    ```
    """
    return "Here are all the switches."

@router.get("/{switch_ip}/vlans")
async def get_switch_vlans(switch_ip: str):
    """
    Retrieve all VLANs associated with a specific switch.

    ### Parameters:
    - `switch_ip` **(str)**: The IP address of the switch.

    ### Returns:
    - **dict**: A JSON object containing:
        - `switch_ip` **(str)**: The IP address of the switch.
        - `switch_name` **(str)**: The hostname of the switch.
        - `vlans` **(list[dict])**: A list of VLANs, where each VLAN object includes:
            - `vlan_id` **(int)**: The VLAN ID.
            - `vlan_name` **(str)**: The VLAN name.

    ### Example Response:
    ```json
    {
        "switch_ip": "192.168.1.1",
        "switch_name": "Switch-1",
        "vlans": [
            {
                "vlan_id": 10,
                "vlan_name": "Data"
            },
            {
                "vlan_id": 20,
                "vlan_name": "Voice"
            }
        ]
    }
    ```
    """
    return SwitchService.get_vlans(switch_ip, username, password)

@router.get("/{switch_ip}/vlans/{vlan_id}")
async def get_switch_vlan_ports(switch_ip: str, vlan_id: int):
    """
    Get all the ports on a specific VLAN.

    ### Parameters:
    - `switch_ip` **(str)**: The IP address of the switch.
    - `vlan_id` **(int)**: The VLAN ID to fetch port details for.

    ### Returns:
    - **dict**: A JSON object containing:
        - `switch_ip` **(str)**: The IP address of the switch.
        - `switch_name` **(str)**: The hostname of the switch.
        - `vlan_id` **(int)**: The requested VLAN ID.
        - `vlan_name` **(str)**: The VLAN name.
        - `ports` **(list[str])**: A list of ports assigned to the VLAN.

    ### Example Response:
    ```json
    {
        "switch_ip": "192.168.1.1",
        "switch_name": "Switch-1",
        "vlan_id": 10,
        "vlan_name": "Data",
        "ports": ["Gi0/1", "Gi0/2", "Gi0/3"]
    }
    ```
    """
    return SwitchService.get_vlan_ports(switch_ip, username, password, vlan_id)

@router.get("/{switch_ip}/ports")
async def get_switch_ports(switch_ip: str):
    """
    Retrieve the status of all ports on a specific switch.

    ### Parameters:
    - `switch_ip` **(str)**: The IP address of the switch.

    ### Returns:
    - **dict**: A JSON object containing:
        - `switch_ip` **(str)**: The IP address of the switch.
        - `switch_name` **(str)**: The hostname of the switch.
        - `ports` **(list[dict])**: A list of ports, where each port object includes:
            - `port_id` **(str)**: The port identifier (e.g., "Gi0/1").
            - `vlan_id` **(int)**: The VLAN assigned to the port (if applicable).
            - `status` **(str)**: The operational status of the port (e.g., "connected", "notconnect").

    ### Example Response:
    ```json
    {
        "switch_ip": "192.168.1.1",
        "switch_name": "Switch-1",
        "ports": [
            {
                "port_id": "Gi0/1",
                "vlan_id": 10,
                "status": "connected"
            },
            {
                "port_id": "Gi0/2",
                "vlan_id": 15,
                "status": "notconnect"
            }
        ]
    }
    ```
    """
    return SwitchService.get_all_ports_status(switch_ip, username, password)

@router.get("/{switch_ip}/ports/{port_id}")
async def get_switch_port_config(switch_ip: str, port_id: str):
    """
    Retrieve the configuration details of a specific port on a switch.

    ### Parameters:
    - `switch_ip` **(str)**: The IP address of the switch.
    - `port_id` **(str)**: The port identifier (formatted as "Gi0-1", converted to "Gi0/1").

    ### Returns:
    - **dict**: A JSON object containing:
        - `switch_ip` **(str)**: The IP address of the switch.
        - `switch_name` **(str)**: The hostname of the switch.
        - `port_id` **(str)**: The requested port ID.
        - `mode` **(str)**: The port mode (e.g., "access", "trunk").
        - `vlan_id` **(int, optional)**: The VLAN assigned to the port (if applicable).
        - `status` **(str)**: The administrative status of the port.

    ### Example Response:
    ```json
    {
        "switch_ip": "192.168.1.1",
        "switch_name": "Switch-1",
        "port_id": "Gi0/1",
        "mode": "access",
        "vlan_id": 10,
        "status": "up"
    }
    ```
    """
    port_id = port_id.replace("-", "/")
    return SwitchService.get_port_config(switch_ip, username, password, port_id)

@router.get("/{switch_ip}/ports/{port_id}/status")
async def get_switch_port_status(switch_ip: str, port_id: str):
    """
    Retrieve the operational status of a specific port on a switch.

    ### Parameters:
    - `switch_ip` **(str)**: The IP address of the switch.
    - `port_id` **(str)**: The port identifier (formatted as "Gi0-1", converted to "Gi0/1").

    ### Returns:
    - **dict**: A JSON object containing:
        - `switch_ip` **(str)**: The IP address of the switch.
        - `switch_name` **(str)**: The hostname of the switch.
        - `port_id` **(str)**: The requested port ID.
        - `status` **(str)**: The current operational status of the port (e.g., "up", "down").
        - `last_change` **(str, optional)**: The timestamp of the last status change.

    ### Example Response:
    ```json
    {
        "switch_ip": "192.168.1.1",
        "switch_name": "Switch-1",
        "port_id": "Gi0/1",
        "status": "up",
        "last_change": "2025-04-01T12:30:00Z"
    }
    ```
    """
    port_id = port_id.replace("-", "/")
    return SwitchService.get_port_status(switch_ip, username, password, port_id)