# Prepare for use with:
# sudo apt-get install python-envirophat # Python 2
# sudo apt-get install python3-envirophat # Python 3
# pip install flask

# run this script with python enviro_app.py


from flask import jsonify
from envirophat import weather, leds, light, motion, analog
import socket # Used to retrieve hostname
from flask import Flask, request # Flask microservice

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
    return jsonify(data_set), 200
  else:
    return "{'usage':'http://%s/measure?sensor=temperature|pressure|color|light|analog|compass|accelerometer'}" % hostname, 400

app.run(debug=False, host=hostname, port=4000)