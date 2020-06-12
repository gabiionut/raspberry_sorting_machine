import numpy as np
import cv2
import argparse

from sobel import sobel_edge_detection
from gaussian_smoothing import gaussian_blur
from get_contours import getContours
from resize import resize
from hysteresis import hysteresis
from non_max_suppression import  non_max_suppression
from threshold import threshold

import matplotlib.pyplot as plt

def canny(image):
    blurred_image = gaussian_blur(image, kernel_size=9)

    edge_filter = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])

    gradient_magnitude, gradient_direction = sobel_edge_detection(blurred_image, edge_filter)

    new_image = non_max_suppression(gradient_magnitude, gradient_direction)

    weak = 50

    new_image = threshold(new_image, 5, 20, weak)

    new_image = hysteresis(new_image, weak)

    new_image = new_image.astype(np.uint8)
    kernel = np.ones((5, 5))
    img_dil = cv2.dilate(new_image, kernel, iterations=1)

    form = getContours(img_dil, image, image)

    return form

