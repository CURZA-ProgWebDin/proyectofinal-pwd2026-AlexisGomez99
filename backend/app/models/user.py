from app.models import db
from app.models.base_model import BaseModel
from werkzeug.security import generate_password_hash, check_password_hash

class User(BaseModel):
    
    __tablename__= 'users'
    name = db.Column(db.String(100), unique = True)
    email = db.Column(db.String(200), unique =True)
    password = db.Column(db.String(255) )

    rol_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    rol = db.relationship('Rol', back_populates='users')
    info_user = db.relationship('InfoUser', back_populates='user', uselist=False)
    payments = db.relationship('Payment', back_populates='user')
    routines = db.relationship('UserRoutine', back_populates='user')

    
     
    def to_dict(self, with_roles=True, with_info=True, with_payments=True, with_routines=True):
        data = {
          'id':self.id,
          'name':self.name,
          'email':self.email,
          'created_at':self.created_at,
          'updated_at': self.updated_at,
          'active': self.active
        }
        if with_roles:
          data['rol']= self.rol.to_dict(with_users = False)
        if with_info:
          data['info']= self.info_user.to_dict(with_user = False) if self.info_user else None
        if with_payments:
          data['payments']= [payment.to_dict(with_user=False) for payment in self.payments]
        if with_routines:
          data['routines']= [routine.to_dict(with_user=False) for routine in self.routines]
        return data
      
    def validate_password(self, password:str) -> bool:
        return check_password_hash(self.password, password)
    
    def generate_password(self, password:str):
        self.password = generate_password_hash(password)