from app.models import db
from app.models.base_model import BaseModel

class InfoRoutine(BaseModel):
    __tablename__ ="info_routines"
    day = db.Column(db.String(40))
    name_section = db.Column(db.String(80))
    description = db.Column(db.String(200))
    comment = db.Column(db.String(200))
    sets = db.Column(db.String(200))
    reps = db.Column(db.String(255) )
    weights = db.Column(db.String(255))

    exercise_id = db.Column(db.Integer, db.ForeignKey('exercises.id'), nullable=False)
    routine_id = db.Column(db.Integer, db.ForeignKey('routines.id'), nullable=False)
    

    routine = db.relationship('Routine', back_populates='routines_exercises')
    exercise = db.relationship('Exercise', back_populates='info_exercises')
    
    
    def to_dict(self, with_exercise=True, with_routine=True,):
        data = {
            'id':self.id,
            'day':self.day,
            'comment': self.comment,
            'description': self.description,
            'sets': self.sets,
            'reps': self.reps,
            'weights': self.weights,
            'name_section':self.name_section,
            'exercise_id':self.exercise_id,
            'routine_id':self.routine_id,
            'created_at':self.created_at,
            'updated_at': self.updated_at,
            'active': self.active
        }
        if with_exercise:
            data['exercise']= self.exercise.to_dict(with_info_routine=False)
        if with_routine:
            data['routine']= self.routine.to_dict(with_info_routines=False)
        
        return data