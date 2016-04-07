
from sqlalchemy import create_engine, Table, Column, ForeignKey
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import sessionmaker
from database_setup import Restaurant, MenuItem

engine = create_engine('sqlite:///restaurantmenu.db', echo = True)

Base = automap_base()
Base.prepare(engine)

session_creator = sessionmaker()
session_creator.configure(bind=engine)
