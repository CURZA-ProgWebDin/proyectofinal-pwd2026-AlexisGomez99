from app.controllers.user_routine_controller import UserRoutineController
from flask import request, Blueprint
from flask_jwt_extended import jwt_required
from app.decorators.rol_access import rol_access


user_routines = Blueprint('user_routines', __name__, url_prefix='/user_routines')

@user_routines.route('/')
@jwt_required()
@rol_access(['admin', 'operador'])
def get_all():
    return UserRoutineController.get_all()
@user_routines.route('/<int:id>')
@jwt_required()
@rol_access(['admin', 'operador'])
def show(id):
    return UserRoutineController.show(id)

@user_routines.route("/", methods=['POST'])
@jwt_required()
@rol_access(['admin'])
def create():
    return UserRoutineController.create(request.get_json() or None)

@user_routines.route("/<int:id>", methods=['PUT'])
@jwt_required()
@rol_access(['admin'])
def update(id):
    return  UserRoutineController.update(request=request.get_json() or None, id=id)
    

@user_routines.route("/<int:id>", methods=['DELETE'])
@jwt_required()
@rol_access(['admin'])
def destroy(id):
    return UserRoutineController.destroy( id)
