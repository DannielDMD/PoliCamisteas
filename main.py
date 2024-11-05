import datetime
from flask import Flask, jsonify, request
from models import Base, Usuario, Camiseta, Estampa, Pedido
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

# Rutas para Usuarios
@app.route('/usuarios', methods=['GET'])
def obtener_usuarios():
    usuarios = session.query(Usuario).all()
    return jsonify([{"id": u.id, "nombre": u.nombre, "correo": u.correo, "rol": u.rol} for u in usuarios])

@app.route('/usuarios/<int:id>', methods=['GET'])
def obtener_usuario(id):
    try:
        usuario = session.query(Usuario).filter_by(id=id).one()
        return jsonify({"id": usuario.id, "nombre": usuario.nombre, "correo": usuario.correo, "rol": usuario.rol})
    except NoResultFound:
        return jsonify({"error": "Usuario no encontrado"}), 404

@app.route('/usuarios', methods=['POST'])
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

@app.route('/usuarios/<int:id>', methods=['PUT'])
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

@app.route('/usuarios/<int:id>', methods=['DELETE'])
def eliminar_usuario(id):
    try:
        usuario = session.query(Usuario).filter_by(id=id).one()
        session.delete(usuario)
        session.commit()
        return jsonify({"mensaje": "Usuario eliminado"})
    except NoResultFound:
        return jsonify({"error": "Usuario no encontrado"}), 404

# Rutas para Camisetas
@app.route('/camisetas', methods=['GET'])
def obtener_camisetas():
    camisetas = session.query(Camiseta).all()
    return jsonify([{"id": c.id, "tipo": c.tipo, "talla": c.talla, "material": c.material, "precio": float(c.precio), "stock": c.stock} for c in camisetas])

@app.route('/camisetas/<int:id>', methods=['GET'])
def obtener_camiseta(id):
    try:
        camiseta = session.query(Camiseta).filter_by(id=id).one()
        return jsonify({
            "id": camiseta.id,
            "tipo": camiseta.tipo,
            "talla": camiseta.talla,
            "material": camiseta.material,
            "precio": float(camiseta.precio),
            "stock": camiseta.stock
        })
    except NoResultFound:
        return jsonify({"error": "Camiseta no encontrada"}), 404

@app.route('/camisetas', methods=['POST'])
def crear_camiseta():
    data = request.get_json()
    nueva_camiseta = Camiseta(
        tipo=data['tipo'],
        talla=data['talla'],
        material=data['material'],
        precio=data['precio'],
        stock=data['stock']
    )
    session.add(nueva_camiseta)
    session.commit()
    return jsonify({"mensaje": "Camiseta creada"}), 201

@app.route('/camisetas/<int:id>', methods=['PUT'])
def actualizar_camiseta(id):
    try:
        camiseta = session.query(Camiseta).filter_by(id=id).one()
        data = request.get_json()
        camiseta.tipo = data['tipo']
        camiseta.talla = data['talla']
        camiseta.material = data['material']
        camiseta.precio = data['precio']
        camiseta.stock = data['stock']
        session.commit()
        return jsonify({"mensaje": "Camiseta actualizada"})
    except NoResultFound:
        return jsonify({"error": "Camiseta no encontrada"}), 404

@app.route('/camisetas/<int:id>', methods=['DELETE'])
def eliminar_camiseta(id):
    try:
        camiseta = session.query(Camiseta).filter_by(id=id).one()
        session.delete(camiseta)
        session.commit()
        return jsonify({"mensaje": "Camiseta eliminada"})
    except NoResultFound:
        return jsonify({"error": "Camiseta no encontrada"}), 404

# Rutas para Estampas
@app.route('/estampas', methods=['GET'])
def obtener_estampas():
    estampas = session.query(Estampa).all()
    return jsonify([{"id": e.id, "nombre": e.nombre, "artista": e.artista, "precio": float(e.precio), "stock": e.stock} for e in estampas])

