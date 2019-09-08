# This script just waits 30 seconds before starting a Flask app
# To ensure that loading from crontab isn't prevented by missing network

# Put this in the crontab as @reboot /home/<user>/lazy_load_enviro_app.sh

echo Lazy loading enviro_app..
sleep 30
python /home/pi/enviro_app.py &

