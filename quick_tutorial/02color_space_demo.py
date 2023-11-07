import cv2 as cv
import numpy as np

'''
图像色彩空间转换

cvtColor()函数是opencv里的颜色空间转换函数，可以实现RGB颜色向HSV，HSI等颜色空间的转换，也可以转换成灰度图像。

HSV颜色模型
HSV(Hue, Saturation, Value)是根据颜色的直观特性由A. R. Smith在1978年创建的一种颜色空间, 也称六角锥体模型(Hexcone Model)。
这个模型中颜色的参数分别是：色调（H），饱和度（S），亮度（V）。
色调H：用角度度量，取值范围为0°～360°，从红色开始按逆时针方向计算，红色为0°，绿色为120°,蓝色为240°。它们的补色是：黄色为60°，青色为180°,品红为300°；
饱和度S：取值范围为0.0～1.0；
亮度V：取值范围为0.0(黑色)～1.0(白色)。
https://blog.csdn.net/qinglongzhan/article/details/107213767
'''
def color_space_demo():
    image = cv.imread("../images/test.jpg")
    gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY) #将加载的彩色图像转换为灰度图像
    hsv = cv.cvtColor(image,cv.COLOR_BGR2HSV) #将加载的彩色图像转换为HSV颜色空间

    cv.imshow("gray",gray)
    cv.imshow("hsv",hsv)
    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == '__main__':
    color_space_demo()
