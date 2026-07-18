from app.controllers.routine_controller import RoutineController
from flask import request, Blueprint
from flask_jwt_extended import jwt_required
from app.decorators.rol_access import rol_access


routines = Blueprint('routines', __name__, url_prefix='/routines')

@routines.route('/')
@jwt_required()
@rol_access(['admin', 'entrenador','creador','operador'])
def get_all():
    return RoutineController.get_all()
@routines.route('/<int:id>')
@jwt_required()
@rol_access(['admin', 'entrenador','creador','operador'])
def show(id):
    return RoutineController.show(id)

@routines.route('/me/<int:id>')
@jwt_required()
@rol_access(['admin', 'entrenador','creador'])
def showFrom(id):
    return RoutineController.get_my_routines(id)

@routines.route("/", methods=['POST'])
@jwt_required()
@rol_access(['admin', 'entrenador','creador'])
def create():
    return RoutineController.create(request.get_json() or None)

@routines.route("/<int:id>", methods=['PUT'])
@jwt_required()
@rol_access(['admin', 'entrenador','creador'])
def update(id):
    return  RoutineController.update(request=request.get_json() or None, id=id)
    

@routines.route("/<int:id>", methods=['DELETE'])
@jwt_required()
@rol_access(['admin', 'entrenador','creador'])
def destroy(id):
    return RoutineController.destroy( id)
