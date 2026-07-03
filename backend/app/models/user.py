from app.models import db
from app.models.base_model import BaseModel
from werkzeug.security import generate_password_hash, check_password_hash

class User(BaseModel):
    
    __tablename__= 'users'
    name = db.Column(db.String(100), unique = True)
    email = db.Column(db.String(200), unique =True)
    rol_id = db.Column(db.Integer, db.ForeignKey('roles.id'),)
    password = db.Column(db.String(255) )
    rol = db.relationship('Rol', back_populates='users')
    
     
    def to_dict(self, with_roles=True):
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
      return data
      
    def validate_password(self, password:str) -> bool:
      return check_password_hash(self.password, password)
    
    def generate_password(self, password:str):
      self.password = generate_password_hash(password)