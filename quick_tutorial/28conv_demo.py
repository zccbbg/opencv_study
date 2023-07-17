import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
'''
高斯模糊
'''

def demo():
    image = cv.imread("../images/test.jpg",cv.IMREAD_GRAYSCALE)
    cv.imshow("input", image)
    result = cv.GaussianBlur(image, (5, 5), 15)
    cv.imshow("result", result)
    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == '__main__':
    demo()