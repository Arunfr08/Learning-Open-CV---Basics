import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8')
cv.imshow('Blank img', blank)

# 1. To paint image a certain color
blank[200:300 , 300:550] = 0,255,0
cv.imshow('Painted img', blank)

# 2. Draw a rectangle
cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2),(0,255,0),2, cv.LINE_AA)
cv.imshow('Rectangle', blank)

# 3. Draw a circle
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2),50, (255,0,0), -1, cv.LINE_AA)
cv.imshow('Circles', blank)

# 4. draw a line
cv.line(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,0,200), 3)
cv.imshow('Lines', blank)

#  To write text on image
cv.putText(blank, 'Hello World', (100,250), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), 2, cv.LINE_AA)
cv.imshow('Text', blank)

cv.waitKey(0)




# create a program with what we have learn above

print('Welcome to draw shape program!!')
img = np.zeros((500,500,3), dtype = 'uint8')

print('Create : \n1. Simple line \n2. Circle \n3. Rectangle')

choice = int(input('Select option : '))

if choice == 1:
    s_pt1 = int(input('Enter pt1 : '))
    s_pt2 = int(input('Enter pt2 : '))
    e_pt1 = int(input('Enter end pt1 : '))
    e_pt2 = int(input('Enter end pt2 : '))
    cv.line(img,(s_pt1,s_pt2), (e_pt1,e_pt2), (0,0,250), 2, cv.LINE_AA)
    cv.imshow('Line Image', img)
    cv.waitKey(0)

elif choice == 2:
    radius = int(input('Enter radius : '))
    pt1 = int(input('Enter center pt1 : '))
    pt2 = int(input('Enter center pt2 : '))
    cv.circle(img,(pt1,pt2), radius, (250,0,0), 3, cv.LINE_AA)
    cv.imshow('Circle Image', img)
    cv.waitKey(0)

else:
    s_pt1 = int(input('Enter st pt1 : '))
    s_pt2 = int(input('Enter st pt2 : '))
    e_pt1 = int(input('Enter end pt1 : '))
    e_pt2 = int(input('Enter end pt2 : '))
    cv.rectangle(img,(s_pt1,s_pt2),(e_pt1,e_pt2),(0,250,0), 3,cv.LINE_AA)
    cv.imshow('Rectangle', img)
    cv.waitKey(0)

