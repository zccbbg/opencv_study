import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
'''
高斯双边模糊
这段代码加载了一张彩色图像，对其进行了双边滤波处理，然后显示原始图像和双边滤波处理后的结果。
双边滤波是一种能够在保留边缘信息的同时对图像进行平滑处理的滤波方法，常用于去除噪声并保留图像中的重要细节。
'''

def demo():
    image = cv.imread("../images/test.jpg")
    cv.imshow("input", image)
    '''
    使用 OpenCV 的 cv.bilateralFilter 函数对彩色图像进行双边滤波处理。这个函数的参数包括：

    image：输入的图像。
    0：表示滤波器的直径，如果为0，则根据 sigmaSpace 计算。
    100：控制颜色空间的标准差，即控制对颜色的权重。
    10：控制空间域的标准差，即控制像素距离的权重。
    '''
    result = cv.bilateralFilter(image, 0, 100, 10)
    cv.imshow("result", result)
    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == '__main__':
    demo()