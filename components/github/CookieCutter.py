#INITIAL SETUP
#----------------------------------------------------------------
import cv2
from cvzone import HandTrackingModule, overlayPNG
import numpy as np
import os

folderPath = 'Frames'
mylist = os.listdir(folderPath)
graphic = [cv2.imread(f'{folderPath}/{imgPath}')for imgPath in mylist]

intro = graphic[0]
# read frames\img 1 in the intro variable

kill = graphic[1]
# read frames\img 2 in the kill variable

winner = graphic[2]
# read frames\img 3 in the winner variable

cap = cv2.VideoCapture(0)
frameHeight = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
frameWidth = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
#read the camera

detector = HandTrackingModule.HandDetector(maxHands=1,detectionCon=0.77)
#sets the minimum confidence threshold for the detection

#INITILIZING GAME COMPONENTS
#----------------------------------------------------------------
folderPath = 'img'
mylist2 = os.listdir(folderPath)
graphic = [cv2.imread(f'{folderPath}/{imgPath}')for imgPath in mylist2]
sqr_img = graphic[1]
# read img\sqr (1) in the sqr_img variable
mlsa = graphic[0]
# read img\mlsa in the mlsa variable
#INTRO SCREEN WILL STAY UNTIL Q IS PRESSED

cv2.imshow('Squid Game - Cookie Cutter',cv2.resize(intro,(0,0),fx=0.7,fy=0.7))
cv2.waitKey(1)
while True:
     cv2.imshow('Squid Game - Cookie Cutter',cv2.resize(intro,(0,0),fx=0.7,fy=0.7))
     if cv2.waitKey(1) & 0xFF == ord('q'):
        break

maxMove = 6500000
font = cv2.FONT_HERSHEY_PLAIN

showFrame = cv2.resize(sqr_img,(0,0),fx = 0.7,fy = 0.7)
     
 

gameOver = False
NotWon =True
#GAME LOGIC UPTO THE TEAMS
#-----------------------------------------------------------------------------------------
while not gameOver:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # gray = cv2.GaussianBlur(gray, (21, 21), 0)
    ref = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frameDelta = cv2.absdiff(ref, gray)
    thresh = cv2.threshold(frameDelta, 20, 255, cv2.THRESH_BINARY)[1]
    change = np.sum(thresh)
    continue
    if cv2.waitKey(10) & 0xFF == ord('q'):
     break

camShow = cv2.resize(frame, (0, 0), fx=0.4, fy=0.4)

camH, camW = camShow.shape[0], camShow.shape[1]
showFrame[0:camH, -camW:] = camShow
cv2.imshow('Squid Game - Cookie Cutter', showFrame)
        
   
        
#LOSS SCREEN
cap.release()
if NotWon:
    for i in range(10):
         cv2.imshow('Squid Game - Cookie Cutter',cv2.resize(kill,(0,0),fx = 0.7,fy = 0.7))
       #show the loss screen from the kill image read before
    while True:
        cv2.imshow('Squid Game - Cookie Cutter', cv2.resize(kill, (0, 0), fx=0.7, fy=0.7))
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
        #show the loss screen from the kill image read before and end it after we press q

else:
    cv2.imshow('Squid Game - Cookie Cutter', cv2.resize(winner, (0, 0), fx=0.7, fy=0.7))
    cv2.waitKey(125)
#WIN SCREEN
#show the win screen from the winner image read before

    while True:
        cv2.imshow('Squid Game - Cookie Cutter', cv2.resize(winner, (0, 0), fx=0.7, fy=0.7))
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
        #show the win screen from the winner image read before and end it after we press q

#destroy all the windows

    cv2.destroyAllWindows()
