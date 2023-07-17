import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
'''
图像卷积
'''

def demo():
    image = cv.imread("../images/test.jpg",cv.IMREAD_GRAYSCALE)
    cv.imshow("input", image)
    result = cv.blur(image, (15, 15))
    cv.imshow("result", result)
    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == '__main__':
    demo()