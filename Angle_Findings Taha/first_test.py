import cv2
import math

path = 'test.jpg'
img = cv2.imread(path)
pointList=[]

def mousePoints(event,x,y,flags,params):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),5,(0,0,255),cv2.FILLED)
        pointList.append([x,y])
        print(pointList)
        #print(x,y)


while True:
    cv2.imshow('Image',img)
    cv2.setMouseCallback('Image',mousePoints)

    if cv2.waitKey(1) & 0xFF ==ord('q'):
        pointList=[]
        img = cv2.imread(path)

cv2.waitKey(0)
