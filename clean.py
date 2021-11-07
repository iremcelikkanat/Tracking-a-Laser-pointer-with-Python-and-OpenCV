import cv2
import numpy as np


lazer = cv2.VideoCapture(0)

lazer.set(cv2.CAP_PROP_FRAME_WIDTH,640)
lazer.set(cv2.CAP_PROP_FRAME_HEIGHT,480)


def  func(matris):
    say=0
    for ax in range(0,matris.shape[0],1):   
        for bx in range(0,matris.shape[1],1):               
            if (matris[ax][bx]) == 255:
                
                    say=say+1
    return say
                    
                
while (1):


    ret, frame = lazer.read()
    hsvrenkdonusum = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    (thresh, blackAndWhiteFrame) = cv2.threshold(gray, 220, 255, cv2.THRESH_BINARY)


    lower_kırmızı = np.array([160, 100, 255])
    upper_kırmızı = np.array([179, 255, 255])
    maskeleme = cv2.inRange(hsvrenkdonusum, lower_kırmızı, upper_kırmızı)
    (minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(maskeleme)
    print("minimum val:",minVal)
    print("max value",maxVal)


    #cv2.circle(frame, maxLoc, 50, (60, 255, 100), 4, cv2.LINE_AA)
    
    cv2.imwrite("foto.jpg", frame)
    
    maxFrameCorners=[]
    maxBeyazNoktaSayisi=0
    for i in range(0,blackAndWhiteFrame.shape[0],40): #satır
        for j in range(0,blackAndWhiteFrame.shape[1],40): #sutun

            matris=blackAndWhiteFrame[j:40+j,i:40+i]
            beyazNoktaSayisi=func(matris)
            if(beyazNoktaSayisi>=maxBeyazNoktaSayisi):
                maxFrameCorners=[i,j,40+i,40+j]
                maxBeyazNoktaSayisi=beyazNoktaSayisi
            
    
    print("max Beyaz Nokta Sayisi-->",maxBeyazNoktaSayisi)
               
    if cv2.waitKey(1) & 0xFF == ord('q'):    
        break
    cv2.rectangle(frame, (maxFrameCorners[0],maxFrameCorners[1]), (maxFrameCorners[2],maxFrameCorners[3]), (60, 255, 100), 2)
    cv2.imshow('Lazer Takip', frame)
    cv2.imshow('Lazer ', blackAndWhiteFrame)




lazer.release()
cv2.destroyAllWindows()