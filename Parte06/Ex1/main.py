#!/usr/bin/env python
# --------------------------------------------------
# Drawing Circles
# Filipe Gonçalves, 98083
# PSR, Setember 2022.
# --------------------------------------------------

import cv2

image = cv2.imread("/home/filipeg/Desktop/psr_22-23/Parte06/docs/atlascar2_multichannel_thresholded.png", cv2.IMREAD_COLOR)

cv2.namedWindow("Circle")

cv2.circle(image, (int(image.shape[0]/2), int(image.shape[1]/2)), 30, (0, 0, 0), -1)
cv2.putText(image, "PSR", (int(image.shape[0]/2)-15, int(image.shape[1]/2)+5), cv2.FONT_HERSHEY_PLAIN, 1, (255, 255, 255), 1)
cv2.imshow("Circle", image)

cv2.waitKey(0)
cv2.destroyAllWindows()