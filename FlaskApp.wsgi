#!/usr/bin/python

import sys
import logging

logging.basicConfig(stream=sys.stderr)
sys.path.insert(o,"/var/www/FlaskApp")

from FlaskApp import app as application

application.secret_key = 'Something that is secret'
