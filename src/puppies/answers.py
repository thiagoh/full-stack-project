from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from puppies import Base, Shelter, Puppy
#from flask.ext.sqlalchemy import SQLAlchemy
from random import randint
import datetime
import random

engine = create_engine('sqlite:///puppyshelter.db')

Base.metadata.bind = engine

session_creator = sessionmaker(bind=engine)

s = session_creator()

for p in s.query(Puppy).order_by(Puppy.name.desc()).all():
   print p.name + ' was born in ' + str(p.dateOfBirth)

from datetime import datetime, date, timedelta
six_months_back = datetime.now() - timedelta(days=6*30)

for p in s.query(Puppy).filter(Puppy.dateOfBirth >= six_months_back).order_by(Puppy.dateOfBirth.asc()).all():
   print p.name + ' was born in ' + str(p.dateOfBirth)

for p in s.query(Puppy).order_by(Puppy.weight.asc()).all():
   print p.name + ' wheighs ' + str(p.weight)

for shelter in s.query(Shelter).all():
   print shelter.name + ' shelter houses \n'
   for p in s.query(Puppy).filter(Puppy.shelter == shelter).order_by(Puppy.name.asc()).all():
      print '  ' + p.name + ' wheighs ' + str(p.weight)
   print '---------- \n'
