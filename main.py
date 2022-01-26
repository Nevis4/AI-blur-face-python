import cv2


capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
faceCascade = cv2.CascadeClassifier(
    '/Users/przemyslawmalara/programowanie/pyton/Machine_Learning/Open_CV/haarcascades/haarcascade_frontalface_default.xml') # put your path to classifier
while True:
    _, frame = capture.read() # the function passes two values. The first is the return value and the second is the image

    greyscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        greyscale, scaleFactor=1.2, minNeighbors=5, minSize=(50, 50)
    )

    for x, y, face_width, face_height in faces:

        # cv2.rectangle(frame, (x,y), (x+face_width, y+face_height), (255,0,0),5) # make rectangle

        blur = cv2.blur(frame[y:y + face_height, x:x + face_width], ksize=(50, 50)) # make blur
        frame[y:y + face_height, x:x + face_width] = blur

    cv2.imshow('frame', frame)
    cv2.imshow('grey', greyscale)

    key = cv2.waitKey(50)
    if key == 27:
        break

capture.release() # function to free a certain amount of memory
