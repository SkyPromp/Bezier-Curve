import cv2 as cv
import numpy as np


def curve(p0, p1, p2, t):
    x = (1 - t) * (p0[0] * (1 - t) + p1[0] * t) + t * (p1[0] * (1 - t) + p2[0] * t)
    y = (1 - t) * (p0[1] * (1 - t) + p1[1] * t) + t * (p1[1] * (1 - t) + p2[1] * t)

    return x, y


def draw(img, amount, start, middle, end):
    for t in range(0, amount + 1):
        coords = curve(start, middle, end, t / amount)
        if 0 <= round(coords[1]) < img.shape[1] and 0 <= round(coords[0]) < img.shape[0]:
            img[round(coords[1])][round(coords[0])] = 255

    return img


canvas = np.zeros((1001, 1001, 1), dtype="uint8")

amount = 10000  # Amount of dots drawn
x = 100  # Offset x from origin
y = 100  # Offset y from origin
height = 500  # Total height
thickness = 20

alphabet = {"B": [[(thickness + x, y), (thickness + x, height / 2 + y), (thickness + x, height + y)],
                  [(x, y), (thickness / 2 + x, y), (thickness + x, y)],
                  [(x, y), (x, height + y), (x, height + y)],
                  [(x, height + y), (thickness / 2 + x, height + y), (thickness + x, height + y)],
                  [(thickness + x, y), (thickness * 8 + x, (height - thickness / 2) / 4 + y), (thickness + x, (height - thickness / 2) / 2 + y)],
                  [(thickness + x, thickness + y), (thickness * 7 + x, (height - 3 * thickness / 2) / 4 + y), (thickness + x, (height - 2 * thickness) / 2 + y)],
                  [(thickness + x, (height - thickness / 2) / 2 + y), (thickness * 12 + x, (3 * height / 2 + thickness / 2) / 2 + y), (thickness + x, height + y)],
                  [(thickness + x, (height + thickness) / 2 + y), (thickness * 11 + x, (3 * height / 2 + thickness / 2) / 2 + y), (thickness + x, height - thickness + y)]],


            }


for i in range(3):
    for points in alphabet["B"]:
        canvas = draw(canvas, amount, points[0], points[1], points[2])

    cv.imshow("", canvas)
    cv.waitKey(1000)
