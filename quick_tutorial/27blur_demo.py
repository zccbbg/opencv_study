import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
'''
这段代码加载了一张灰度图像，对其进行了均值滤波（模糊处理），然后显示原始图像和模糊处理后的结果。
均值滤波是一种常见的图像模糊方法，它通过将每个像素的值替换为周围像素值的平均值来降低图像的高频信息，从而实现模糊效果。
'''
def demo():
    image = cv.imread("../images/test.jpg",cv.IMREAD_GRAYSCALE)
    cv.imshow("input", image)
    '''
    使用 OpenCV 的 cv.blur 函数对灰度图像进行均值滤波（模糊处理）。
    (15, 15) 是滤波核的大小，表示在水平和垂直方向上的窗口大小为 15x15。
    '''
    result = cv.blur(image, (15, 15))
    cv.imshow("result", result)
    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == '__main__':
    demo()