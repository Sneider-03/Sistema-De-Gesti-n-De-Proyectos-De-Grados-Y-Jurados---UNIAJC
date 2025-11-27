import os
from flask import Flask

# Crear instancia de Flask
app = Flask(__name__)

# Configuración de la carpeta de subidas
UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), 'backend', 'uploads')
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB máximo

# Importar y registrar Blueprints
from backend.routes.documentos import documentos_bp

app.register_blueprint(documentos_bp)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
