# Archivo: backend/routes/documentos.py
import os
from flask import Blueprint, request, current_app
from werkzeug.utils import secure_filename

# Definimos el Blueprint (tu módulo)
documentos_bp = Blueprint('documentos', __name__)

# Extensiones permitidas
ALLOWED_EXTENSIONS = {'pdf', 'doc', 'docx'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@documentos_bp.route('/subir-documento', methods=['GET', 'POST'])
def subir_documento():
    if request.method == 'POST':
        if 'archivo' not in request.files:
            return "Error: No se encontró el archivo"
        
        file = request.files['archivo']
        
        if file.filename == '':
            return "Error: No seleccionaste archivo"

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            # Guardamos en la carpeta configurada en app.py
            ruta = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
            file.save(ruta)
            return f"¡Éxito! Archivo guardado en: {ruta}"
        else:
            return "Error: Archivo no válido (Solo PDF/Word)"

    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Subir Documento</title>
    </head>
    <body>
        <h1>Subir Documento</h1>
        <form method="POST" action="/subir-documento" enctype="multipart/form-data">
            <label for="archivo">Selecciona un archivo:</label>
            <input type="file" name="archivo" id="archivo" required>
            <button type="submit">Subir</button>
        </form>
    </body>
    </html>
    '''
