import cv2
import os
import numpy as np
cap = cv2.VideoCapture("./video.h264")

try :
    if not os.path.exists('data'):
        os.makedirs('data')

except OAError:
    print('error')

currentframe = 0
while True:
    ret, frame = cap.read()
    if ret:
        name = './data/frame' + str(currentframe) + '.jpg'
        print('Creating...'+ name)
        
        cv2.imwrite(name, frame)
        #cv2.imshow('capture', frame)
        currentframe += 1
    else :
        break
    if currentframe >= 24:
        break
cap.release()
cv2.destroyAllWindows()

