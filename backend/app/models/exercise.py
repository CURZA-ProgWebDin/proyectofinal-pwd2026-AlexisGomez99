from app.models import db
from app.models.base_model import BaseModel

class Exercise(BaseModel):
    
    __tablename__= 'exercises'
    name = db.Column(db.String(100), unique = True)
    sets = db.Column(db.String(200))
    reps = db.Column(db.String(255) )
    example_link = db.Column(db.String(255))
    weights = db.Column(db.String(255))

    info_exercises = db.relationship('InfoRoutine', back_populates='exercise')

    
     
    def to_dict(self, with_info_routine=True):
        data = {
          'id':self.id,
          'name':self.name,
          'sets':self.sets,
          'reps':self.reps,
          'example_link':self.example_link,
          'weights': self.weights,
          'created_at':self.created_at,
          'updated_at': self.updated_at,
          'active': self.active
        }
    
        if with_info_routine:
          data['routines']= [info_exercise.to_dict(with_exercise=False) for info_exercise in self.info_exercises]
        return data
      