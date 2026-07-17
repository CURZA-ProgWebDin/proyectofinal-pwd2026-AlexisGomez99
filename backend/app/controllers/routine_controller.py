from typing import Literal
from sqlalchemy.exc import IntegrityError
from app.models.routine import Routine
from datetime import datetime
from app.models import db
from flask import Response, jsonify
from app.controllers import Controller

class RoutineController (Controller):
    
    @staticmethod
    def get_all() -> tuple[Response, int]:
        routines_list = db.session.execute(db.select(Routine).order_by(db.desc(Routine.id))).scalars().all()
        if len(routines_list) > 0:
            routines_to_dict = [routine.to_dict() for routine in routines_list ]
            return jsonify(routines_to_dict), 200 
        return jsonify({"message": 'datos no encontrados'}), 404
    
    @staticmethod
    def get_my_routines(id) -> tuple[Response, int]:
        routines_list = db.session.execute(db.select(Routine).filter_by(user_id=id).order_by(db.desc(Routine.id))).scalars().all()
        if len(routines_list) > 0:
            routines_to_dict = [routine.to_dict() for routine in routines_list ]
            return jsonify(routines_to_dict), 200 
        return jsonify({"message": 'datos no encontrados'}), 404
    
    @staticmethod
    def show(id)->tuple[Response, int]:
        routine = db.session.get(Routine, id)
        if routine:
            return jsonify(routine.to_dict()), 200
        return jsonify({"message": 'rutina no encontrada'}), 404
    
    @staticmethod
    def create(request:dict) -> tuple[Response, int]:
        name= request.get('name')
        error :str | None = None
        if name is None:
            error = 'El nombre es requerido'
            
        if error is None:
            try:
                routine = Routine(name=name)
                db.session.add(routine)
                db.session.commit()
                return jsonify({'message': "rutina creada con exito"}), 201
            except IntegrityError:
                db.session.rollback()
                return jsonify({'message': "rutina ya registrado"}), 409
        return jsonify ({'message': error}), 422
        
        
    @staticmethod
    def update(request, id)->tuple[Response, int]:
        name= request.get('name')
        user_id = request.get('user_id')
        error :str | None = None
        if name is None:
            error = 'El nombre es requerido'
        if user_id is None:
            error = 'El usuario es requerido'
            
        if error is None:
            routine = db.session.get(Routine, id)
            if routine:
                try:
                    routine.name = name
                    routine.user_id = user_id
                    routine.updated_at = datetime.now()
                    db.session.commit()
                    return jsonify({'message':'rutina modificada con exito'}), 200
                except IntegrityError:
                    error = 'se necesitan todos los datos correctos' 
                    return jsonify({'message':error}), 409
            else:     
                error = 'rutina no encontrada'
            
        return jsonify({'message':error}), 404
        
    @staticmethod
    def destroy(id) -> tuple[Response, int]:
        routine = db.session.get(Routine, id)
        error = None
        if routine:
            db.session.delete(routine)
            db.session.commit()
            return jsonify({'message':'la rutina fue eliminada con exito'}), 200
        else:
            error = 'rutina no encontrada'
        return jsonify({'message':error}), 404