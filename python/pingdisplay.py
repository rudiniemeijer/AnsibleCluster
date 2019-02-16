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

# Set brightness to less dagenrout acceptable level
uh.brightness(0.5)

# Set the appropriate pixel for the node number
# As there are 16 nodes (P11, P12, .. , P43, P44),
# pixels are shown in a 4 x 4 block
# First row is controller1, second row is controller2, etc.
def set_node_pixel(node_number, status):
  x = node_number % 4 # 0..3
  y = int(node_number / 4) # 0..3
  if status == "present":
    uh.set_pixel(x, y, 0, 255, 0)
  elif status == "absent":
    # Should include the concept of 'not seen before',
    # as opposed to 'was there, but gone now'
    uh.set_pixel(x, y, 255, 0, 0)
  uh.show()

clusterhat_nodes = ['p11', 'p12', 'p13', 'p14', 'p21', 'p22', 'p23', 'p24', 'p31', 'p32', 'p33', 'p34', 'p41', 'p42', 'p43', 'p44']

print("Scanning ClusterHAT nodes P11..P44")
while True:
  current_node = 0
  for node in clusterhat_nodes:
    response = os.system("ping -q -c 1 " + node + " > /dev/null")

    if response == 0: # Node was found
      set_node_pixel(current_node, "present")
    else:
      set_node_pixel(current_node, "absent")
    current_node += 1
  time.sleep(10)
