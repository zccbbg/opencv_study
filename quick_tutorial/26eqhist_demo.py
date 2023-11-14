import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
'''
直方图均衡化
'''

def demo():
    image = cv.imread("../images/test.jpg",cv.IMREAD_GRAYSCALE)
    cv.imshow("input", image)
    '''
    使用 OpenCV 的 cv.equalizeHist 函数对灰度图像进行直方图均衡化。
    这个函数将应用直方图均衡化，使得图像的灰度级分布更均匀，从而增强对比度。
    '''
    result = cv.equalizeHist(image)
    cv.imshow("result", result)
    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == '__main__':
    demo()