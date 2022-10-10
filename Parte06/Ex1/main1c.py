#!/usr/bin/env python
# --------------------------------------------------
# Paint
# Filipe Gonçalves, 98083
# PSR, Setember 2022.
# --------------------------------------------------

import cv2
import numpy as np


blank_image = np.ones((600, 400, 3)) * 255
blank_image = blank_image.astype(np.uint8)
color = (255, 0, 0)
selected = False

def mouse_handler(event, x, y, flags, params):
    global selected
    global color

    if event == cv2.EVENT_MOUSEMOVE and selected:
        blank_image[y, x] = color

    if event == cv2.EVENT_LBUTTONUP:
        selected = True if not selected else False


def main():

    global color, blank_image

    cv2.namedWindow("Blank")
    cv2.setMouseCallback("Blank", mouse_handler)

    while True:

        cv2.imshow("Blank", blank_image)

        key = cv2.waitKey(20)

        if key == 27:
            break
        
        if key != -1:
            print(f"Key Pressed {key}")

        if key == ord("r"):
            print("Color changed to RED")
            color = (0, 0, 255)

        if key == ord("b"):
            print("Color changed to BLUE")
            color = (255, 0, 0)

        if key == ord("g"):
            print("Color changed to GREEN")
            color = (0, 255, 0)


    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
