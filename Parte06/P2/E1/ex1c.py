#!/usr/bin/python3
# -------------------------
# @Time      : $ {DATE} $ {TIME}
# @Author    : Pedro Carvalho
# -------------------------
import numpy as np
import cv2

isdown = False
color = (255, 0, 0)  # default blue color

def mouse_paint(event, x, y, flags, params):
    global image
    global window_name
    global isdown
    global color
    if event == cv2.EVENT_MOUSEMOVE:
        if isdown == True:
            image[y, x] = color

    if event == cv2.EVENT_LBUTTONDOWN:
        isdown = True
    if event == cv2.EVENT_LBUTTONUP:
        isdown = False


def main():
    # -----------------------------------
    # Initialize
    # -----------------------------------
    global image, window_name, color
    image = np.ones((400, 600, 3)) * 255  # rows and columns
    window_name = "Paint - Whiteboard"
    cv2.imshow(window_name, image)
    image = image.astype(np.uint8)
    print("Paint - Whiteboard")
    cv2.setMouseCallback(window_name, mouse_paint)

    # -----------------------------------
    # Execution
    # -----------------------------------
    while True:
        # print('doing another iteration of while ...')
        cv2.imshow(window_name, image)
        choice = cv2.waitKey(20)
        if choice != -1:
            print("Tecla pressionada: " + str(choice))
            if choice == ord('R') or choice == ord('r'):
                color = (0, 0, 255)
                print('Red color selected')
            if choice == 71 or choice == 103:
                color = (0, 255, 0)
                print('Green color selected')
            if choice == 66 or choice == 98:
                color = (255, 0, 0)
                print('Blue color selected')
            if choice == 83 or choice == 115:
                break


if __name__ == '__main__':
    main()
