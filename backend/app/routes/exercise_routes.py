from app.controllers.exercise_controller import ExerciseController
from flask import request, Blueprint
from flask_jwt_extended import jwt_required
from app.decorators.rol_access import rol_access


exercises = Blueprint('exercises', __name__, url_prefix='/exercises')

@exercises.route('/')
@jwt_required()
@rol_access(['admin', 'creador','entrenador','operador'])
def get_all():
    return ExerciseController.get_all()
@exercises.route('/<int:id>')
@jwt_required()
@rol_access(['admin', 'creador','entrenador','operador'])
def show(id):
    return ExerciseController.show(id)

@exercises.route("/", methods=['POST'])
@jwt_required()
@rol_access(['admin', 'creador','entrenador'])
def create():
    return ExerciseController.create(request.get_json() or None)

@exercises.route("/<int:id>", methods=['PUT'])
@jwt_required()
@rol_access(['admin', 'creador','entrenador'])
def update(id):
    return  ExerciseController.update(request=request.get_json() or None, id=id)
    

@exercises.route("/<int:id>", methods=['DELETE'])
@jwt_required()
@rol_access(['admin', 'creador','entrenador'])
def destroy(id):
    return ExerciseController.destroy( id)
