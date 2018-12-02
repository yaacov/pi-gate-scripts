#!/usr/bin/env python

import requests
from time import sleep
from pirc522 import RFID

# URL for openning latch.
lock_url = 'http://127.0.0.1:8000/latch/open'

# Init NFC reader.
rdr = RFID()


# Check for valid UID.
def check(b):
  valid_uid = [
    [210, 5, 105, 27, 165],
  ]

  if b in valid_uid:
    requests.get(lock_url)


# Wait for NFC cards.
while True:
  rdr.wait_for_tag()
  (error, tag_type) = rdr.request()
  if not error:
    (error, uid) = rdr.anticoll()
    if not error:
      # Debug printing.
      print("UID: " + str(uid))

      # Check for valid UID.
      check(uid)
      sleep(1)

# Calls GPIO cleanup
rdr.cleanup()
