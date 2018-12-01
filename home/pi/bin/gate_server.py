#!/usr/bin/env python

from time import sleep
from flask import Flask
from flask import jsonify
from gevent.pywsgi import WSGIServer

import RPi.GPIO as GPIO

# Init latch pin and state consts.
latch_pin = 5
latch_open = GPIO.LOW
latch_lock = GPIO.HIGH

# Init GPIO lock latch.
GPIO.setmode(GPIO.BOARD)
GPIO.setup(latch_pin, GPIO.OUT)
GPIO.output(latch_pin, latch_lock)

# Init the Flask application.
app = Flask(__name__)


@app.route('/')
def status():
  # Return state lock.
  d = {
    "state": "lock",
  }
  return jsonify(d)

@app.route('/latch/open')
def unlock():
  GPIO.output(latch_pin, latch_open)
  sleep(2)
  GPIO.output(latch_pin, latch_lock)

  # Return state done.
  d = {
    "state": "done",
  }
  return jsonify(d)


# Start gevent server.
http_server = WSGIServer(('', 8000), app)
http_server.serve_forever()

