from typing import Literal
from sqlalchemy.exc import IntegrityError
from app.models.user import User
from datetime import datetime
from app.models import db
from flask import Response, jsonify
from app.controllers import Controller

class UserController (Controller):
    
    @staticmethod
    def get_all() -> tuple[Response, int]:
        usuarios_list = db.session.execute(db.select(User).order_by(db.desc(User.id))).scalars().all()
        if len(usuarios_list) > 0:
            usuarios_to_dict = [usuario.to_dict() for usuario in usuarios_list ]
            return jsonify(usuarios_to_dict), 200 
        return jsonify({"message": 'datos no encontrados'}), 404
    
    @staticmethod
    def show(id)->tuple[Response, int]:
        usuario = db.session.get(User, id)
        if usuario:
            return jsonify(usuario.to_dict()), 200
        return jsonify({"message": 'usuario no encontrado'}), 404
    
    @staticmethod
    def create(request:dict) -> tuple[Response, int]:
        name:str | None = request.get('name')
        email:str | None = request.get('email')
        password:str | None = request.get('password')
        rol_id = request.get('rol_id')
        error :str | None = None
        if name is None:
            error = 'El nombre es requerido'
        if email is None:
            error = 'El email es requerido'
        if password is None:
            error = 'La contraseña es requerida'
        if rol_id is None:
            error = 'El rol es requerido'
            
        if error is None:
            try:
                if rol_id and name and password and email is not None:
                    user = User(name=name, email=email, rol_id=rol_id, password=password)    
                    user.generate_password(password)
                    db.session.add(user)
                    db.session.commit()
                return jsonify({'message': "usuario creado con exito"}), 201               
                
            except IntegrityError:
                db.session.rollback()
                return jsonify({'message': "Usuario ya registrado"}), 409
        
        
    @staticmethod
    def update(request, id)->tuple[Response, int]:
        name= request.get('name')
        email= request.get('email')
        rol_id = request.get('rol_id')
        active = request.get('active')
        error :str | None = None
        if name is None:
            error = 'El name es requerido'
        if email is None:
            error = 'El email es requerido'
        if rol_id is None:
            error = 'El rol es requerido'

            
        if error is None:
            usuario = db.session.get(User, id)
            if usuario:
                try:
                    usuario.name = name
                    usuario.email = email
                    usuario.rol_id = rol_id
                    usuario.active = active
                    usuario.updated_at = datetime.now()
                    db.session.commit()
                    return jsonify({'message':'usuario modificado con exito'}), 200
                except IntegrityError:
                    error = 'el email o el username ya existen' 
                    return jsonify({'message':error}), 409
            else:     
                error = 'usuario no encontrado'
            
        return jsonify({'message':error}), 404
        
    @staticmethod
    def destroy(id) -> tuple[Response, int]:
        usuario = db.session.get(User, id)
        error = None
        if usuario:
            db.session.delete(usuario)
            db.session.commit()
            return jsonify({'message':'el usuario fue eliminado con exito'}), 200
        else:
            error = 'usuario no encontrado'
        return jsonify({'message':error}), 404