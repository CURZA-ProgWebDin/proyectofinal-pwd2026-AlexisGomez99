from typing import Literal
from sqlalchemy.exc import IntegrityError
from app.models.info_user import InfoUser
from datetime import datetime
from app.models import db
from flask import Response, jsonify
from app.controllers import Controller

class InfoUserController (Controller):
    
    @staticmethod
    def get_all() -> tuple[Response, int]:
        info_users_list = db.session.execute(db.select(InfoUser).order_by(db.desc(InfoUser.id))).scalars().all()
        if len(info_users_list) > 0:
            info_users_to_dict = [info_user.to_dict() for info_user in info_users_list ]
            return jsonify(info_users_to_dict), 200 
        return jsonify({"message": 'datos no encontrados'}), 404
    
    @staticmethod
    def show(id)->tuple[Response, int]:
        infouser = db.session.get(InfoUser, id)
        if infouser:
            return jsonify(infouser.to_dict()), 200
        return jsonify({"message": 'informacion no encontrada'}), 404
    
    @staticmethod
    def get_me(id) -> tuple[Response, int]:
        query = db.select(InfoUser).filter_by(user_id=id).order_by(db.desc(InfoUser.id))
        info_user = db.session.execute(query).scalar_one_or_none()
        
        if info_user:
            return jsonify(info_user.to_dict()), 200 
            
        return jsonify({"message": 'datos no encontrados'}), 404
    
    
    @staticmethod
    def create(request:dict) -> tuple[Response, int]:
        dni= request.get('dni')
        name= request.get('name')
        last_name= request.get('last_name')
        number_phone = request.get('number_phone')
        adress = request.get('adress')
        user_id = request.get('user_id')
        error :str | None = None
        if dni is None:
            error = 'El dni es requerido'
        if name is None:
            error = 'El nombre es requerido'
        if last_name is None:
            error = 'El apellido es requerido'
        if number_phone is None:
            error = 'El numero es requerido'
        if adress is None:
            error = 'La direccion es requerida'
        if user_id is None:
            error = 'El user_id es requerido'
            
        if error is None:
            try:
                info_user = InfoUser(dni=dni, name=name, last_name=last_name, number_phone=number_phone, adress=adress, user_id=user_id)
                db.session.add(info_user)
                db.session.commit()
                return jsonify({'message': "usuario creado con exito"}), 201
            except IntegrityError:
                db.session.rollback()
                return jsonify({'message': "usuario ya registrado"}), 409
        return jsonify ({'message': error}), 422
        
        
    @staticmethod
    def update(request, id)->tuple[Response, int]:
        dni= request.get('dni')
        name= request.get('name')
        last_name= request.get('last_name')
        number_phone = request.get('number_phone')
        adress = request.get('adress')
        user_id = request.get('user_id')
        error :str | None = None
        if dni is None:
            error = 'El dni es requerido'
        if name is None:
            error = 'El nombre es requerido'
        if last_name is None:
            error = 'El apellido es requerido'
        if number_phone is None:
            error = 'El numero es requerido'
        if adress is None:
            error = 'La direccion es requerida'
            
        if error is None:
            info_user = db.session.get(InfoUser, id)
            if info_user:
                try:
                    info_user.dni = dni
                    info_user.name = name
                    info_user.last_name = last_name
                    info_user.number_phone = number_phone
                    info_user.adress = adress
                    info_user.updated_at = datetime.now()
                    
                    db.session.commit()
                    return jsonify({'message':'usuario modificado con exito'}), 200
                except IntegrityError:
                    error = 'se necesitan todos los datos correctos' 
                    return jsonify({'message':error}), 409
            else:     
                error = 'pago no encontrado'
            
        return jsonify({'message':error}), 404
        
    @staticmethod
    def destroy(id) -> tuple[Response, int]:
        info_user = db.session.get(InfoUser, id)
        error = None
        if info_user:
            db.session.delete(info_user)
            db.session.commit()
            return jsonify({'message':'el usuario fue eliminado con exito'}), 200
        else:
            error = 'usuario no encontrado'
        return jsonify({'message':error}), 404