# Database related imports
# Make sure to import your tables!
from model import Base, Donate

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# You can change the name of your database, just change project.db to whatever you want (make sure to include .db at the end!)
# Make sure you have the same name for the database in the app.py file!
engine = create_engine('sqlite:///project.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Your database functions are located under here (querying, adding items, etc.)

# Example of adding a student:
def add_donate(name,story,email, needer_type, needs, phone_num, adress, link, pic):
    print("Added a donate!")
    don = Donate(name=name,story=story, email=email, needer_type=needer_type, needs=needs,phone_num=phone_num,adress=adress,link=link, pic=pic)
    session.add(don)
    session.commit()

def get_all_donates():
    donates = session.query(Donate).all()
    return donates

gilad=add_donate("gilad" , "i want to buy ice cream" , "g@gmail.com" , "person", "money", 000, "ha","rf", "ddfsdf")
