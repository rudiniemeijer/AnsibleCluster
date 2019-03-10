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

@app.route('/showpixel')
def showpixel():
  x = request.args.get('x', default=None, type=int)
  y = request.args.get('y', default=None, type=int)
  hue = request.args.get('hue', default=None, type=float)
  r = request.args.get('r', default=None, type=int)
  g = request.args.get('g', default=None, type=int)
  b = request.args.get('b', default=None, type=int)
  

  if sensor_value is not None:
    data_set = {'value':sensor_value}
    return str(data_set), 200
  else:
    return "{'usage':'http://%s/showpixel?x=[0..15]&y=[0..3]&sensor=temperature|pressure|color|light|analog|compass|accelerometer'}" % hostname, 400

app.run(debug=False, host=hostname, port=4000)
