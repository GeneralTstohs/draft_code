#!/usr/bin/python3
#Name:			draft_api.py
#Author:		Adam Stohs
#Date:			4/2018
#Purpose:		API for getting player information by querying either the elias id or the sport.
#Inputs:		Either the elias id or the name of the sport
#Outputs		A player single player onbject for the player endpoint and a list of player objects for the sport endpoint
#
#
#
#
#


from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from flask.ext.jsonpify import jsonify
from draft_create_db import Base, Player
from sqlalchemy import create_engine
engine = create_engine('sqlite:///draft_test.db')
Base.metadata.bind = engine
from sqlalchemy.orm import sessionmaker
DBSession = sessionmaker()
DBSession.bind = engine
session= DBSession()


app = Flask(__name__)
api = Api(app)

#turns the query result into a json format
def createJSON(result):

	player = {}
	player = {'id':result.elias_id,
			'name_brief':result.name_brief,
			'first_name':result.first_name,
			'last_name':result.last_name,
			'position':result.position,
			'age':result.age,
			'average_position_age_diff':result.age_diff
			}
	player_json = jsonify(player)
	return player_json


#getPLayer endpoint. Returns a single player object.
class getPlayer(Resource):
	def get(self, name):
		self.name  = name
		result = session.query(Player).filter(Player.elias_id == self.name).one()

		return createJSON(result)


#getSport endpoint. Return list of player objects		 
class getSport(Resource):
	def get(self, sport):
		self.sport = sport
		player_list = []
		result = session.query(Player).filter(Player.sport == self.sport).all()
		for i in result:
			player = {}
			player = {'id':i.elias_id,
				'name_brief':i.name_brief,
				'first_name':i.first_name,
				'last_name':i.last_name,
				'position':i.position,
				'age':i.age,
				'average_position_age_diff':i.age_diff
				}
			player_list.append(player)
		return player_list



api.add_resource(getPlayer, 'draft//player/<string:name>') # Route_1
api.add_resource(getSport, 'draft//sport/<string:sport>') #Route 2


if __name__=='__main__':
	app.run(debug=True)