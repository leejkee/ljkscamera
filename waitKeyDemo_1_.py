from picamera import PiCamera
from time import sleep

import cv2

#if you want to open a new window
cv2.namedWindow('window')
camera = PiCamera()
camera.start_preview()
while True:
    key_code = cv2.waitKey(0)#wait for a key,and the '0' means no time limit

    if key_code != -1:
        if chr(key_code) == 'q':#press q to quit
            print('Quit')
            break

        elif chr(key_code) == 'p':
            print('Taken a picture in /home/pi/Desktop/camera...')
            camera.capture('/home/pi/Desktop/image_demo1.jpg')

        elif chr(key_code) == 's':
            camera.start_recording('/home/pi/Desktop/video1.h264')
            sleep(10)
            camera.stop_recording()
camera.stop_preview()
cv2.destroyWindow('window')
