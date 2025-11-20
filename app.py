from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Sistema de Gestión de Proyectos - Funciona!"

if __name__ == '__main__':
    app.run(debug=True)