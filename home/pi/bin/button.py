#!/usr/bin/env python

from time import sleep
import RPi.GPIO as GPIO
#import requests
import urllib3

# URL for openning latch.
http=urllib3.PoolManager()
lock_url = 'http://127.0.0.1:8000/latch/open?button'

# Init latch pin and state consts.
latch_pin = 18
latch_open = GPIO.LOW
latch_lock = GPIO.HIGH

# Init GPIO lock latch.
GPIO.setmode(GPIO.BOARD)
GPIO.setup(latch_pin, GPIO.IN)

print("start button reader on:", latch_pin)
while True:
    state = GPIO.input(latch_pin)
    sleep(0.1)
    if state == 1:
        print("pressed")
        http.request('get',lock_url)
        #requests.get(lock_url)
        sleep(1)
