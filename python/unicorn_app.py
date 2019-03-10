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

  if (x is not None) and (y is not None) and (hue is not None):
    uh.set_pixel(x,y,to_rgb(hue))
    uh.show()
    return "", 200
  else:
    return "{'usage':'http://%s/showpixel?x=[0..15]&y=[0..3]&hue=[0..1]'}" % hostname, 400

app.run(debug=False, host=hostname, port=4000)
