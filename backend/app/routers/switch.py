from urllib.parse import unquote
from dotenv import load_dotenv
import os

from fastapi import APIRouter
from app.services.switch_service import SwitchService

# FOR TESTING
load_dotenv()
username = os.getenv("MY_USERNAME")
password = os.getenv("MY_PASSWORD")

router = APIRouter(prefix="/switches")

@router.get("")
async def get_switches():
    return "Here are all the switches."

@router.get("/{switch_ip}/vlans")
async def get_switch_vlans(switch_ip: str):
    return SwitchService.get_vlans(switch_ip, username, password)

@router.get("/{switch_ip}/vlans/{vlan_id}")
async def get_switch_vlan_ports(switch_ip: str, vlan_id: int):
    return SwitchService.get_vlan_ports(switch_ip, username, password, vlan_id)

@router.get("/{switch_ip}/ports")
async def get_switch_ports(switch_ip: str):
    return SwitchService.get_all_ports_status(switch_ip, username, password)

@router.get("/{switch_ip}/ports/{port_id}")
async def get_switch_port_config(switch_ip: str, port_id: str):
    port_id = port_id.replace("-", "/")
    return SwitchService.get_port_config(switch_ip, username, password, port_id)

@router.get("/{switch_ip}/ports/{port_id}/status")
async def get_switch_port_status(switch_ip: str, port_id: str):
    port_id = port_id.replace("-", "/")
    return SwitchService.get_port_status(switch_ip, username, password, port_id)