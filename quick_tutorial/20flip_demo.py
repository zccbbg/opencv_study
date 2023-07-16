import cv2 as cv
import numpy as np

'''
图像翻转
'''

def demo():
    image = cv.imread("../images/test.jpg")
    cv.imshow("input",image)
    cv.namedWindow("flip",cv.WINDOW_AUTOSIZE)
    dst= cv.flip(image,-1)
    cv.imshow("flip",dst)
    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == '__main__':
    demo()