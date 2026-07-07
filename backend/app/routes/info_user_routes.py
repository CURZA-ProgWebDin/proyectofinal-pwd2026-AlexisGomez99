from app.controllers.info_user_controller import InfoUserController
from flask import request, Blueprint
from flask_jwt_extended import jwt_required
from app.decorators.rol_access import rol_access


info_users = Blueprint('info_users', __name__, url_prefix='/info_users')

@info_users.route('/')
@jwt_required()
@rol_access(['admin', 'operador'])
def get_all():
    return InfoUserController.get_all()
@info_users.route('/<int:id>')
@jwt_required()
@rol_access(['admin', 'operador'])
def show(id):
    return InfoUserController.show(id)

@info_users.route("/", methods=['POST'])
@jwt_required()
@rol_access(['admin'])
def create():
    return InfoUserController.create(request.get_json() or None)

@info_users.route("/<int:id>", methods=['PUT'])
@jwt_required()
@rol_access(['admin'])
def update(id):
    return  InfoUserController.update(request=request.get_json() or None, id=id)
    

@info_users.route("/<int:id>", methods=['DELETE'])
@jwt_required()
@rol_access(['admin'])
def destroy(id):
    return InfoUserController.destroy( id)
