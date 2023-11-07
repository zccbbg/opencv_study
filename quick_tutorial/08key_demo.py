import cv2 as cv
import numpy as np
'''
键盘响应操作
'''

def keys_demo():
    image = cv.imread("../images/test.jpg")
    cv.namedWindow("input",cv.WINDOW_AUTOSIZE)
    cv.imshow("input", image)
    while True:
        c=cv.waitKey(1)
        if c==49: #1
            # 将原始图像转换为灰度图像，使用cv.cvtColor函数和cv.COLOR_BGR2GRAY参数实现。
            gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
            cv.imshow("result",gray)
        if c==50: #2
            # 将原始图像转换为HSV颜色空间图像，使用cv.cvtColor函数和cv.COLOR_BGR2HSV参数实现。
            hsv = cv.cvtColor(image,cv.COLOR_BGR2HSV)
            cv.imshow("result",hsv)
        if c==51: #3
            # 反转原始图像的颜色，使用cv.bitwise_not函数实现。
            invert = cv.bitwise_not(image)
            cv.imshow("result",invert)
        if c==27:
            break
    cv.destroyAllWindows()

if __name__ == '__main__':
    keys_demo()