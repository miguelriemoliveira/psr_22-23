#!/usr/bin/env python
# --------------------------------------------------
# Face Recognition in video capture
# Filipe Gonçalves, 98083
# PSR, Setember 2022.
# --------------------------------------------------

import cv2
import numpy as np

def main():

    # start video cpature
    capture = cv2.VideoCapture(0)

    window_name = 'A5-Ex2'
    cv2.namedWindow(window_name,cv2.WINDOW_AUTOSIZE)

    while True:

        # captura a frame
        ret, frame = capture.read()

        # wait for a key every milisecond
        k = cv2.waitKey(1)

        # if there is no frame
        if not ret:
            print("failed to grab frame")
            break

        # press q to close
        if k == ord("q"):
            break

        # Load the cascade
        face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        # Convert into grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)

        for (x, y, w, h) in faces:
            # paint
            sub_img = frame[y:y+h, x:x+w]

            retval, image_thresholded = cv2.threshold(sub_img, 190, 255, cv2.THRESH_TOZERO_INV)

            frame[y:y+h, x:x+w] = image_thresholded

            # Draw rectangle around the faces
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)

        # show the image
        cv2.imshow(window_name, frame)

    # end the video capture
    capture.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()


