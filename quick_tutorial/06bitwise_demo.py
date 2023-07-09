import cv2 as cv
import numpy as np
'''
像素的逻辑操作
'''

def demo():
    b1 = np.zeros((400,400,3), dtype=np.uint8)
    b1[:,:] =(255,0,255)
    b2 = np.zeros((400,400,3), dtype=np.uint8)
    b2[:, :] = (0, 255, 255)
    cv.imshow("b1",b1)
    cv.imshow("b2",b2)

    dst1 = cv.bitwise_and(b1,b2)
    dst2 = cv.bitwise_not(b1,b2)
    cv.imshow("bitwise_and",dst1)
    cv.imshow("bitwise_not",dst2)

    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == '__main__':
    demo()