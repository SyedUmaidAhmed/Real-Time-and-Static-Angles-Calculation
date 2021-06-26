import cv2
import math

path = 'test.jpg'
img = cv2.imread(path)
pointsList=[]

def mousePoints(event,x,y,flags,params):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),5,(0,0,255),cv2.FILLED)
        pointsList.append([x,y])
        print(pointsList)
        #print(x,y)



def gradient(pt1,pt2):
    return ((pt2[1]-pt1[1])/(pt2[0]-pt1[0]))

def getAngle(pointsList):
    pt1,pt2,pt3=pointsList[-3:]
    m1 = gradient(pt1,pt2)
    m2 = gradient(pt1,pt3)
    angR=math.atan((m2-m1)/(1+(m2*m1)))
    angD = round(math.degrees(angR))
    print(angD)



    
while True:

    if len(pointsList)%3==0 and len(pointsList)!=0:
        getAngle(pointsList)

    
    cv2.imshow('Image',img)
    cv2.setMouseCallback('Image',mousePoints)

    if cv2.waitKey(1) & 0xFF ==ord('q'):
        pointList=[]
        img = cv2.imread(path)

cv2.waitKey(0)
