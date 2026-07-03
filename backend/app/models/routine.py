from app.models import db
from app.models.base_model import BaseModel

class Routine(BaseModel):
    __tablename__= "routines"
    name = db.Column(db.String(100))

    user_routines = db.relationship('UserRoutine', back_populates='routine')
    
     
    def to_dict(self, with_user_routine=True):
        data = {
            'id':self.id,
            'name':self.name,
            'created_at':self.created_at,
            'updated_at': self.updated_at,
            'active': self.active
        }
        if with_user_routine:
            data['user']= self.user_routines.to_dict(with_routine=False)
        return data