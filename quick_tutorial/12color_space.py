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
    '''
    使用cv.cvtColor函数将原始图像b1从BGR颜色空间转换为HSV颜色空间
    '''
    hsv = cv.cvtColor(b1,cv.COLOR_BGR2HSV)
    cv.imshow("hsv",hsv)
    '''
    使用cv.inRange函数生成一个二值掩码mask，
    HSV图像的像素值在指定范围内的被设为255（白色），不在范围内的被设为0（黑色）。
    在这里，指定的HSV范围为(35, 43, 46)到(77, 255, 255)，这个范围用于表示绿色的颜色范围。
    '''
    mask = cv.inRange(hsv,(35,43,46),(77,255,255))
    '''
    使用cv.bitwise_not函数对掩码取反，将白色变为黑色，黑色变为白色
    这样，生成的掩码将包含图像中非绿色区域的白色像素
    '''
    cv.bitwise_not(mask,mask)
    '''
    使用cv.bitwise_and函数对原始图像b1和生成的掩码mask进行按位与操作。
    这意味着只有在掩码为白色（255）的位置，原始图像的对应位置的像素值才被保留，其他位置的像素值为0。
    最终生成的result图像将只保留原图中绿色区域的像素，而非绿色区域的像素被设为0。
    '''
    result = cv.bitwise_and(b1,b1,mask=mask)
    cv.imshow("mask",mask)
    cv.imshow("result",result)
    cv.waitKey(0)
    cv.destroyAllWindows()



if __name__ == '__main__':
    demo()