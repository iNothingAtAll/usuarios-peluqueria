from flask import jsonify, request, current_app
from functools import wraps

from app.models import *

# Genera todas las rutas al llamar la funcion
def register_routes(app):


    # Define el listado de rutas que pueden accederse sin la api key
    RUTAS_PUBLICAS  = ['/login']


    # Define que por defecto todas las rutas requiera api key
    @app.before_request
    def verificar_api_key():
        if request.path in RUTAS_PUBLICAS:
            return  # No requiere autenticación

        api_key = request.headers.get('X-API-KEY')
        expected_key = current_app.config.get('API_KEY_ACCESS')

        if not api_key or api_key != expected_key:
            return jsonify({"error": "API Key invalida"}), 401


    # Devuelte todos los usuarios
    @app.route('/api/historial/usuarios', methods=['GET'])
    def listar_usuarios():
        usuarios = Usuario.query.all()
        return jsonify([usuario.to_dict() for usuario in usuarios]), 200


    # Devuelte todos los usuarios por id
    @app.route('/api/historial/usuarios/<int:usuario_id>', methods=['GET'])
    def obtener_usuario(usuario_id):
        usuario = Usuario.query.get_or_404(usuario_id)
        return jsonify(usuario.to_dict()), 200


    # Devuelte todos las citas
    @app.route('/api/historial/citas', methods=['GET'])
    def listar_citas():
        citas = Cita.query.all()
        return jsonify([cita.to_dict() for cita in citas]), 200
