from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_db(app):
    db.init_app(app)
    with app.app_context():
        db.create_all()
        print("✅ Base de datos SQLite creada exitosamente!")
        print("📁 Ubicación: backend/database/uniajc_proyectos.db")
    return db