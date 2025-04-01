from fastapi import APIRouter
from app.services.switch_service import SwitchService

router = APIRouter(prefix="/switches")

@router.get("")
async def get_all_switches():
    return "Here are all the switches"

@router.get("/{switch_ip}/vlans")
async def get_switch_vlans(switch_ip: str):
    username = ""
    password = ""
    return SwitchService.get_all_vlans(switch_ip, username, password)