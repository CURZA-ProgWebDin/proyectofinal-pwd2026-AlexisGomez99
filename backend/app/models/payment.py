from app.models import db
from app.models.base_model import BaseModel

class Payment(BaseModel):
    
    __tablename__= 'payments'
    amount = db.Column(db.Numeric(10, 2), nullable=False) 
    description = db.Column(db.String(200))
    service = db.Column(db.String(100))

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    user = db.relationship('User', back_populates='payments')
    
     
    def to_dict(self, with_user=True):
        data = {
            'id':self.id,
            'amount':self.amount,
            'description':self.description,
            'service':self.service,
            'created_at':self.created_at,
            'updated_at': self.updated_at,
            'active': self.active
        }
        if with_user:
            data['user']= self.user.to_dict(with_payments=False,with_roles=False)
        return data