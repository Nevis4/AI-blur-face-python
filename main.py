import cv2

capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while True:
    _, frame = capture.read()
    cv2.imshow('frame', frame)

    key = cv2.waitKey(50)
    if key == 27:
        break

capture.release()