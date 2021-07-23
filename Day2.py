import cv2
import numpy as mp

# img = cv2.imread("Lec.png")
# kernel = mp.ones((5,5), mp.uint8) # uint8 gives 0 to 2^8 = 255 color value

# cannyImg = cv2.Canny(img,100,100) # as value increases edge detection decreases
# cv2.imshow("Canny Image",cannyImg)
# imgDilate = cv2.dilate(cannyImg,kernel, iterations=1)
# # iterations se edge thickness increase hoti hai
# cv2.imshow("Dilation Img",imgDilate)

# 4. Draw rectangle, put text on images etc
# 4.1
# 0= for black and 1= white
# img = mp.zeros((512,512 , 3),mp.uint8)
# # if 3 you will not write then you will get error 
# # 3 ka mtlb kauns channel for our case this is 
# print(img.shape)    # to check dimension
# # cv2.imshow("Numpy Image", img)

# # Give color functionality
# img[200:300, 100:300] = 0,240,240 # to color full use img[:] = 255,0,0 BGR
# cv2.imshow("Colored Img",img)

# # Draw a line on colored part
# cv2.line(img,(100,300),(300,200),(0,0,250),4) # put arrow on line to know more
# cv2.imshow("Colored Img",img)

# # Diagonal Line of img 
# cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(255,0,250),4)
# cv2.imshow("Colored Img",img)

# # Draw Rectangle -- Put Arrow on rectangle to know parameters-veryEasy
# cv2.rectangle(img,(200,0),(350,100),(255,255,0),cv2.FILLED) # to fill the rectangle
# # write cv2.FILLED in place of thickness

# # Draw Circle -- to fill color same as rectangle
# cv2.circle(img,(200,150),25,(165,160,255),6)

# # Write Text On img
# cv2.putText(img,"Hello Dosto!!",(20,30),cv2.FONT_HERSHEY_COMPLEX,1,(100,100,255),2 )
# # scale value may be integer as well as float like 0.5/1/1.5/1.25 etc.
# cv2.imshow("Colored Img",img)

# 5 Warp Perspective

# width, height = 300,400
# img = cv2.imread("Lec.png")
# # cv2.imshow("Picture ", img)
# print(img.shape)

# # To know img co-ordinate open img in paint and mark your co-ordinate
# # jis img ko nikalnna ho
# src = mp.float32([[715,150], [1250,140], [715,708], [1266,712]])

# #dest me vh co-ordinate hota hai jis ratio ka hm outcome chahte hai 
# dest = mp.float32([ [0,0], [width,0], [0,height], [width,height] ])

# matrix = cv2.getPerspectiveTransform(src,dest) # src img se perspective cut krke dest me rkhna

# outputImg = cv2.warpPerspective(img, matrix,(width, height))

# cv2.imshow("Original", img)
# cv2.imshow("Warp Perspective", outputImg)

# # 6 Image joining
# img = cv2.imread("Pic.png")

# # Horizontal Image stacking
# horStack = mp.hstack((img,img,img))
# # cv2.imshow("Picture", img)
# cv2.imshow("Horizontal ", horStack)

# # Vertical Image stacking
# verStack = mp.vstack((img,img,img))
# cv2.imshow("Vertical",verStack)

# st = mp.stack((img,img,img),(img,img,img))
# cv2.imshow("Vertical",st)
# Just trying to scale km krne ke liye function
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
    
# 7. Color Detection
path = "Lec.png"

# h_min etc.= 4,173,182,255,153,255 for Lec.png
# just function do nothing
def empty(a):
    pass

# Creating new window Track Bar
cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars",640,240)
cv2.createTrackbar("Hue Min","TrackBars",0,179,empty)    # 0= inital value, 179= Hue Value
# Vaise to Hue ki max value 360 hoti hai but OpenCV me yh 180 hi hai 

# ab hm kuch aur tarcker bna rhe
cv2.createTrackbar("Hue Min","TrackBars",0,179,empty)
cv2.createTrackbar("Hue Max","TrackBars",179,179,empty)
cv2.createTrackbar("Sat Min","TrackBars",0,255,empty)
cv2.createTrackbar("Sat Max","TrackBars",255,255,empty)
cv2.createTrackbar("Val Min","TrackBars",0,255,empty)
cv2.createTrackbar("Val Max","TrackBars",0,255,empty)

# Sat = saturation, Val = Value 

# Ab hmko trackbar se value read krna h
# ki jisse hm value apply kr ske
while True:

    img = cv2.imread(path)
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HLS)
    h_min = cv2.getTrackbarPos("Hue Min","TrackBars") #spelling should be exact same
    h_max = cv2.getTrackbarPos("Hue Max","TrackBars") #spelling should be exact same
    s_min = cv2.getTrackbarPos("Sat Min","TrackBars") #spelling should be exact same
    s_max = cv2.getTrackbarPos("Sat Max","TrackBars") #spelling should be exact same
    v_min = cv2.getTrackbarPos("Val Min","TrackBars") #spelling should be exact same
    v_max = cv2.getTrackbarPos("Val Max","TrackBars") #spelling should be exact same
    print(h_min, h_max, s_min, s_max, v_min,v_max)
    lower = mp.array([h_min, s_min, v_min])
    upper = mp.array([h_max, s_max, v_max])
    # Mask se hme black-n-white image mil jayegi on changing tracker
    #4,173,182,255,153,255 for Lec.png for good view
    # 0 179 119 255 0 255 Best output
    mask = cv2.inRange(imgHSV, lower,upper)
    # mask img se color img kaise bnaye?
    imgResultMask = cv2.bitwise_and(img, img, mask = mask)
    
    # cv2.imshow("Original",img)
    # cv2.imshow("HSV image",imgHSV)
    # cv2.imshow("Mask image",mask)
    # cv2.imshow("Result image",imgResultMask)

    # char images window se play se axxa hai ki inki stacking kr le
    imgStack = stackImages(0.6, ([img, imgHSV],[mask,imgResultMask]))
    cv2.imshow("Full Window1",imgStack)
    
    
    cv2.waitKey(1)
