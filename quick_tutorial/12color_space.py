import cv2 as cv
import numpy as np

'''
图像色彩空间转换
'''
def demo():
    b1 = cv.imread("../images/greenback.png")
    print(b1.shape)
    cv.imshow("input",b1)

    hsv = cv.cvtColor(b1,cv.COLOR_BGR2HSV)
    cv.imshow("hsv",hsv)
    mask = cv.inRange(hsv,(35,43,46),(77,255,255))
    cv.bitwise_and(b1,b1,mask=mask)
    cv.imshow("mask",mask)

    cv.waitKey(0)
    cv.destroyAllWindows()



if __name__ == '__main__':
    demo()