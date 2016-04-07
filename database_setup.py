
import os
import sys

from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()

class Restaurant(Base):
    __tablename__ = 'restaurant'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)


class MenuItem(Base):
    __tablename__ = 'menu_item'

    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    description = Column(String(250))
    price = Column(String(8))
    course = Column(String(250))
    restaurant_id = Column(Integer, ForeignKey('restaurant.id'))
    restaurant = relationship(Restaurant)

# Before we write any database code, we need to create an database engine for our db session.
engine = create_engine('sqlite:///restaurantmenu.db', echo = False)

Base.metadata.create_all(engine)

print 'Engine created!'

## # Once we have created a database engine, we can proceed to create a database session and create tables for all the database classes previously defined as Person and Address.
## 
## from sqlalchemy.ext.declarative import declarative_base
## 
## Base = declarative_base()
## 
## from sqlalchemy import create_engine
## engine = create_engine('sqlite:///restaurantmenu.db')
## from sqlalchemy.orm import sessionmaker
## 
## session = sessionmaker()
## session.configure(bind=engine)
## 
## Base.metadata.create_all(engine)
