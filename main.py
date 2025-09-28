#import modules 
import cv2
import dlib
import time
import serial
from scipy.spatial import distance as dist

# Connect to Arduino
arduino = serial.Serial('COM8', 9600)  # Replace COM3 with your Arduino port
time.sleep(2)  # Wait for Arduino to initialize

# Drowsiness detection function
def eye_aspect_ratio(eye):
    A = dist.euclidean(eye[1], eye[5])
    B = dist.euclidean(eye[2], eye[4])
    C = dist.euclidean(eye[0], eye[3])
    ear = (A + B) / (2.0 * C)
    return ear

EYE_AR_THRESH = 0.25
EYE_AR_CONSEC_FRAMES = 20
COUNTER = 0

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')  # Download this model

(lStart, lEnd) = (42, 48)
(rStart, rEnd) = (36, 42)

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    rects = detector(gray, 0)

    for rect in rects:
        shape = predictor(gray, rect)
        shape = [(shape.part(i).x, shape.part(i).y) for i in range(68)]
        
        leftEye = shape[lStart:lEnd]
        rightEye = shape[rStart:rEnd]
        
        leftEAR = eye_aspect_ratio(leftEye)
        rightEAR = eye_aspect_ratio(rightEye)
        ear = (leftEAR + rightEAR) / 2.0
        
        if ear < EYE_AR_THRESH:
            COUNTER += 1
            if COUNTER >= EYE_AR_CONSEC_FRAMES:
                print("Drowsiness Detected!")
                arduino.write(b'1')  # Send signal to Arduino
        else:
            COUNTER = 0

    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()