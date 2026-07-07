from typing import Literal
from sqlalchemy.exc import IntegrityError
from app.models.user_routine import UserRoutine
from datetime import datetime
from app.models import db
from flask import Response, jsonify
from app.controllers import Controller

class UserRoutineController (Controller):
    
    @staticmethod
    def get_all() -> tuple[Response, int]:
        user_routines_list = db.session.execute(db.select(UserRoutine).order_by(db.desc(UserRoutine.id))).scalars().all()
        if len(user_routines_list) > 0:
            user_routines_to_dict = [routine.to_dict() for routine in user_routines_list ]
            return jsonify(user_routines_to_dict), 200 
        return jsonify({"message": 'datos no encontrados'}), 404
    
    @staticmethod
    def show(id)->tuple[Response, int]:
        user_routine = db.session.get(UserRoutine, id)
        if user_routine:
            return jsonify(user_routine.to_dict()), 200
        return jsonify({"message": 'rutina de usuario no encontrada'}), 404
    
    @staticmethod
    def create(request:dict) -> tuple[Response, int]:
        description= request.get('description')
        comment= request.get('comment')
        user_id= request.get('user_id')
        routine_id= request.get('routine_id')
        error :str | None = None
        if description is None:
            error = 'La descripcion es requerida'
        if comment is None:
            comment = ""
        if user_id is None:
            error = 'El user_id es requerido'
        if routine_id is None:
            error = 'El routine_id es requerido'
            
        if error is None:
            try:
                user_routine = UserRoutine(description=description, comment=comment,user_id=user_id,routine_id=routine_id)
                db.session.add(user_routine)
                db.session.commit()
                return jsonify({'message': "rutina de usuario creada con exito"}), 201
            except IntegrityError:
                db.session.rollback()
                return jsonify({'message': "problemas con el registro"}), 409
        return jsonify ({'message': error}), 422
        
        
    @staticmethod
    def update(request, id)->tuple[Response, int]:
        description= request.get('description')
        comment= request.get('comment')
        user_id= request.get('user_id')
        routine_id= request.get('routine_id')
        error :str | None = None
        if description is None:
            error = 'La descripcion es requerida'
        if user_id is None:
            error = 'El user_id es requerido'
        if routine_id is None:
            error = 'El routine_id es requerido'
            
        if error is None:
            user_routine = db.session.get(UserRoutine, id)
            if user_routine:
                try:
                    user_routine.description = description
                    user_routine.comment = comment
                    user_routine.user_id = user_id
                    user_routine.routine_id = routine_id
                    user_routine.updated_at = datetime.now()
                    db.session.commit()
                    return jsonify({'message':'rutina de usuario modificada con exito'}), 200
                except IntegrityError:
                    error = 'se necesitan todos los datos correctos' 
                    return jsonify({'message':error}), 409
            else:     
                error = 'rutina no encontrada'
            
        return jsonify({'message':error}), 404
        
    @staticmethod
    def destroy(id) -> tuple[Response, int]:
        user_routine = db.session.get(UserRoutine, id)
        error = None
        if user_routine:
            db.session.delete(user_routine)
            db.session.commit()
            return jsonify({'message':'la rutina de usuario fue eliminada con exito'}), 200
        else:
            error = 'rutina de usuario no encontrada'
        return jsonify({'message':error}), 404