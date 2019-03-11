# Prepare for use with:
# sudo pip install unicornhat

# run this script with sudo python unicorn_app.py

# import the Pimoroni Unicorn library
import unicornhat as uh
import time, socket # Used to retrieve hostname
from flask import Flask, request # Flask microservice
from random import random, randint

# Specify that the pHAT is used (instead of a HAT)
uh.set_layout(uh.PHAT)

width, height = uh.get_shape()
serial_display_pixel = -1

app = Flask(__name__)
hostname = socket.gethostname()

# Calculate approximate RGB values from hue parameter
def to_rgb(hue):
  if hue < (1.0 / 3.0):
    r = 2 - hue * 6
    g = hue * 6
    b = 0
  elif hue < (2.0 / 3.0):
    r = 0
    g = 4 - hue * 6
    b = hue * 6 - 2
  else:
    r = hue * 6 - 4
    g = 0
    b = (1 - hue) * 6

  if r > 1:
    r = 1
  if g > 1:
    g = 1
  if b > 1:
    b = 1

  r = int(r * 255)
  g = int(g * 255)
  b = int(b * 255)

  return (r, g, b)

# Determine if the pixel is in an acceptable range
def valid_pixel(x, y, hue):
  if x < 0 or x >= width or y < 0 or y >= height or hue < 0 or hue > 1:
    return False
  else:
    return True 

@app.route('/set')
def set():
  x = request.args.get('x', default=None, type=int)
  y = request.args.get('y', default=None, type=int)
  hue = request.args.get('hue', default=None, type=float)

  invalid_msg = "{'usage':'http://%s/set?x=[0..%s]&y=[0..%s]&hue=[0..1]'}" % (hostname, max_x - 1, max_y - 1)

  if (x is not None) and (y is not None) and (hue is not None):
    if valid_pixel(x,y,hue):
      r,g,b = to_rgb(hue)
      uh.set_pixel(x,y,r,g,b)
      uh.show()
      return "{'result':'Set a pixel at (%s,%s)'}" % (x,y), 200
    else:
      return invalid_msg, 406
  else:
    return invalid_msg, 400

@app.route('/status')
def log():
  global serial_display_pixel
  serial_display_pixel += 1
  if serial_display_pixel >= (width * height):
    uh.clear()
    uh.show()
    serial_display_pixel = 0

  msg = request.args.get('msg', default='critical', type=str)
  if msg == 'info':
    r , g, b = 0, 0, 255
  elif msg == 'warn':
    r, g, b = 255, 255, 0
  elif msg == 'error':
    r, g, b = 255, 165, 0
  else:
    r, g, b = 255, 0, 0

  x = serial_display_pixel % 8
  y = int(serial_display_pixel / 8)

  uh.set_pixel(x,y,r,g,b)
  uh.show()

  return "{'result':'Set status as a pixel at (%s,%s)'}" % (x,y), 200

@app.route('/any')
def any():
  x = randint(0, width - 1)
  y = randint(0, height - 1)
  r, g, b = to_rgb(random())
  uh.set_pixel(x,y,r,g,b)
  uh.show()
  return "{'result':'Set a random pixel'}", 200

@app.route('/clear')
def clear():
  uh.clear()
  uh.show()
  return "{'result':'Cleared the display'}", 200

app.run(debug=False, host=hostname, port=4000)
