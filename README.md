## Team Members
Alex Frederic
Peyton Crawford

## Instructions for Compilation/Execution
First, install the RPi camera into the "CAMERA" port of the RPI 4B using the ribbon connector. Ensure the computer and the RPi are on the same local network and SSH into the RPI.
Ensure you have NodeJS and NPM installed on your machine and enter the frontend/ directory. If you haven't already, run "npm install" to ensure you have all React dependencies installed. Also make sure to download the requirements.txt (opencv and ultralytics are big).
Then, run the flaskServer.py program using the latest version of Python3.
Then, run the computerListen.py program using the same version of Python3. This will connect to flaskServer.py, so it needs to be run after it.
Wait a moment for the "Enter the Computer address to connect to: " input prompt to appear in the terminal. Then, input the IP address of the computer that you are running this program from.
Then, on your RPi, run the piWatch.py program using the same version of Python3. This program connects to computerListen.py, so it needs to be run after.
Wait a moment for the "Enter the Computer address to connect to: " input prompt to appear in the terminal, and enter the same IP address as the one you entered in the previous input prompt.
The RPi will now begin taking photos at regular 5 second intervals, so mount/point the camera where on the area you want to monitor.
Ensure you are in the PiWatch Discord server at https://discord.gg/HPNQ63Ec6 to receive Discord notifications from PiWatch Bot when a human is detected by computerListen.py.
Then, run "npm run dev" and click the resulting link or go to http://localhost:5173/ to view the frontend webpage.

## Libraries
Python:
picamera
socket
flask
time
os
ultralytics
requests
opencv-python
pathlib
flask-cors
json

React:
bootstrap (CSS)
