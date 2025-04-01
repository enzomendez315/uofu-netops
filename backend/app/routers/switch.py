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