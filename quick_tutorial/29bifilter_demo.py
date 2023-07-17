import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
'''
高斯双边模糊
'''

def demo():
    image = cv.imread("../images/test.jpg")
    cv.imshow("input", image)
    result = cv.bilateralFilter(image, 0, 100, 10)
    cv.imshow("result", result)
    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == '__main__':
    demo()