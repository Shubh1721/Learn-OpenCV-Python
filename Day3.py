import cv2
import numpy as mp

# From 6
def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = mp.zeros((height, width, 3), mp.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = mp.hstack(imgArray[x])
        ver = mp.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= mp.hstack(imgArray)
        ver = hor
    return ver

def getContour(img):
    # cv2.RETR_EXTERNAL = yh extreme contour retrieve kr ke deta h
    # cv2.CHAIN_APPROX_NONE = to get all the contour refer google for more info
    contour, hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contour:
        area = cv2.contourArea(cnt)    # For each contour we are going to find area first
        print(area)
        # cv2.drawContours(imgContour, cnt, -1,(255,0,0),4)   # -1 for complete/all contour
        if area > 500: # agar area 500 se jyada ho to hi contour outline kre
            cv2.drawContours(imgContour, cnt, -1,(255,0,0),4) # jisse koi error(noice) km ho
            # To approximate the cornor of our shape
            parameter = cv2.arcLength(cnt,True) # True= all our shape are closed
            # print(parameter)
            # To write the corner
            # 0.02*parameter= Resolution(you can nplay with it)
            approx = cv2.approxPolyDP(cnt,0.02*parameter, True) 
            # print(approx) # to print corner
            print(len(approx)) # To print number of corner

            # To detect the object Corner
            objCorner = len(approx)
            # Now we are going to create the bounding box around the detected object
            # To draw the bounding box around the object what will be the x,y,width,height
            x, y, w, h = cv2.boundingRect(approx)
            cv2.rectangle(imgContour, (x,y),(x+w, y+h),(0,0,255),3) 
            # From the bounding box We can find center,area, 
            # Ab hm chahte hai ki triangnle pr triangle, circle pr circle likh jaye etc
            if objCorner == 3: objType = "Tri"
            elif objCorner == 4:
                aspectRatio = w//float(h)
                if aspectRatio>0.95 and aspectRatio<1.05: # just taking 5% deviation
                    objType = "Square"
                else:
                    objType = "Rectangle"
            elif objCorner>4: objType = "Circle"
            else: objType = "NONE"
            cv2.putText(imgContour,objType, 
                        (x+(w//2)-10, y+(h//2)-10),cv2.FONT_HERSHEY_COMPLEX,
                        0.7,(0,0,0), 3)
            


             




# 8. Contour/Shape Detection

img = cv2.imread("shapes.png")
# cv2.imshow("Original",img)

# Make copy of original img ki koi problem nna ho
imgContour = img.copy()

imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7,7), 1)
imgCanny = cv2.Canny(imgBlur, 50,50)    # as value increases edge detection decreases
imgBlank = mp.zeros_like(img)

getContour(imgCanny)


imgStack = stackImages(0.65, ([img ,imgGray, imgBlur],
                            [imgCanny, imgContour,imgBlank]))
# cv2.imshow("Gray img",imgGray)
cv2.imshow("Blur img",imgStack)


cv2.waitKey(0)