@app.route('/estampas/<int:id>', methods=['GET'])
def obtener_estampa(id):
    try:
        estampa = session.query(Estampa).filter_by(id=id).one()
        return jsonify({
            "id": estampa.id,
            "nombre": estampa.nombre,
            "artista": estampa.artista,
            "precio": float(estampa.precio),
            "stock": estampa.stock
        })
    except NoResultFound:
        return jsonify({"error": "Estampa no encontrada"}), 404

@app.route('/estampas', methods=['POST'])
def crear_estampa():
    data = request.get_json()
    nueva_estampa = Estampa(
        nombre=data['nombre'],
        artista=data['artista'],
        precio=data['precio'],
        stock=data['stock']
    )
    session.add(nueva_estampa)
    session.commit()
    return jsonify({"mensaje": "Estampa creada"}), 201

@app.route('/estampas/<int:id>', methods=['PUT'])
def actualizar_estampa(id):
    try:
        estampa = session.query(Estampa).filter_by(id=id).one()
        data = request.get_json()
        estampa.nombre = data['nombre']
        estampa.artista = data['artista']
        estampa.precio = data['precio']
        estampa.stock = data['stock']
        session.commit()
        return jsonify({"mensaje": "Estampa actualizada"})
    except NoResultFound:
        return jsonify({"error": "Estampa no encontrada"}), 404

@app.route('/estampas/<int:id>', methods=['DELETE'])
def eliminar_estampa(id):
    try:
        estampa = session.query(Estampa).filter_by(id=id).one()
        session.delete(estampa)
        session.commit()
        return jsonify({"mensaje": "Estampa eliminada"})
    except NoResultFound:
        return jsonify({"error": "Estampa no encontrada"}), 404

# Rutas para Pedidos
@app.route('/pedidos', methods=['GET'])
def obtener_pedidos():
    pedidos = session.query(Pedido).all()
    return jsonify([{
        "id": p.id,
        "usuario_id": p.usuario_id,
        "fecha_pedido": p.fecha_pedido,
        "total": float(p.total),
        "estado": p.estado
    } for p in pedidos])

@app.route('/pedidos/<int:id>', methods=['GET'])
def obtener_pedido(id):
    try:
        pedido = session.query(Pedido).filter_by(id=id).one()
        return jsonify({
            "id": pedido.id,
            "usuario_id": pedido.usuario_id,
            "fecha_pedido": pedido.fecha_pedido,
            "total": float(pedido.total),
            "estado": pedido.estado
        })
    except NoResultFound:
        return jsonify({"error": "Pedido no encontrado"}), 404

@app.route('/pedidos', methods=['POST'])
def crear_pedido():
    data = request.get_json()
    nuevo_pedido = Pedido(
        usuario_id=data['usuario_id'],
        total=data['total'],
        estado=data['estado']
    )
    try:
        session.add(nuevo_pedido)
        session.commit()
        return jsonify({"mensaje": "Pedido creado"}), 201
    except Exception as e:
        session.rollback()  # Hacer rollback en caso de error
        return jsonify({"error": str(e)}), 400

@app.route('/pedidos/<int:id>', methods=['PUT'])
def actualizar_pedido(id):
    try:
        pedido = session.query(Pedido).filter_by(id=id).one()
        data = request.get_json()
        pedido.total = data['total']
        pedido.estado = data['estado']
        session.commit()
        return jsonify({"mensaje": "Pedido actualizado"})
    except NoResultFound:
        return jsonify({"error": "Pedido no encontrado"}), 404

@app.route('/pedidos/<int:id>', methods=['DELETE'])
def eliminar_pedido(id):
    try:
        pedido = session.query(Pedido).filter_by(id=id).one()
        session.delete(pedido)
        session.commit()
        return jsonify({"mensaje": "Pedido eliminado"})
    except NoResultFound:
        return jsonify({"error": "Pedido no encontrado"}), 404


if __name__ == '__main__':
    Base.metadata.create_all(engine)
    app.run(debug=True)
