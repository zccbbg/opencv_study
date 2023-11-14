import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
'''
高斯模糊是一种常用的图像模糊方法，通过使用高斯核来降低图像的高频信息，从而实现模糊效果。
高斯模糊在图像处理中常用于去除图像中的噪声，平滑图像，或者作为其他图像处理操作的预处理步骤。
'''
def demo():
    image = cv.imread("../images/test.jpg",cv.IMREAD_GRAYSCALE)
    cv.imshow("input", image)
    '''
    使用 OpenCV 的 cv.GaussianBlur 函数对灰度图像进行高斯模糊处理。
    (5, 5) 是高斯核的大小，表示在水平和垂直方向上的窗口大小为 5x5。
    参数 15 表示高斯核的标准差，用于控制模糊的程度。
    '''
    result = cv.GaussianBlur(image, (5, 5), 15)
    cv.imshow("result", result)
    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == '__main__':
    demo()