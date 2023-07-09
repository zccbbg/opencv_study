import cv2 as cv
import numpy as np
'''
像素的逻辑操作

bitwise_and是对二进制数据进行“与”操作，即对图像（灰度图像或彩色图像均可）每个像素值进行二进制“与”操作，1&1=1，1&0=0，0&1=0，0&0=0
bitwise_or是对二进制数据进行“或”操作，即对图像（灰度图像或彩色图像均可）每个像素值进行二进制“或”操作，1|1=1，1|0=0，0|1=0，0|0=0
bitwise_xor是对二进制数据进行“异或”操作，即对图像（灰度图像或彩色图像均可）每个像素值进行二进制“异或”操作，1^1=0,1^0=1,0^1=1,0^0=0
bitwise_not是对二进制数据进行“非”操作，即对图像（灰度图像或彩色图像均可）每个像素值进行二进制“非”操作，~1=0，~0=1

原文链接：https://blog.csdn.net/u011028345/article/details/77278467
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