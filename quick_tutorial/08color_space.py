import cv2 as cv
import numpy as np

'''
图像色彩空间转换
'''
def demo():
    b1 = cv.imread("C:/Users/zccbbg/Pictures/400.png")
    print(b1.shape)
    cv.imshow("input",b1)
    b2 = b1[:,:,1]
    cv.imshow("b2",b2)

    mv = cv.split(b1)
    print(len(mv))

    mv[0][:,:] = 255
    result = cv.merge(mv)
    cv.imshow("result",result)

    cv.waitKey(0)
    cv.destroyAllWindows()



if __name__ == '__main__':
    demo()