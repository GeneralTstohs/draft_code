#!/usr/bin/python3
#Name:			draft_create_db.py
#Author:		Adam Stohs
#Date:			4/2018
#Purpose:		Creates Database to be used for the draft API
#Inputs:		None
#Outputs		creates the draft test database in the current directory	
#
#
#
#
#


import os
import sys
import json
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
 

Base = declarative_base()
 

#creates player table
class Player(Base):
	__tablename__ = 'player'
	# Here we define columns for the table person
	# Notice that each column is also a normal Python instance attribute.
	sport = Column(String(250))
	elias_id = Column(String(250), nullable=False, primary_key=True)
	name_brief = Column(String(250))
	first_name = Column(String(250))
	last_name = Column(String(250))
	position = Column(String(250))
	age = Column(String(250))
	age_diff = Column(String(250))




def main():

	# Create an engine that stores data in the local directory's
	# sqlalchemy_example.db file.
	engine = create_engine('sqlite:///draft_test.db')
 
	# Create all tables in the engine. This is equivalent to "Create Table"
	# statements in raw SQL.
	Base.metadata.create_all(engine)

	print (engine.table_names())
	print(Player.__table__.columns.keys())

if __name__=="__main__":
	main()