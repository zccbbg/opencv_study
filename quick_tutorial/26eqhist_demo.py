import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
'''
直方图均衡化
'''

def demo():
    image = cv.imread("../images/test.jpg",cv.IMREAD_GRAYSCALE)
    cv.imshow("input", image)
    result = cv.equalizeHist(image)
    cv.imshow("result", result)
    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == '__main__':
    demo()