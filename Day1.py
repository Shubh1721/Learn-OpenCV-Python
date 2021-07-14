import cv2
# 1.1
# print("Succesfully imported!!")

# 1.2 Image reading

# img = cv2.imread("Lec.png") # image reading path
# cv2.imshow("image", img) # image = window title, img = above object(file)
# cv2.waitKey(0)  # without this img screen will disappear in a moment
# # waitkey(0) me 0=infinite time, baki kuch b dalo sb milisecond me honge

# 1.3 Video accessing 

# cap = cv2.VideoCapture("Intro.mp4")
# while True:
#     success, img = cap.read()
#     cv2.imshow("Video",img)
#     # on pressing 'q' quit from video 
#     if cv2.waitKey(1) & 0xff == ord('q'):
#         break

# 1.4 Camera capturing 

# 0 = inbuilt camera, 1 = ext. Camera 
# cap = cv2.VideoCapture(0)
# cap.set(3,680)  # id = 3, width = 680
# cap.set(3,400)  # id = 4, aur height = 400
# cap.set(10, 100)  # id = 10 for bightness = 100
# cap.set()

# while True:
#     success, img = cap.read()   # reading frames 
#     cv2.imshow("Video",img)     # and showing on screen
#     if cv2.waitKey(1) & 0xff == ord('q'):   
#         break


# 2.1 converting image in different scale
# img = cv2.imread("Lec.png")
# 2.1.1 cv2 me color convention RGB na hokar BGR hota hai
# isliye color convert krne ke liye BG to any krte hai 
# grayImagae = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)    # convert color to gray
# cv2.imshow("Gray Image",grayImagae)
# hlsImagae = cv2.cvtColor(img,cv2.COLOR_BGR2HLS)    # convert color to hls
# cv2.imshow("HLS Image",hlsImagae)

# 2.1.2
# blurImg = cv2.GaussianBlur(img,(7,7),0) # src, kernel Size, sigmaX(deviation)
# cv2.imshow("Blur Image",blurImg)
# # compare above and below image 
# cv2.imshow("Image",img)

# 2.1.3 edge detecter
# iske  liye hm canny ka use krte hai
# cannyImg = cv2.Canny(img,100,100) # as value increases edge detection decreases
# cannyImg2 = cv2.Canny(img,200,200) 
# cv2.imshow("Canny Image",cannyImg)
# cv2.imshow("Canny2 Image",cannyImg2)

# # 2.1.4 Image dilation 
# # iska use hm edge ko moti krne ke liye krte h
# # jo img hme canny se mili hai uska krke dekhe
# # iske liye matrix ki jrurat pdti hai jo hme 'numpy' se lena h
# # isliye hm ise skip kr rhe hai abhi ke liye  
# imgDilate = cv2.dilate(img,)


# 3.1 Image Resize

img = cv2.imread("Lec.png")
# to know current width,height,scale(3 for BGR)
print(img.shape) # width = 712,height = 1266, 
imgResize = cv2.resize(img, (700,400))
# ******** OpenCV me hmesha is tarah (width, height) hote h
# baki me phle height phir width
# cv2.imshow("Image",img)
cv2.imshow("Resized img", imgResize)
print(imgResize.shape)
# 3.2 Crop the Image
# isme X-axis rightSide me and Y-axis down side me
# resize krne k liye array ke model me cut krte h
croped = imgResize[0:200, 100:300] # output se smje

cv2.imshow("Resized img", imgResize)
cv2.imshow("Cropped img", croped)


cv2.waitKey(0) # wait for 4 second, 0 for infinite time