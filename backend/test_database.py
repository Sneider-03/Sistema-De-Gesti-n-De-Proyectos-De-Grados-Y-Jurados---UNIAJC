from flask import Flask
from config import Config
from database.database import init_db, db
from database.models import Proyecto, Documento

def crear_y_probar_base_datos():
    # Crear aplicación Flask temporal
    app = Flask(__name__)
    app.config.from_object(Config)
    
    print("🚀 Iniciando creación de base de datos...")
    print("📊 Configurando modelos: Proyecto y Documento")
    
    # Inicializar base de datos
    init_db(app)
    
    # Probar la base de datos con datos de ejemplo
    with app.app_context():
        print("\n🧪 Insertando datos de prueba...")
        
        # Crear proyecto 1
        proyecto1 = Proyecto(
            nombre="Sistema de Gestión Académica",
            descripcion="Desarrollo de plataforma para gestión de proyectos de grado"
        )
        db.session.add(proyecto1)
        
        # Crear proyecto 2
        proyecto2 = Proyecto(
            nombre="App Móvil para Biblioteca UNIAJC",
            descripcion="Aplicación móvil para reserva de libros y recursos bibliográficos"
        )
        db.session.add(proyecto2)
        
        db.session.commit()
        print("✅ Proyectos creados exitosamente")
        
        # Crear documentos para proyecto 1
        doc1 = Documento(
            proyecto_id=proyecto1.id,
            nombre_archivo="anteproyecto_sistema_gestion.pdf",
            ruta="/documentos/proyecto1/anteproyecto.pdf"
        )
        db.session.add(doc1)
        
        doc2 = Documento(
            proyecto_id=proyecto1.id,
            nombre_archivo="cronograma_actividades.xlsx",
            ruta="/documentos/proyecto1/cronograma.xlsx"
        )
        db.session.add(doc2)
        
        # Crear documento para proyecto 2
        doc3 = Documento(
            proyecto_id=proyecto2.id,
            nombre_archivo="propuesta_app_biblioteca.docx",
            ruta="/documentos/proyecto2/propuesta.docx"
        )
        db.session.add(doc3)
        
        db.session.commit()
        print("✅ Documentos creados exitosamente")
        
        # Mostrar resultados
        print("\n📊 RESULTADOS DE LA BASE DE DATOS:")
        print("=" * 50)
        
        proyectos = Proyecto.query.all()
        print(f"📁 Total de proyectos: {len(proyectos)}")
        
        for proyecto in proyectos:
            print(f"\n🏆 Proyecto: {proyecto.nombre}")
            print(f"   📝 Descripción: {proyecto.descripcion}")
            print(f"   📅 Fecha: {proyecto.fecha}")
            print(f"   🆔 ID: {proyecto.id}")
            
            documentos = Documento.query.filter_by(proyecto_id=proyecto.id).all()
            print(f"   📎 Documentos asociados: {len(documentos)}")
            
            for doc in documentos:
                print(f"      • {doc.nombre_archivo} -> {doc.ruta}")
        
        print("\n" + "=" * 50)
        print("🎉 Base de datos verificada y funcionando correctamente!")
        print("💾 Archivo: backend/database/uniajc_proyectos.db")

if __name__ == '__main__':
    crear_y_probar_base_datos()