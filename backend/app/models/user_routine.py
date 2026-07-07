from app.models import db
from app.models.base_model import BaseModel

class UserRoutine(BaseModel):
    __tablename__ ="user_routines"
    description = db.Column(db.String(200))
    comment = db.Column(db.String(200))
    
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    routine_id = db.Column(db.Integer, db.ForeignKey('routines.id'), nullable=False)
    
    user = db.relationship('User', back_populates='routines')
    routine = db.relationship('Routine', back_populates='user_routines')
    
    def to_dict(self, with_user=True, with_routine=True):
        data = {
            'id':self.id,
            'description':self.description,
            'comment':self.comment,
            'user_id':self.user_id,
            'routine_id':self.routine_id,
            'created_at':self.created_at,
            'updated_at': self.updated_at,
            'active': self.active
        }
        if with_user:
            data['user']= self.user.to_dict(with_payments=False,with_roles=False,with_routines=False,with_info=False)
        if with_routine:
            data['routine']= self.routine.to_dict(with_user_routines=False)
        
        return data