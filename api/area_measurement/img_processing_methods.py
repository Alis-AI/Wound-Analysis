import cv2
import numpy as np
from scipy.spatial import distance as dist

# Purely for measure_area


def midpoint(ptA, ptB):
    return ((ptA[0] + ptB[0]) * 0.5, (ptA[1] + ptB[1]) * 0.5)


def apply_mask(lower_range, upper_range, image):
    # Convert image to hsv file
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    lower_mask = cv2.inRange(hsv, lower_range[0], upper_range[0])
    upper_mask = cv2.inRange(hsv, lower_range[1], upper_range[1])
    mask = cv2.bitwise_or(lower_mask, upper_mask)
    image = cv2.bitwise_and(image, image, mask=mask)
    image[mask > 0] = (255, 255, 255)

    return image


def sharpen(image):
    kernel = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
    return cv2.filter2D(image, -1, kernel)


def blur(image):
    return cv2.GaussianBlur(image, (7, 7), 0)


def measure_area(image_background, contours, sq_ratio):
    areas = []
    for cont in contours:
        cont_area = cv2.contourArea(cont)/sq_ratio
        # if the contour is not sufficiently large, ignore it
        print(cont_area)
        if cont_area < 0.125:
            continue

        areas.append(cont_area)
        cv2.drawContours(image_background, cont, -1, (0, 255, 0), 2)
    return areas
