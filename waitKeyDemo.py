import cv2

cv2.namedWindow('image')
#camera.start_preview()

while True:
    #wait a keyboard pressing
    key_code = cv2.waitKey(0)#wait for a key,and the '0' means no time limit

    if key_code != -1:
        #print('key {} pressed!!! value={}'.format(chr(key_code), key_code))
        if chr(key_code) == 'q':#press q to quit
            print('Quit')
            break

        elif chr(key_code) == 'p':
            print('Taken a picture in /home/pi/Desktop/camera...')
            #camera.capture()

        elif chr(key_code) == 's':
            print('Start recording...(press t to stop) ')
            #camera.start_recording()

        elif chr(key_code) == 't':
            print('Stop recording...(the video have been saved in /home/pi/Desktop/camera)...')
            #camera.stop_recording()
            
            
   #if you want to use the waiting tips
   #else:
        #no keyboard pressing
       # print('no keyboard pressing,wait 1s')


#camera.stop_preview()
cv2.destroyWindow('image')
