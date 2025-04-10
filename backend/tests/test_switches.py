from fastapi.testclient import TestClient
from unittest.mock import patch
from app.main import app

client = TestClient(app)

@patch("app.services.switch_service.SwitchService.get_vlans")
def test_get_switch_vlans_success(mock_get_vlans):
    """Test fetching VLANs of a switch"""
    mock_get_vlans.return_value = {
        "switch_ip": "192.168.1.1",
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
    
    response = client.get("/api/v1/switches/192.168.1.1/vlans")

    assert response.status_code == 200
    assert response.json() == {
        "switch_ip": "192.168.1.1",
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


@patch("app.services.switch_service.SwitchService.get_vlans")
def test_get_switch_vlans_invalid_ip(mock_get_vlans):
    """Test fetching VLANs for a non-existent switch IP"""
    mock_get_vlans.side_effect = Exception("Switch not found")

    response = client.get("/api/v1/switches/192.168.99.99/vlans")

    assert response.status_code == 404
    assert response.json() == {"detail": "Switch 192.168.99.99 not found"}


@patch("app.services.switch_service.SwitchService.get_vlans")
def test_get_switch_vlans_no_vlans(mock_get_vlans):
    """Test fetching VLANs when no VLANs exist on the switch"""
    mock_get_vlans.return_value = {
        "switch_ip": "192.168.1.1",
        "vlans": []
    }
    
    response = client.get("/api/v1/switches/192.168.1.1/vlans")

    assert response.status_code == 200
    assert response.json() == {
        "switch_ip": "192.168.1.1",
        "vlans": []
    }


@patch("app.services.switch_service.SwitchService.get_vlan_ports")
def test_get_switch_vlan_ports_success(mock_get_vlan_ports):
    """Test fetching VLAN ports of a switch"""
    mock_get_vlan_ports.return_value = {
        "switch_ip": "192.168.1.1",
        "vlan_id": 10,
        "vlan_name": "Data",
        "ports": ["Gi0/1", "Gi0/2", "Gi0/3"]
    }
    
    response = client.get("/api/v1/switches/192.168.1.1/vlans/10")

    assert response.status_code == 200
    assert response.json() == {
        "switch_ip": "192.168.1.1",
        "vlan_id": 10,
        "vlan_name": "Data",
        "ports": ["Gi0/1", "Gi0/2", "Gi0/3"]
    }


@patch("app.services.switch_service.SwitchService.get_vlan_ports")
def test_get_switch_vlan_ports_invalid_ip(mock_get_vlan_ports):
    """Test fetching VLAN ports for a non-existent switch IP"""
    mock_get_vlan_ports.side_effect = Exception("Switch not found")

    response = client.get("/api/v1/switches/192.168.99.99/vlans/10")

    assert response.status_code == 404
    assert response.json() == {"detail": "Switch not found"}


@patch("app.services.switch_service.SwitchService.get_vlan_ports")
def test_get_switch_vlan_ports_no_ports(mock_get_vlan_ports):
    """Test fetching VLAN ports when none are on the VLAN"""
    mock_get_vlan_ports.return_value = {
        "switch_ip": "192.168.1.1",
        "vlan_id": 10,
        "vlan_name": "Data",
        "ports": []
    }
    
    response = client.get("/api/v1/switches/192.168.1.1/vlans/10")

    assert response.status_code == 200
    assert response.json() == {
        "switch_ip": "192.168.1.1",
        "vlan_id": 10,
        "vlan_name": "Data",
        "ports": []
    }


@patch("app.services.switch_service.SwitchService.get_vlan_ports")
def test_get_switch_vlan_ports_invalid_vlan(mock_get_vlan_ports):
    """Test fetching VLAN ports for a non-existing VLAN"""
    mock_get_vlan_ports.side_effect = Exception("VLAN not found")
    
    response = client.get("/api/v1/switches/192.168.1.1/vlans/10")

    assert response.status_code == 404
    assert response.json() == {"detail": "VLAN 10 not found on switch 192.168.1.1"}