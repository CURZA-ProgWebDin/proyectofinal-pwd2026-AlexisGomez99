from app.controllers.payment_controller import PaymentController
from flask import request, Blueprint
from flask_jwt_extended import jwt_required
from app.decorators.rol_access import rol_access


payments = Blueprint('payments', __name__, url_prefix='/payments')

@payments.route('/')
@jwt_required()
@rol_access(['admin', 'operador'])
def get_all():
    return PaymentController.get_all()
@payments.route('/<int:id>')
@jwt_required()
@rol_access(['admin', 'operador'])
def show(id):
    return PaymentController.show(id)

@payments.route("/", methods=['POST'])
@jwt_required()
@rol_access(['admin'])
def create():
    return PaymentController.create(request.get_json() or None)

@payments.route("/<int:id>", methods=['PUT'])
@jwt_required()
@rol_access(['admin'])
def update(id):
    return  PaymentController.update(request=request.get_json() or None, id=id)
    

@payments.route("/<int:id>", methods=['DELETE'])
@jwt_required()
@rol_access(['admin'])
def destroy(id):
    return InfoUserController.destroy( id)
