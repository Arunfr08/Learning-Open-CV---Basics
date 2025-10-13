import cv2 as cv

img = cv.imread('sample.png')
cv.imshow('Original image', img)

def rescaleFrame(frame, scale = 0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimension = (width,height)

    return cv.resize(frame, dimension, interpolation = cv.INTER_AREA)

resized_img = rescaleFrame(img)
cv.imshow('Resized Image', resized_img)

capture = cv.VideoCapture(0)
while True:
    isTrue,frame = capture.read()
    resized_frame = rescaleFrame(frame)
    cv.imshow('Original video', frame)
    cv.imshow('Rescaled Video', resized_frame)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()
