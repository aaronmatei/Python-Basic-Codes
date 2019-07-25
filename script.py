import cv2

cv2.CascadeClassifier("1.2 haarcascade_frontalface_default.xml")
ipm_img = cv2.VideoCapture("elon.jpg")

res, img = ipm_img.read()
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = detect.detectMultiscale(gray, 1.3, 5)

cv2.imShow("Elon Image", img)