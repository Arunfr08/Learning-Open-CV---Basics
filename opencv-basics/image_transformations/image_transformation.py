import cv2 as cv
import numpy as np

img = cv.imread('opencv/park.png')
cv.imshow('Original image', img)

# 1. Translation (to move image up, down, right, left according to the x-axis and y-axis or combination of both)
# -x => left, -y => up , x => right, y => down
def trans(img, x, y):
    trans_matrix = np.float32([[1,0,x],[0,1,y]])
    dimension = (img.shape[1],img.shape[0])
    return cv.warpAffine(img,trans_matrix,dimension)

trans_img = trans(img, -150, 125)
cv.imshow('Translated Image', trans_img)

# 2. Rotation 
def rotate(img, angle, rotation_pt = None):
    (height, width) = img.shape[:2]
    
    if rotation_pt is None:
        rotation_pt = (width//2, height//2) # floor division to get the center of image.
        rotation_Mat = cv.getRotationMatrix2D(rotation_pt, angle, 1.0)
        dimension = (width,height)

        return cv.warpAffine(img, rotation_Mat, dimension)

rotated_img = rotate(img, 45)
cv.imshow('Rotated Image', rotated_img)

# Rotate the rotated image further
double_rotated = rotate(rotated_img, 30)
cv.imshow('Double Rotation', double_rotated)

# 3. Resizing
resize_img = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC) # decides how new pexels values are calculated
cv.imshow('Resized image', resize_img)

# 4. flipping
# flip code [-1 (vertical and horizontal flip), 1 (horizontal flip over y axis), 0 (veritcal flip over x axis)]

flip = cv.flip(img, 0) 
cv.imshow('Flipped image', flip)

# 5. Cropped
crop = img[200:300, 450:650] # 2nd coordinates should be greater then 1st coordinates
cv.imshow('Cropped', crop)

cv.waitKey(0)

# create menu based program on what we learn 

print('Welcome to image transformation.')
print('Which transformation you want to choose??\n')
print('1. Translation\n2. Rotation\n3. Resizing\n4. Cropping\n5. Flipping')



choice = int(input('Enter your choice : '))

if choice == 1:
    location = input('Enter location of image : ')
    img = cv.imread(location)
    
    if img is None:
        exit()

    x = int(input('Enter shift along x axis (positive to right), (negative for left) : '))
    y = int(input('Enter shift along y axis (positive to down), (negative for up) : '))

    trans_mat = np.float32([[1,0,x],[0,1,y]])
    dimension = (img.shape[1], img.shape[0])
    translated = cv.warpAffine(img, trans_mat, dimension)
    cv.imshow('Translated image', translated)
    cv.waitKey(0)

elif choice == 2:
    location = input('Enter location of image : ')
    img = cv.imread(location)
    
    if img is None:
        exit()

    angle = float(input('Enter rotation angle : '))
    (height,width) = img.shape[:2]
    center = (width // 2, height // 2)
    dimension = (width,height)
    rotation_mat = cv.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv.warpAffine(img, rotation_mat, dimension)
    cv.imshow('Rotated image', rotated)
    cv.waitKey(0)


elif choice == 3:
    location = input('Enter location of image : ')
    img = cv.imread(location)
    
    if img is None:
        exit()

    resize_width = int(input('Enter resized Width : '))
    resize_height = int(input('Enter resized height : '))
    resized = cv.resize(img,(resize_width,resize_height), interpolation=cv.INTER_CUBIC)
    cv.imshow('Resized image', resized)
    cv.waitKey(0)

elif choice == 4:
    location = input('Enter location of image : ')
    img = cv.imread(location)
    
    if img is None:
        exit()

    x1 = int(input('Enter x1 coordinate : '))
    y1 = int(input('Enter y1 coordinate : '))
    x2 = int(input('Enter x2 coordinate : '))
    y2 = int(input('Enter y2 coordinate : '))

    if x1 > x2 or y1 > y2:
        print('Error : x2 and y2 should greater than x1 and y1!!')
        exit()

    cropped = img[y1:y2, x1:x2]
    cv.imshow('Cropped image', cropped)
    cv.waitKey(0)

elif choice == 5:
    location = input('Enter location of image : ')
    img = cv.imread(location)
    
    if img is None:
        exit()
    
    flip_code = int(input('Enter flip code (-1 to flip image verti and hori (both), 1 to flip image horizontal, 0 to flip image vertical): '))
    flipped = cv.flip(img, flip_code)
    cv.imshow('Flipped image', flipped)
    cv.waitKey(0)

else:
    print('Error : Enter choice between 1 to 5')