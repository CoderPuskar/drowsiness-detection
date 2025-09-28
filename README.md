# drowsiness-detection
This project detects driver drowsiness using OpenCV, dlib, and Arduino. It monitors the eye aspect ratio (EAR) in real-time to check if the driver is falling asleep. If drowsiness is detected, the Arduino can trigger an buzzer.
## Features
Eye aspect ratio (EAR) calculation
Real-time face and eye detection using dlib
Arduino integration for alarm system
Adjustable thresholds for sensitivity
## Requirements
Python 3.x
OpenCV
dlib
scipy
Arduino with Serial communication
## How to Run
1. Clone this repository:
git clone https://github.com/CoderPuskar/drowsiness-detection.git
cd your-repo

2. Install dependencies:
pip install opencv-python dlib scipy pyserial

3. Connect Arduino and update the COM port in main.py.
4. Run the program:
python main.py

## Future Improvements
Add a GUI dashboard for monitoring
Collect eye blink statistics
I use threshold you can modify with ML or deep learning models 