from app.controllers.info_user_controller import InfoUserController
from flask import request, Blueprint
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.decorators.rol_access import rol_access


info_users = Blueprint('info_users', __name__, url_prefix='/info_users')

@info_users.route('/')
@jwt_required()
@rol_access(['admin', 'operador','entrenador','creador'])
def get_all():
    return InfoUserController.get_all()

@info_users.route('/<int:id>')
@jwt_required()
@rol_access(['admin', 'operador','entrenador','creador'])
def show(id):
    return InfoUserController.show(id)

@info_users.route('/me',methods=['GET'])
@jwt_required()
@rol_access(['admin', 'operador','entrenador','creador'])
def me():
    user_id = get_jwt_identity()
    return InfoUserController.get_me(user_id)

@info_users.route("/", methods=['POST'])
@jwt_required()
@rol_access(['admin', 'operador','entrenador','creador'])
def create():
    return InfoUserController.create(request.get_json() or None)

@info_users.route("/<int:id>", methods=['PUT'])
@jwt_required()
@rol_access(['admin', 'operador','entrenador','creador'])
def update(id):
    return  InfoUserController.update(request=request.get_json() or None, id=id)
    

@info_users.route("/<int:id>", methods=['DELETE'])
@jwt_required()
@rol_access(['admin', 'operador','entrenador','creador'])
def destroy(id):
    return InfoUserController.destroy( id)
