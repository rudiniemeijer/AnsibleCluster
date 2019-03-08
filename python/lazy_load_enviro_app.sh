# This script just waits 30 seconds before starting a Flask app
# To ensure that loading from crontab isn't prevented by missing network
echo Lazy loading enviro_app..
sleep 30
python /home/pi/enviro_app.py &

