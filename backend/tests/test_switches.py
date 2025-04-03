from fastapi.testclient import TestClient
from unittest.mock import patch
from app.main import app

client = TestClient(app)

@patch("app.services.switch_service.SwitchService.get_vlans")
def test_get_switch_vlans_success(mock_get_vlan_ports):
    """Test fetching VLANs of a switch"""
    mock_get_vlan_ports.return_value = {
        "switch_ip": "192.168.1.1",
        "vlans": [
            {
                "vlan_id": 10,
                "name": "Data"
            },
            {
                "vlan_id": 20,
                "name": "Voice"
            }
        ]
    }
    
    response = client.get("/api/v1/switches/192.168.1.1/vlans")

    assert response.status_code == 200
    assert response.json() == {
        "switch_ip": "192.168.1.1",
        "vlans": [
            {
                "vlan_id": 10,
                "name": "Data"
            },
            {
                "vlan_id": 20,
                "name": "Voice"
            }
        ]
    }


@patch("app.services.switch_service.SwitchService.get_vlans")
def test_get_switch_vlans_invalid_ip(mock_get_vlan_ports):
    """Test fetching VLANs for a non-existent switch IP"""
    mock_get_vlan_ports.side_effect = Exception("Switch not found")

    response = client.get("/api/v1/switches/192.168.99.99/vlans")

    assert response.status_code == 404
    assert response.json() == {"detail": "Switch not found"}



@patch("app.services.switch_service.SwitchService.get_vlans")
def test_get_switch_vlans_no_vlans(mock_get_vlan_ports):
    """Test fetching VLANs when no VLANs exist on the switch"""
    mock_get_vlan_ports.return_value = {
        "switch_ip": "192.168.1.1",
        "vlans": []
    }
    
    response = client.get("/api/v1/switches/192.168.1.1/vlans")

    assert response.status_code == 200
    assert response.json() == {
        "switch_ip": "192.168.1.1",
        "vlans": []
    }