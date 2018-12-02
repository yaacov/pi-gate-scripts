#!/usr/bin/env python

import requests
from evdev import InputDevice, KeyEvent, categorize, ecodes, events

# URL for openning latch.
lock_url = 'http://127.0.0.1:8000/latch/open'

# Path to keyboard device.
device_path = '/dev/input/by-id/usb-CHESEN_PS2_to_USB_Converter-event-kbd'

# Init keyboard device.
dev = InputDevice(device_path)

buf = []

key_map = {
'KEY_1': 1,
'KEY_2': 2,
'KEY_3': 3,
'KEY_4': 4,
'KEY_5': 5,
'KEY_6': 6,
'KEY_7': 7,
'KEY_8': 8,
'KEY_9': 9,
'KEY_0': 0,
'KEY_LEFTSHIFT': -1
}


# Check for valid UID.
def check(b):
  valid_uid = [
    [1, 2, 3, 4],
  ]

  if b in valid_uid:
    requests.get(lock_url)


# Wait for keyboard events.
for event in dev.read_loop():
  # Check for key up events.
  if event.type == ecodes.EV_KEY:
    k = KeyEvent(event)
    if k.keystate == k.key_up:

      # Append key code to global key buffer.
      code = key_map[k.keycode]
      buf.append(code)

      # Debug printing.
      print("UID: " + str(buf))

      # If this is the shift key (e.g. '*' or '#'), check bufer for uid.
      if code == -1:
        check(buf[:-2])

        # Always clean buffer after shift key.
        buf = []

