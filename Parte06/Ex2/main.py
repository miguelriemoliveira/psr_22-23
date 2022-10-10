#!/usr/bin/env python
# --------------------------------------------------
# Video Capture
# Filipe Gonçalves, 98083
# PSR, Setember 2022.
# --------------------------------------------------

import cv2

def main():

    capture = cv2.VideoCapture(0)
    window_name = 'A5-Ex2'
    cv2.namedWindow(window_name,cv2.WINDOW_AUTOSIZE)

    while True:

        ret, frame = capture.read()

        k = cv2.waitKey(1)

        if not ret:
            print("failed to grab frame")
            break

        cv2.imshow(window_name, frame)

        if k == ord("q"):
            break

    capture.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()