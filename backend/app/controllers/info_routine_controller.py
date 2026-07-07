from typing import Literal
from sqlalchemy.exc import IntegrityError
from app.models.info_routine import InfoRoutine
from datetime import datetime
from app.models import db
from flask import Response, jsonify
from app.controllers import Controller

class InfoRoutineController (Controller):
    
    @staticmethod
    def get_all() -> tuple[Response, int]:
        info_routines_list = db.session.execute(db.select(InfoRoutine).order_by(db.desc(InfoRoutine.id))).scalars().all()
        if len(info_routines_list) > 0:
            info_routines_to_dict = [info_routine.to_dict() for info_routine in info_routines_list ]
            return jsonify(info_routines_to_dict), 200 
        return jsonify({"message": 'datos no encontrados'}), 404
    
    @staticmethod
    def show(id)->tuple[Response, int]:
        info_routine = db.session.get(InfoRoutine, id)
        if info_routine:
            return jsonify(info_routine.to_dict()), 200
        return jsonify({"message": 'informacion de rutina no encontrada'}), 404
    
    @staticmethod
    def create(request:dict) -> tuple[Response, int]:
        day= request.get('day')
        name_section= request.get('name_section')
        exercise_id= request.get('exercise_id')
        routine_id= request.get('routine_id')
        error :str | None = None
        if day is None:
            error = 'El dia es requerido'
        if name_section is None:
            error = 'El nombre de la seccion es requerido'
        if exercise_id is None:
            error = 'El ejercicio es requerido'
        if routine_id is None:
            error = 'La rutina es requerida'
            
        if error is None:
            try:
                info_routine = InfoRoutine(day=day, name_section=name_section,exercise_id=exercise_id,routine_id=routine_id)
                db.session.add(info_routine)
                db.session.commit()
                return jsonify({'message': "informacion de rutina creada con exito"}), 201
            except IntegrityError:
                db.session.rollback()
                return jsonify({'message': "informacion de rutina ya registrada"}), 409
        return jsonify ({'message': error}), 422
        
        
    @staticmethod
    def update(request, id)->tuple[Response, int]:
        day= request.get('day')
        name_section= request.get('name_section')
        exercise_id= request.get('exercise_id')
        routine_id= request.get('routine_id')
        error :str | None = None
        if day is None:
            error = 'El dia es requerido'
        if name_section is None:
            error = 'El nombre de la seccion es requerido'
        if exercise_id is None:
            error = 'El ejercicio es requerido'
        if routine_id is None:
            error = 'La rutina es requerida'
            
        if error is None:
            info_routine = db.session.get(InfoRoutine, id)
            if info_routine:
                try:
                    info_routine.day = day
                    info_routine.name_section = name_section
                    info_routine.exercise_id = exercise_id
                    info_routine.routine_id = routine_id
                    info_routine.updated_at = datetime.now()
                    db.session.commit()
                    return jsonify({'message':'informacion de rutina modificada con exito'}), 200
                except IntegrityError:
                    error = 'se necesitan todos los datos correctos' 
                    return jsonify({'message':error}), 409
            else:     
                error = 'informacion de rutina no encontrada'
            
        return jsonify({'message':error}), 404
        
    @staticmethod
    def destroy(id) -> tuple[Response, int]:
        info_routine = db.session.get(InfoRoutine, id)
        error = None
        if info_routine:
            db.session.delete(info_routine)
            db.session.commit()
            return jsonify({'message':'la informacion de rutina fue eliminada con exito'}), 200
        else:
            error = 'informacion de rutina no encontrada'
        return jsonify({'message':error}), 404