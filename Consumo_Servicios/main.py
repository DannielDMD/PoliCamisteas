import datetime
from flask import Flask, jsonify, request, render_template
from models import Base, Usuario
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import NoResultFound

# Configuración de la base de datos
DATABASE_URL = "postgresql://postgres:DmD020827*@localhost:5432/PoliCamisetas2"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

# Inicializar la aplicación Flask
app = Flask(__name__)

# Ruta para cargar la interfaz HTML
@app.route('/usuarios')
def pagina_usuarios():
    return render_template('usuarios.html')  # Renderiza el archivo HTML desde la carpeta templates

# Rutas CRUD para Usuarios
@app.route('/api/usuarios', methods=['GET'])
def obtener_usuarios():
    usuarios = session.query(Usuario).all()
    return jsonify([{"id": u.id, "nombre": u.nombre, "correo": u.correo, "rol": u.rol} for u in usuarios])

@app.route('/api/usuarios/<int:id>', methods=['GET'])
def obtener_usuario(id):
    try:
        usuario = session.query(Usuario).filter_by(id=id).one()
        return jsonify({"id": usuario.id, "nombre": usuario.nombre, "correo": usuario.correo, "rol": usuario.rol})
    except NoResultFound:
        return jsonify({"error": "Usuario no encontrado"}), 404

@app.route('/api/usuarios', methods=['POST'])
def crear_usuario():
    data = request.get_json()
    nuevo_usuario = Usuario(
        nombre=data['nombre'],
        correo=data['correo'],
        contraseña=data['contraseña'],
        rol=data['rol']
    )
    session.add(nuevo_usuario)
    session.commit()
    return jsonify({"mensaje": "Usuario creado"}), 201

@app.route('/api/usuarios/<int:id>', methods=['PUT'])
def actualizar_usuario(id):
    try:
        usuario = session.query(Usuario).filter_by(id=id).one()
        data = request.get_json()
        usuario.nombre = data['nombre']
        usuario.correo = data['correo']
        usuario.rol = data['rol']
        session.commit()
        return jsonify({"mensaje": "Usuario actualizado"})
    except NoResultFound:
        return jsonify({"error": "Usuario no encontrado"}), 404

@app.route('/api/usuarios/<int:id>', methods=['DELETE'])
def eliminar_usuario(id):
    try:
        usuario = session.query(Usuario).filter_by(id=id).one()
        session.delete(usuario)
        session.commit()
        return jsonify({"mensaje": "Usuario eliminado"})
    except NoResultFound:
        return jsonify({"error": "Usuario no encontrado"}), 404

if __name__ == '__main__':
    Base.metadata.create_all(engine)
    app.run(debug=True)
