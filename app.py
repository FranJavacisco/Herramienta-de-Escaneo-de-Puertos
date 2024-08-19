from flask import Flask, request, render_template, jsonify
import socket
from colorama import Fore, Style, init

# Inicializa colorama
init()

app = Flask(__name__)

def scan_ports(ip, start_port, end_port):
    open_ports = []
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))
        if result == 0:
            open_ports.append(port)
        sock.close()
    return open_ports

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scan', methods=['POST'])
def scan():
    ip = request.form.get('ip')
    start_port = int(request.form.get('start_port'))
    end_port = int(request.form.get('end_port'))

    if not ip or not start_port or not end_port:
        return jsonify({"error": "Invalid input"}), 400

    print(Fore.CYAN + 'Scanning ports...' + Style.RESET_ALL)  # Mensaje en color cyan
    open_ports = scan_ports(ip, start_port, end_port)
    
    if open_ports:
        print(Fore.GREEN + f'Open ports: {open_ports}' + Style.RESET_ALL)  # Mensaje en color verde
    else:
        print(Fore.RED + 'No open ports found' + Style.RESET_ALL)  # Mensaje en color rojo

    return jsonify({"open_ports": open_ports})

if __name__ == '__main__':
    app.run(debug=True)
