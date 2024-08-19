import pytest
from app.scanner import scan_ports

def test_scan_ports():
    # Ejemplo de IP y puertos que debes ajustar para tus pruebas
    ip = '127.0.0.1'
    start_port = 80
    end_port = 82
    
    open_ports = scan_ports(ip, start_port, end_port)
    
    # Ajusta los puertos esperados según la configuración de tu entorno
    assert 80 in open_ports
    assert 81 not in open_ports  # Si el puerto 81 no está abierto
    assert 82 in open_ports
