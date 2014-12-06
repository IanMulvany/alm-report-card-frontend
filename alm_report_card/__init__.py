import sys
import os
from flask import Flask
import requests
import logging, sys

app = Flask(__name__)
app.config.from_object('config') # gets config info from config.py

import alm_report_card.models
import alm_report_card.views

if __name__ == '__main__':
	app.run()
