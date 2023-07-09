import cv2 as cv
import numpy as np

'''
图像色彩空间转换

bitwise_and是对二进制数据进行“与”操作，即对图像（灰度图像或彩色图像均可）每个像素值进行二进制“与”操作，1&1=1，1&0=0，0&1=0，0&0=0
bitwise_or是对二进制数据进行“或”操作，即对图像（灰度图像或彩色图像均可）每个像素值进行二进制“或”操作，1|1=1，1|0=0，0|1=0，0|0=0
bitwise_xor是对二进制数据进行“异或”操作，即对图像（灰度图像或彩色图像均可）每个像素值进行二进制“异或”操作，1^1=0,1^0=1,0^1=1,0^0=0
bitwise_not是对二进制数据进行“非”操作，即对图像（灰度图像或彩色图像均可）每个像素值进行二进制“非”操作，~1=0，~0=1
原文链接：https://blog.csdn.net/u011028345/article/details/77278467

cv2.inRange是OpenCV库中的一种函数，用于提取图像中特定颜色范围内的像素值，从而实现颜色分割或物体识别等应用。
'''
def demo():
    b1 = cv.imread("../images/greenback.png")
    print(b1.shape)
    cv.imshow("input",b1)

    hsv = cv.cvtColor(b1,cv.COLOR_BGR2HSV)
    cv.imshow("hsv",hsv)
    mask = cv.inRange(hsv,(35,43,46),(77,255,255))
    cv.bitwise_not(mask,mask)
    result = cv.bitwise_and(b1,b1,mask=mask)
    cv.imshow("mask",mask)
    cv.imshow("result",result)
    cv.waitKey(0)
    cv.destroyAllWindows()



if __name__ == '__main__':
    demo()