import cv2
from cvzone.FaceDetectionModule import FaceDetector
import pyfirmata
import numpy as np
import serial
import time

arduino = serial.Serial(port='COM4', baudrate=115200, timeout=.1)
cap = cv2.VideoCapture(0)
#ws, hs = 400,400
cap.set(3, 1280)
cap.set(4, 720)


if not cap.isOpened():
    print("Camera couldn't Access!!!")
    exit()

"""
port = "COM4"
board = pyfirmata.Arduino(port)
servo_pinX = board.get_pin('d:7:s') #pin 9 Arduino
servo_pinY = board.get_pin('d:10:s') #pin 10 Arduino
"""
detector = FaceDetector()
servoPos = [90, 90] # initial servo position

def write_read(x):
    arduino.write(x.encode())
    
    #data = arduino.readline()
    #print(data)
    #return data

def translate(value, leftMin, leftMax, rightMin, rightMax):
    # Figure out how 'wide' each range is
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin

    # Convert the left range into a 0-1 range (float)
    valueScaled = float(value - leftMin) / float(leftSpan)

    # Convert the 0-1 range into a value in the right range.
    return int(rightMin + (valueScaled * rightSpan))

def decimalToBinary(n):
    # converting decimal to binary
    # and removing the prefix(0b)
    return bin(n).replace("0b", "")

while True:
    success, img = cap.read()
    img, bboxs = detector.findFaces(img, draw=False)

    if bboxs:
        #get the coordinate
        fx, fy = bboxs[0]["center"][0], bboxs[0]["center"][1]
        pos = [fx, fy]
        #convert coordinat to servo degree
       
        
        servoX = translate(fx, 0, 1280,0, 180)
        #servo_writeX= decimalToBinary(servoX)
        
        
        
        if servoX < 0:
            servoX = 0
        elif servoX > 180:
            servoX = 180
            
        """
            if servoY < 0:
            servoY = 0
        elif servoY > 180:
            servoY = 180
        """
        """
        servoPos[0] = servoX
        servoPos[1] = servoY
        """
        
        
        
        #print(bytes(str(servoX),'utf-8'))
        
        
    

        #cv2.circle(img, (fx, fy), 80, (0, 0, 255), 2)
        cv2.putText(img, str(pos), (fx+15, fy-15), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2 )
        #cv2.line(img, (0, fy), (ws, fy), (0, 0, 0), 2)  # x line
        #cv2.line(img, (fx, hs), (fx, 0), (0, 0, 0), 2)  # y line
        cv2.circle(img, (fx, fy), 15, (0, 0, 255), cv2.FILLED)
        cv2.putText(img, "face tracking", (850, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3 )
    

    else:
        cv2.putText(img, "no face detected", (880, 50), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 255), 3)
        #cv2.circle(img, (640, 360), 80, (0, 0, 255), 2)
        #cv2.circle(img, (640, 360), 15, (0, 0, 255), cv2.FILLED)
        #cv2.line(img, (0, 360), (ws, 360), (0, 0, 0), 2)  # x line
        #cv2.line(img, (640, hs), (640, 0), (0, 0, 0), 2)  # y line


    cv2.putText(img, f'Servo X: {int(servoPos[0])} deg', (50, 50), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)
    cv2.putText(img, f'Servo Y: {int(servoPos[1])} deg', (50, 100), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)

    """servo_pinX.write(servoPos[0])
    servo_pinY.write(servoPos[1])
    """
    value=write_read(str(fx))
    
    
    
    cv2.imshow("Image", img)
    cv2.waitKey(1)
    

    