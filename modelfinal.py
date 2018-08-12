from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class donate(Base):
	__tablename__ = 'needer'
	id = Column(Integer, primary_key=True)
	name = Column(String)
	story=Column(String)
	email=Column(String)
	needer_type=Column(String)
	needs = Column(String)
	phone_num=Column(Integer)
	pic=Column(String)


def __repr__(self):
	return ("Donator id: {}\n"
			"Donator name: {} \n"
			"Donator story: {} \n "
			"Donator email: {} \n "
			"Donator type: {} \n "
			"the donate: {} \n "
			"Donator phone number: {} \n ").format(
				self.id,
				self.name,
				self.story,
				self.email,
				self.needer_type,
				self.needs,
				self.phone_num)

