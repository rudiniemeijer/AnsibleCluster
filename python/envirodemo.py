# Prepare for use with:
# sudo apt-get update
# sudo apt-get install pip
# sudo apt-get install python-envirophat # Python 2
# sudo apt-get install python3-envirophat # Python 3
# run this script with sudo python envirodemo.py

# import the Pimoroni Unicorn library
from envirophat import weather, leds, light, motion, analog

# import other utilities
import time

# Read the current temperature
temperature = weather.temperature()

# Read the current color
leds.on()
color = light.rgb()
leds.off()
print(color)



