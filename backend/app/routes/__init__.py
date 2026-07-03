from app.routes.user_routes import users
from app.routes.rol_routes import roles
from app.routes.auth_routes import auth_bp
from flask import Blueprint

api_v1 = Blueprint('api_v1', __name__, url_prefix='/api_v1')

api_v1.register_blueprint(users,url_prefix='/users')
api_v1.register_blueprint(roles,url_prefix='/roles')
api_v1.register_blueprint(auth_bp,url_prefix='/auth')