import cv2 as cv
import numpy as np

'''
图像色彩空间转换
'''
def color_space_demo():
    image = cv.imread("../images/test.jpg")
    gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    hsv = cv.cvtColor(image,cv.COLOR_BGR2HSV)

    cv.imshow("gray",gray)
    cv.imshow("hsv",hsv)
    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == '__main__':
    color_space_demo()
