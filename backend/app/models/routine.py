from app.models import db
from app.models.base_model import BaseModel

class Routine(BaseModel):
    __tablename__= "routines"
    name = db.Column(db.String(100))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    user = db.relationship('User', back_populates='routines')
    routines_exercises = db.relationship('InfoRoutine', back_populates='routine')
     
    def to_dict(self, with_info_routines=True, with_user=True):
        data = {
            'id':self.id,
            'name':self.name,
            'created_at':self.created_at,
            'updated_at': self.updated_at,
            'active': self.active
        }
        if with_info_routines:
            data['routine_exercises']= [routines_exercise.to_dict(with_routine=False) for routines_exercise in self.routines_exercises]
        if with_user:
            data['user'] = self.user.to_dict(with_roles=False,with_info=False,with_payments=False,with_routine=False) if self.user else None
        return data