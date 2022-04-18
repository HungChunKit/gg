import cv2
print(cv2.__version__)


cam = cv2.VideoCapture(0)

cam.set(3, 640)
cam.set(4, 480)

x, y = 300, 200
dx, dy = 10, -6

while True:
    success , frame = cam.read()

    cv2.putText(frame, "MBS3523 Assignment 1b - Q3 Name: HUNG CHUN KIT PETER", (40, 20), cv2.FONT_HERSHEY_PLAIN, 1, (221, 209, 234), 2)
    cv2.rectangle(frame, (x, y), (x+80, y+80), (255, 255, 255), 2)
    x += dx
    if x >= 560 or x <= 0:
        dx *= (-1)

    y += dy
    if y >= 400 or y <= 0:
        dy *= (-1)

    cv2.imshow('MBS3523', frame)
    if cv2.waitKey(5) & 0xff == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
