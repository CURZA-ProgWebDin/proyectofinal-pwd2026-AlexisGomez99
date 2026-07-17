from app.routes.user_routes import users
from app.routes.rol_routes import roles
from app.routes.auth_routes import auth_bp
from app.routes.exercise_routes import exercises
from app.routes.info_routine_routes import info_routines
from app.routes.info_user_routes import info_users
from app.routes.payment_routes import payments
from app.routes.routine_routes import routines

from flask import Blueprint

api_v1 = Blueprint('api_v1', __name__, url_prefix='/api_v1')

api_v1.register_blueprint(users,url_prefix='/users')
api_v1.register_blueprint(roles,url_prefix='/roles')
api_v1.register_blueprint(auth_bp,url_prefix='/auth')
api_v1.register_blueprint(exercises,url_prefix='/exercises')
api_v1.register_blueprint(info_routines,url_prefix='/info_routines')
api_v1.register_blueprint(info_users,url_prefix='/info_users')
api_v1.register_blueprint(payments,url_prefix='/payments')
api_v1.register_blueprint(routines,url_prefix='/routines')