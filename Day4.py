import cv2
import numpy as mp

# 9 Face Detection
# Face detect krne k liya hm "VIOLA & JONES" ka ek method ka use krenge 
# This one of the oldest method to detect real time face
# Hm kuch faces ko collect krenge to detect the faces
# Positive Face: We collect alots of real faces 
# Negative Face: We will also collect alots of -ive faces which could be anything
# By + & - faces we will train and cascade file that will help us to find right one
# The File will be of xml
# But isme hm system ko train krne nhi ja rhe 
# hm simply already written file ka use krnge 
# OpenCV ne bhut sare cascade file ko de rtakha hai hm usi ka use krenge
# jaise:- haarcascade.xml,  haarcascade_eye_tree_eyeglasses.xml, haarcascade_fontalcatface.xml etc
# 

faceCascade= cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
img = cv2.imread('lena.png')
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(imgGray,1.1,4)

for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)


cv2.imshow("Result", img)
cv2.waitKey(0)






