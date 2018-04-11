#!/usr/bin/python3
#Name:			draft_create)db.py
#Author:		Adam Stohs
#Date:			4/2018
#Purpose:		Populates the player table in the draft_test database to be used for the draft API
#Inputs:		.json containing the URL of the information, the name of the sport, and the format case for the name_brief field
#Outputs		None	
#
#
#
#
#

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from draft_create_db import Base, Player
import json
import requests

 
def main():


	print('Starting')

	engine = create_engine('sqlite:///draft_test.db')

	Base.metadata.bind = engine
	 
	DBSession = sessionmaker(bind=engine)

	session = DBSession()
	 
	#Clear old data
	num_rows_deleted = session.query(Player).delete()


	duplicates = []
	id_keys = []
	keys = []

	#get data from urls provided in file.
	with open('./sports.json') as json_data:
	    urls = json.load(json_data)
	for i in urls:
		#create dictionary
		sport = i
		url = urls[i]['url']
		name_case = urls[i]['name_brief']
		r = requests.get(url)
		data = json.loads(r.content.decode('utf-8'))
		data_raw = data['body']['players']
		
		#get data for mean age by position
		mean_age = {}
		for j in data_raw:
			key = j.get('elias_id')
			#if ID has already been used then skip
			if key in keys: 
				continue
			else:
				keys.append(j.get('elias_id'))			
				age = j.get('age', 'null')
				pos = j.get('position')
				if age and age != 'null':
					if pos not in mean_age:
						mean_age[pos] = {}
						mean_age[pos]['total'] = 1
						mean_age[pos]['mean'] = int(age)
						mean_age[pos]['sum'] = int(age)					
					else:			
						mean_age[pos]['total'] += 1
						mean_age[pos]['sum'] += int(age)
						mean_age[pos]['mean'] = int(mean_age[pos]['sum'] / mean_age[pos]['total'])

		#now create info dicionary and add to DB
		for k in data_raw:
			fname = k.get('elias_id')

			#if key has already been used then skip
			if fname in id_keys:
				duplicates.append(fname)
			else: 	
				id_keys.append(fname)
				info = {}
				firstname = str(k.get('firstname'))
				lastname = str(k.get('lastname'))
				#calculate name_brief
				if name_case == '1':
					name_brief = firstname[:1] + ". " + lastname[:1] + "." 
				elif name_case == '2':
					name_brief = firstname[:1] + ". " + lastname
				elif name_case == '3':
					name_brief = firstname + " " + lastname[:1] + "."		#
				else:
					name_brief = "NA"

				pos = k.get('position')
				age = k.get('age', 'null')
				#calculate age differnce
				if age and age != 'null':
					age_diff = (age - mean_age[k.get('position')]['mean'])
				else:
					age_diff = 'NA'
					age = 'NA'
				#Add player to database
				try:
					new_player = Player(sport=sport, elias_id=fname, first_name=firstname, last_name=lastname, position=pos, age=age, age_diff=age_diff, name_brief=name_brief)
					session.add(new_player)
				except:
					continue
		#commit changes to database.
		session.commit()
	print('Done')

if __name__=="__main__":
	main()