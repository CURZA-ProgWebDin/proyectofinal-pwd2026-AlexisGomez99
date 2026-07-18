from typing import Literal
from sqlalchemy.exc import IntegrityError
from app.models.exercise import Exercise
from datetime import datetime
from app.models import db
from flask import Response, jsonify
from app.controllers import Controller

class ExerciseController (Controller):
    
    @staticmethod
    def get_all() -> tuple[Response, int]:
        exercises_list = db.session.execute(db.select(Exercise).order_by(db.desc(Exercise.id))).scalars().all()
        if len(exercises_list) > 0:
            exercises_to_dict = [exercise.to_dict() for exercise in exercises_list ]
            return jsonify(exercises_to_dict), 200 
        return jsonify({"message": 'datos no encontrados'}), 404
    
    @staticmethod
    def show(id)->tuple[Response, int]:
        exercise = db.session.get(Exercise, id)
        if exercise:
            return jsonify(exercise.to_dict()), 200
        return jsonify({"message": 'ejercicio no encontrado'}), 404
    
    @staticmethod
    def create(request:dict) -> tuple[Response, int]:
        name= request.get('name')
        sets= request.get('sets')
        reps= request.get('reps')
        example_link = request.get('example_link')
        weights = request.get('weights')
        error :str | None = None
        if name is None:
            error = 'El nombre es requerido'
        if sets is None:
            error = 'Las series es requeridas'
        if reps is None:
            error = 'Las repeticiones son requeridas'
        if weights is None:
            error = 'El peso es requerido'
            
        if error is None:
            try:
                exercise = Exercise(name=name, sets=sets, reps=reps, example_link=example_link, weights=weights)
                db.session.add(exercise)
                db.session.commit()
                return jsonify({'message': "ejercicio creado con exito"}), 201
            except IntegrityError:
                db.session.rollback()
                return jsonify({'message': "ejercicio ya registrado"}), 409
        return jsonify ({'message': error}), 422
        
        
    @staticmethod
    def update(request, id)->tuple[Response, int]:
        name= request.get('name')
        sets= request.get('sets')
        reps= request.get('reps')
        example_link = request.get('example_link')
        weights = request.get('weights')
        error :str | None = None
        if name is None:
            error = 'El nombre es requerido'
        if sets is None:
            error = 'Las series es requeridas'
        if reps is None:
            error = 'Las repeticiones son requeridas'
        if weights is None:
            error = 'El peso es requerido'
            
        if error is None:
            exercise = db.session.get(Exercise, id)
            if exercise:
                try:
                    exercise.name = name
                    exercise.sets = sets
                    exercise.reps = reps
                    exercise.example_link = example_link
                    exercise.weights = weights
                    exercise.updated_at = datetime.now()
                    db.session.commit()
                    return jsonify({'message':'ejercicio modificado con exito'}), 200
                except IntegrityError:
                    error = 'se necesitan todos los datos correctos' 
                    return jsonify({'message':error}), 409
            else:     
                error = 'ejercicio no encontrado'
            
        return jsonify({'message':error}), 404
        
    @staticmethod
    def destroy(id) -> tuple[Response, int]:
        exercise = db.session.get(Exercise, id)
        error = None
        if exercise:
            db.session.delete(exercise)
            db.session.commit()
            return jsonify({'message':'el ejercicio fue eliminado con exito'}), 200
        else:
            error = 'ejercicio no encontrado'
        return jsonify({'message':error}), 404