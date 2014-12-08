from alm_report_card import app
from alm_report_card import models
import requests
import random
from flask.ext.restful import reqparse, abort, Api, Resource
from flask import render_template
from flask import jsonify, Response
import json

api = Api(app)

"""
[u'Hogrefe & Huber', u'American Geophysical Union (AGU)', u'Elsevier BV', u'SAGE Publications', u'AVES Publishing Co.', u'Informa UK Limited', u'Springer Science + Business Media', u'Society of Petroleum Engineers (SPE)', u'Ovid Technologies (Wolters Kluwer Health)', u'American Medical Association (AMA)', u'American Chemical Society (ACS)', u'Royal Society of Chemistry (RSC)', u'Nature Publishing Group', u'Ebsco Publishing', u'Portland Press Ltd.', u'European Mathematical Publishing House', u'Scitepress', u'Index Copernicus', u'Binwin BT', u'InTech']

http://almability.crowdometer.org/members/4374/works 

{ "status": "ok", "message-type": "work-list", "message-version": "1.0.0", "message": [ { "doi": "10.7554/elife.02252.046", "url": null, "error": "Canonical URL mismatch: /content/3/e02252 for http://elifesciences.org/content/3/e02252/f1/f43", "status": 404 }, { "doi": "10.7554/elife.02590", "url": "http://doi.org/10.7554/elife.02590", "error": null, "status": 200 }, { "doi": "10.7554/elife.00422.001", "url": null, "error": "Canonical URL mismatch: /content/2/e00422 for http://elifesciences.org/content/2/e00422/abstract-1", "status": 404 }, { "doi": "10.7554/elife.00658.015", "url": null, "error": "Canonical URL mismatch: /content/2/e00658 for http://elifesciences.org/content/2/e00658/f11", "status": 404 }, { "doi": "10.7554/elife.02208.016", "url": null, "error": "Canonical URL mismatch: /content/3/e02208 for http://elifesciences.org/content/3/e02208/f13/f14", "status": 404 }, { "doi": "10.7554/elife.01433.010", "url": null, "error": "Canonical URL mismatch: /content/3/e01433 for http://elifesciences.org/content/3/e01433/f5/f7", "status": 404 }, { "doi": "10.7554/elife.01603.001", "url": null, "error": "Canonical URL mismatch: /content/3/e01603 for http://elifesciences.org/content/3/e01603/abstract-1", "status": 404 }, { "doi": "10.7554/elife.01433.020", "url": null, "error": "Canonical URL mismatch: /content/3/e01433 for http://elifesciences.org/content/3/e01433/media-4", "status": 404 }, { "doi": "10.7554/elife.02206.009", "url": null, "error": "Canonical URL mismatch: /content/3/e02206 for http://elifesciences.org/content/3/e02206/f4", "status": 404 }, { "doi": "10.7554/elife.01202.011", "url": null, "error": "Canonical URL mismatch: /content/2/e01202 for http://elifesciences.org/content/2/e01202/f3/dc4", "status": 404 } ] }

"""


# def jsonp_wrapper(result):
# 	return "if (!window.handleDocList) { console.error('Could not find JSONP callback.'); } else { window.handleDocList(" + result +"); }"

# class About(Resource):
# 	def get(self):
# 		name = "bob"
# 		return render_template('index.html', name=name)



def get_publishers_from_crossref():
	url = "http://api.crossref.org/members"
	r = requests.get(url)
	result = r.json()
	names_ids = {}
	names = []
	for member in result["message"]["items"]:
		names_ids[member["primary-name"]] = member["id"]
		names.append(str(member["primary-name"]))
	return names_ids, names

# class ReportWall(Resource):
# 	def get(self):
# 		return "this is the wall of shame"

# class Report(Resource):
# 	def get(self, host_id):
# 		return "this is info about article %s" % host_id  
 
@app.route('/')
def landing_page():
	names_ids, names = get_publishers_from_crossref()
	for name in names:
		print name 
	print names 
	return render_template('index.html', names=names, name_id_lookups=names_ids)

# api.add_resource(About, '/')
@app.route('/reports')
def Report_Wall():
	return "this is the wall of shame"

@app.route('/reports/host_id/<string:host_id>')
def publisher_report(host_id):
	return render_template('report.html', publisher_id=host_id)


