# Prepare for use with:
# pip install unicornhat

# run this script with python unicorn_app.py

# import the Pimoroni Unicorn library
import unicornhat as uh
import time, socket # Used to retrieve hostname
from flask import Flask, request # Flask microservice

# Specify that the pHAT is used (instead of a HAT)
uh.set_layout(uh.PHAT)

# Most important commands
# .brightness(0..1)
# .set_pixel(x=0..15, y=0..3, r, g, b)
# .show()

app = Flask(__name__)
hostname = socket.gethostname()

def to_rgb(hue):
  rgb = {r=0, g=0, b=0}
  
  if hue < (1 / 3):
    rgb.r = 2 - hue * 6
    rgb.g = hue * 6
    rgb.b = 0
  elif hue < (2 / 3):
    rgb.r = 0
    rgb.g = hue * 6
    rgb.b = hue * 6 - 2
  else
    rgb.r = hue * 6 - 4
    rgb.g = 0
    rgb.b = (1 - hue) * 6
  
  if rgb.r > 1:
    rgb.r = 1
  if rgb.g > 1:
    rgb.g = 1
  if rgb.b > 1:
    rgb.b = 1
    
  rgb.r = rgb.r * 255
  rgb.g = rgb.g * 255
  rgb.b = rgb.b * 255
  
  return rgb

@app.route('/showpixel')
def showpixel():
  x = request.args.get('x', default=None, type=int)
  y = request.args.get('y', default=None, type=int)
  hue = request.args.get('hue', default=None, type=float)

  if (x is not None) and (y is not None) and (hue is not None):
    uh.set_pixel(x,y,to_rgb(hue))
    uh.show()
    return "", 200
  else:
    return "{'usage':'http://%s/showpixel?x=[0..15]&y=[0..3]&hue=[0..1]'}" % hostname, 400

app.run(debug=False, host=hostname, port=4000)
