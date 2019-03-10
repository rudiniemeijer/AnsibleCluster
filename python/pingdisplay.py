# Prepare for use with:
# sudo apt-get update
# sudo apt-get install pip
# sudo pip install unicornhat
# run this script with sudo python pingdisplay.py

# import the Pimoroni Unicorn library
import unicornhat as uh

# import other utilities
import os
import time

# Specify that the pHAT is used
uh.set_layout(uh.PHAT)

# Set brightness to an acceptable level
uh.brightness(0.5)

def set_node_pixel(node_number, status):
  x = node_number % 4 # 0..3
  y = int(node_number / 4) # 0..3
  if status == "present":
    uh.set_pixel(x, y, 0, 255, 0)
  elif status == "absent":
    uh.set_pixel(x, y, 255, 0, 0)
  uh.show()

def set_other_device_pixel(device_number, status):
  x = (device_number % 4) + 4 # 4..7
  y = int(device_number / 4) # 0..3
  if status == "present":
    uh.set_pixel(x, y, 0, 0, 255)
  elif status == "absent":
    uh.set_pixel(x, y, 255, 0, 0)
  uh.show()

clusterhat_nodes = ['p11', 'p12', 'p13', 'p14', 'p21', 'p22', 'p23', 'p24', 'p31', 'p32', 'p33', 'p34', 'p41', 'p42', 'p43', 'p44']
other_devices = ['ttn-gateway', 'www.retro-lab.nl', 'www.softwaretestjezelf.nl', 'www.testconsultancy.nl', 'www.informus.nl', 'scrollphatpi']

print("Scanning ClusterHAT nodes P11..P44 and other devices")
while True:
  current_node = 0
  for node in clusterhat_nodes:
    response = os.system("ping -q -c 1 " + node + " > /dev/null")

    if response == 0:
      set_node_pixel(current_node, "present")
    else:
      set_node_pixel(current_node, "absent")
    current_node += 1

  current_device = 0
  for device in other_devices:
    response = os.system("ping -q -c 1 " + device + " > /dev/null")

    if response == 0:
      set_other_device_pixel(current_device, "present")
    else:
      set_other_device_pixel(current_device, "absent")
    current_device += 1

  time.sleep(10)
