# Scroll pHAT Clock, sourced from pimoroni.co.uk

# Prepare for use with:
#   sudo apt-get update
#   sudo apt-get install python-scrollphathd 

# run this script with python showclock.py
# and/or crontab @reboot python /home/pi/showclock.py 

import time

import scrollphathd
from scrollphathd.fonts import font5x5

print("Scroll pHAT HD Clock")

# Display a progress bar for seconds, a dot is False
DISPLAY_BAR = False

# Brightness of the seconds bar and numbers
BRIGHTNESS = 0.4

while True:
    scrollphathd.clear()

    # Grab the "seconds" component of the current time
    # and convert it to a range from 0.0 to 1.0
    float_sec = (time.time() % 60) / 59.0

    # Multiply our range by 15 to spread the current
    # number of seconds over 15 pixels
    seconds_progress = float_sec * 15

    if DISPLAY_BAR:
        # Step through 15 pixels to draw the seconds bar
        for y in range(15):
            # For each pixel, we figure out its brightness by
            # seeing how much of "seconds_progress" is left to draw
            # If it's greater than 1 (full brightness) then we just display 1.
            current_pixel = min(seconds_progress, 1)

            # Multiply the pixel brightness (0.0 to 1.0) by our global brightness value
            scrollphathd.set_pixel(y + 1, 6, current_pixel * BRIGHTNESS)

            # Subtract 1 now we've drawn that pixel
            seconds_progress -= 1

            # If we reach or pass 0, there are no more pixels left to draw
            if seconds_progress <= 0:
                break
    else:
        # Just display a simple dot
        scrollphathd.set_pixel(int(seconds_progress), 6, BRIGHTNESS)

    # Display the time (HH:MM) in a 5x5 pixel font
    scrollphathd.write_string(
        time.strftime("%H:%M"),
        x=0, # Align to the left of the buffer
        y=0, # Align to the top of the buffer
        font=font5x5, # Use the font5x5 font we imported above
        brightness=BRIGHTNESS # Use our global brightness value
    )

    if int(time.time()) % 2 == 0:
        scrollphathd.clear_rect(8, 0, 1, 5)

    scrollphathd.show()
    time.sleep(0.3)


