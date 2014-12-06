from alm_report_card import app
from alm_report_card import models
import requests
import random
from flask.ext.restful import reqparse, abort, Api, Resource
from flask import jsonify, Response
import json

api = Api(app)

# def jsonp_wrapper(result):
# 	return "if (!window.handleDocList) { console.error('Could not find JSONP callback.'); } else { window.handleDocList(" + result +"); }"

class About(Resource):
	def get(self):
		return "this is a test api for eLife prototyping, we will put our interface here"

class ReportWall(Resource):
	def get(self):
		return "this is the wall of shame"

class Report(Resource):
	def get(self, host_id):
		return "this is info about article %s" % host_id  

api.add_resource(About, '/')
api.add_resource(ReportWall, '/reports')
api.add_resource(Report, '/reports/host_id/<string:host_id>')

