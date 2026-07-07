from app.models import db
from app.models.base_model import BaseModel

class InfoUser(BaseModel):
    
    __tablename__= 'info_users'
    dni = db.Column(db.String(8), unique = True)
    name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    number_phone = db.Column(db.String(50))
    adress = db.Column(db.String(200))

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), unique=True)
    user = db.relationship('User', back_populates='info_user')
    
     
    def to_dict(self, with_user=True):
        data = {
            'id':self.id,
            'dni':self.dni,
            'name':self.name,
            'last_name':self.last_name,
            'number_phone': self.number_phone,
            'adress': self.adress,
            'created_at':self.created_at,
            'updated_at': self.updated_at,
            'active': self.active
        }
        if with_user:
            data['user']= self.user.to_dict(with_info = False,with_payments = False)
        return data