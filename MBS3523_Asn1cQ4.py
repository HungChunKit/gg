import cv2

print(cv2.__version__)

faceCascade = cv2.CascadeClassifier('Resources/haarcascade_frontalface_default.xml')

capture = cv2.VideoCapture('Resources/IU-edited.mp4')
capture = cv2.VideoCapture(0)
capture.set(3,640)
capture.set(4,480)

font = cv2.FONT_HERSHEY_PLAIN

while True:
    success, img = capture.read()

    cv2.putText(img, "MBS3523 Assignment 1C - Q4 Name: HUNG CHUN KIT PETER", (40, 20), cv2.FONT_HERSHEY_PLAIN, 1,
                (221, 209, 234), 2)

    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    imgGray = cv2.cvtColor(imgGray, cv2.COLOR_GRAY2BGR)

    faces = faceCascade.detectMultiScale(imgGray, 1.2, 10)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        roiImg = img[y:y + h, x:x + w].copy()
        imgGray[y:y + h, x:x + w]=roiImg

    cv2.imshow('Frame', imgGray)
    cv2.moveWindow('Frame', 100,20)
    if cv2.waitKey(1) == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()
