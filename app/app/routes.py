from flask import Blueprint, request, render_template, jsonify
from .scanner import scan_ports

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/scan', methods=['POST'])
def scan():
    try:
        ip = request.form.get('ip')
        start_port = int(request.form.get('start_port'))
        end_port = int(request.form.get('end_port'))
        
        if not ip or not start_port or not end_port:
            return jsonify({"error": "Invalid input"}), 400
        
        open_ports = scan_ports(ip, start_port, end_port)
        
        return jsonify({"open_ports": open_ports})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500
