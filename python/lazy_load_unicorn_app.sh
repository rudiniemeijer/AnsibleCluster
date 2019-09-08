# This script just waits 30 seconds before starting a Flask app
# To ensure that loading from crontab isn't prevented by missing network

# Put this in the crontab as @reboot /home/<user>/lazy_load_unicorn_app.sh

echo Lazy loading unicorn_app..
sleep 30
python /home/pi/unicorn_app.py &
