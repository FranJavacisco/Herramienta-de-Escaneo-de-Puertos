from flask import Flask

def create_app():
    app = Flask(__name__)
    
    # Importar y registrar las rutas
    from .routes import main
    app.register_blueprint(main)
    
    return app
