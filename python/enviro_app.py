# Prepare for use with:
# sudo apt-get install python-envirophat # Python 2
# sudo apt-get install python3-envirophat # Python 3
# pip install flask
# run this script with python enviro_app.py

# import the Pimoroni Unicorn library
from envirophat import weather, leds, light, motion, analog

from flask import Flask, request

app = Flask(__name__)
hostname = 'p14'

@app.route('/measure')
def measure():
  leds.on()
  sensor = request.args.get('sensor', default=None, type=str)
  if sensor == 'temperature':
    sensor_value = weather.temperature()
  elif sensor == 'pressure':
    sensor_value = weather.pressure()
  elif sensor == 'color':
    sensor_value = light.rgb()
  elif sensor == 'light':
    sensor_value = light.light()
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
    return str(sensor_value), 200
  else:
    return '''Use: %s/measure?sensor=<i>type</i><br>
where <i>type</i> is one of the following:<br>
- temperature<br>
- pressure<br>
- color<br>
- light<br>
- analog<br>
- compass<br>
- accelerometer''' % hostname, 401

app.run(debug=False, host=hostname, port=4000)
