#importing required libraries
import numpy as np
import cv2

cap = cv2.VideoCapture(0)           #choosing device to initialize video capturing

while True:
    ret, frame = cap.read()         #starting capturing frame by frame
    
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)  #making a hsv frame for mask
    
    #For this example code, orange color has been used for masking the frame
    lower_bound = np.array([10,100,20])     #enter lower bound of your desired color
    upper_bound = np.array([25,255,255])   #enter upper bound of your desired color
    
    mask = cv2.inRange(hsv_frame, lower_bound, upper_bound) #making a masked frame
    final_frame = cv2.bitwise_and(frame, frame, mask=mask)
    
    #Displaying the frames
    cv2.imshow('Masked Frame', final_frame)    
    cv2.imshow('Normal Frame', frame)
    
    #Specifying exit key, In this case it is the key 'q'
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

