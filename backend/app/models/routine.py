from app.models import db
from app.models.base_model import BaseModel

class Routine(BaseModel):
    __tablename__= "routines"
    name = db.Column(db.String(100))

    user_routines = db.relationship('UserRoutine', back_populates='routine')
    routines_exercises = db.relationship('InfoRoutine', back_populates='routine')
     
    def to_dict(self, with_user_routines=True, with_info_routines=True):
        data = {
            'id':self.id,
            'name':self.name,
            'created_at':self.created_at,
            'updated_at': self.updated_at,
            'active': self.active
        }
        if with_user_routines:
            data['user_routine']= [user_routine.to_dict(with_routine=False) for user_routine in self.user_routines]
        if with_info_routines:
            data['routine_exercises']= [routines_exercise.to_dict(with_routine=False) for routines_exercise in self.routines_exercises]
        return data