import socket
from colorama import Fore, Style, init

init(autoreset=True)

def scan_ports(host, start_port, end_port):
    open_ports = []
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Tiempo de espera de 1 segundo
        result = sock.connect_ex((host, port))
        if result == 0:
            open_ports.append(port)
        sock.close()
    return open_ports

def print_results(host, open_ports):
    print(f"{Fore.GREEN}Escaneo completado para {host}:")
    if open_ports:
        for port in open_ports:
            print(f"{Fore.YELLOW}Puerto {port} está abierto.")
    else:
        print(f"{Fore.RED}No se encontraron puertos abiertos.")

if __name__ == "__main__":
    host = input("Introduce la dirección IP o nombre de dominio: ")
    start_port = int(input("Introduce el puerto de inicio: "))
    end_port = int(input("Introduce el puerto de fin: "))
    
    print(f"{Fore.CYAN}Iniciando el escaneo en {host}...")
    open_ports = scan_ports(host, start_port, end_port)
    print_results(host, open_ports)
