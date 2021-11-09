import cv2 as cv
import numpy as np
import pyautogui


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


canvas = np.zeros((1000, 1000, 1), dtype="uint8")

amount = 1000  # amount of dots drawn

start = (0, 500)
middle = (45, 891)
end = (999, 500)

# for i in range(canvas.shape[1]*1000):
#     canvas = draw(np.zeros((1000, 1000, 1), dtype="uint8"), 1000, start, (pyautogui.position()[0], pyautogui.position()[1]), end)
#
#     cv.imshow("", canvas)
#     cv.waitKey(1)

for i in range(canvas.shape[1]):
    canvas = draw(np.zeros((1000, 1000, 1), dtype="uint8"), amount, start, (i, i), end)

    cv.imshow("", canvas)
    cv.waitKey(1)
