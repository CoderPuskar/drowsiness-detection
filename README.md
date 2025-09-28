# drowsiness-detection
This project detects driver drowsiness using OpenCV, dlib, and Arduino. It monitors the eye aspect ratio (EAR) in real-time to check if the driver is falling asleep. If drowsiness is detected, the Arduino can trigger an buzzer.
## Features </br>
Eye aspect ratio (EAR) calculation </br>
Real-time face and eye detection using dlib</br>
Arduino integration for alarm system</br>
Adjustable thresholds for sensitivity</br>
## Requirements </br>
Python 3.x </br>
OpenCV </br>
dlib </br>
scipy </br>
Arduino with Serial communication </br>
## How to Run </br>
1. Clone this repository:
git clone https://github.com/CoderPuskar/drowsiness-detection.git
cd your-repo

2. Install dependencies:
pip install opencv-python dlib scipy pyserial

3. Connect Arduino and update the COM port in main.py.
4. Run the program:
python main.py

## Future Improvements </br>
Add a GUI dashboard for monitoring</br>
Collect eye blink statistics </br>
I use threshold you can modify with ML or deep learning models </br>