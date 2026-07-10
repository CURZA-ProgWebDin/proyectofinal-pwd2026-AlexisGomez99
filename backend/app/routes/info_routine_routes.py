from app.controllers.info_routine_controller import InfoRoutineController
from flask import request, Blueprint
from flask_jwt_extended import jwt_required
from app.decorators.rol_access import rol_access


info_routines = Blueprint('info_routines', __name__, url_prefix='/info_routines')

@info_routines.route('/')
@jwt_required()
@rol_access(['admin', 'operador'])
def get_all():
    return InfoRoutineController.get_all()

@info_routines.route('/my_routine/<int:id>')
@jwt_required()
@rol_access(['admin', 'operador'])
def get_my_routine(id):
    return InfoRoutineController.get_me(id)

@info_routines.route('/<int:id>')
@jwt_required()
@rol_access(['admin', 'operador'])
def show(id):
    return InfoRoutineController.show(id)

@info_routines.route("/", methods=['POST'])
@jwt_required()
@rol_access(['admin'])
def create():
    return InfoRoutineController.create(request.get_json() or None)

@info_routines.route("/<int:id>", methods=['PUT'])
@jwt_required()
@rol_access(['admin'])
def update(id):
    return  InfoRoutineController.update(request=request.get_json() or None, id=id)
    

@info_routines.route("/<int:id>", methods=['DELETE'])
@jwt_required()
@rol_access(['admin'])
def destroy(id):
    return InfoRoutineController.destroy( id)
