# Prepare for use with:
# pip install unicornhat

# run this script with python unicorn_app.py

# import the Pimoroni Unicorn library
import unicornhat as uh
import time, os
from flask import Flask, request # Flask microservice

# Specify that the pHAT is used (instead of a HAT)
uh.set_layout(uh.PHAT)

# Most important commands
# .brightness(0..1)
# .set_pixel(x=0..15, y=0..3, r, g, b)
# .show()

app = Flask(__name__)
hostname = socket.gethostname()

@app.route('/measure')
def measure():
  leds.on()
  sensor = request.args.get('sensor', default=None, type=str)
  sensor_value = None
  if sensor == 'temperature':
    sensor_value = weather.temperature()
  elif sensor == 'pressure':
    sensor_value = weather.pressure('hPa')
  elif sensor == 'color':
    sensor_value = light.rgb()
  elif sensor == 'light':
    leds.off()
    sensor_value = light.light()
    leds.on()
  elif sensor == "analog":
    sensor_value = analog.read_all()
  elif sensor == 'compass':
    sensor_value = motion.heading()
  elif sensor == 'accelerometer':
    sensor_value = motion.accelerometer()
  else:
    sensor_value = None
  leds.off()

  if sensor_value is not None:
    data_set = {'value':sensor_value}
    return str(data_set), 200
  else:
    return "{'usage':'http://%s/measure?sensor=temperature|pressure|color|light|analog|compass|accelerometer'}" % hostname, 400

app.run(debug=False, host=hostname, port=4000)
