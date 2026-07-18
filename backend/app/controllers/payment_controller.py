from typing import Literal
from sqlalchemy.exc import IntegrityError
from app.models.payment import Payment
from datetime import datetime
from app.models import db
from flask import Response, jsonify
from app.controllers import Controller

class PaymentController (Controller):
    
    @staticmethod
    def get_all() -> tuple[Response, int]:
        payments_list = db.session.execute(db.select(Payment).order_by(db.desc(Payment.id))).scalars().all()
        if len(payments_list) > 0:
            payments_to_dict = [payment.to_dict() for payment in payments_list ]
            return jsonify(payments_to_dict), 200 
        return jsonify({"message": 'datos no encontrados'}), 404
    
    @staticmethod
    def show(id)->tuple[Response, int]:
        payment = db.session.get(Payment, id)
        if payment:
            return jsonify(payment.to_dict()), 200
        return jsonify({"message": 'pago no encontrado'}), 404
    
    @staticmethod
    def create(request:dict) -> tuple[Response, int]:
        amount= request.get('amount')
        description= request.get('description')
        service= request.get('service')
        user_id = request.get('user_id')
        error :str | None = None
        if amount is None:
            error = 'El monto es requerido'
        if description is None:
            error = 'La descripcion es requerida'
        if service is None:
            error = 'El servicio es requerido'
        if user_id is None:
            error = 'El user_id es requerido'
            
        if error is None:
            try:
                payment = Payment(amount=amount, description=description, service=service, user_id=user_id)
                db.session.add(payment)
                db.session.commit()
                return jsonify({'message': "pago creado con exito"}), 201
            except IntegrityError:
                db.session.rollback()
                return jsonify({'message': "Pago ya registrado"}), 409
        return jsonify ({'message': error}), 422
        
        
    @staticmethod
    def update(request, id)->tuple[Response, int]:
        amount= request.get('amount')
        description= request.get('description')
        service= request.get('service')
        user_id = request.get('user_id')
        error :str | None = None
        if amount is None:
            error = 'El monto es requerido'
        if description is None:
            error = 'La descripcion es requerida'
        if service is None:
            error = 'El servicio es requerido'
        if user_id is None:
            error = 'El user_id es requerido'
            
        if error is None:
            payment = db.session.get(Payment, id)
            if payment:
                try:
                    payment.amount = amount
                    payment.description = description
                    payment.service = service
                    payment.user_id = user_id
                    payment.updated_at = datetime.now()
                    db.session.commit()
                    return jsonify({'message':'pago modificado con exito'}), 200
                except IntegrityError:
                    error = 'se necesitan todos los datos correctos' 
                    return jsonify({'message':error}), 409
            else:     
                error = 'pago no encontrado'
            
        return jsonify({'message':error}), 404
        
    @staticmethod
    def destroy(id) -> tuple[Response, int]:
        payment = db.session.get(Payment, id)
        error = None
        if payment:
            db.session.delete(payment)
            db.session.commit()
            return jsonify({'message':'el pago fue eliminado con exito'}), 200
        else:
            error = 'pago no encontrado'
        return jsonify({'message':error}), 404