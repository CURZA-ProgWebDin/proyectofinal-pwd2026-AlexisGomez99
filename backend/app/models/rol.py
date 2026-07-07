from app.models import db
from app.models.base_model import BaseModel

class Rol(BaseModel):
    
    __tablename__="roles"
    name = db.Column(db.String, unique = True)
    users = db.relationship('User', back_populates='rol')
        
    def to_dict(self, with_users=True):
        data= {
            'id': self.id,
            'name': self.name,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
            'active': self.active
        }
        if with_users:
            data['users'] = [user.to_dict(with_roles=False,with_info=False,with_payments=False,with_routines=False) for user in self.users]
        return data
    