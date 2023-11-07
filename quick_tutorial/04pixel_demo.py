import cv2 as cv
import numpy as np

'''
图像像素的读写操作
'''
def pixel_demo():
    image = cv.imread("../images/test.jpg")
    cv.imshow("input",image)
    '''
    其中h表示高度（行数），w表示宽度（列数），c表示通道数。对于彩色图像，通道数通常为3，表示红色、绿色和蓝色三个通道
    '''
    h,w,c = image.shape
    for row in range(h): #外层循环遍历图像的每一行
        for col in range(w): #内层循环遍历图像的每一列
            b,g,r = image[row,col] # 这一行代码获取当前像素的蓝色（b）、绿色（g）和红色（r）通道的值
            image[row,col] = (255-b,255-g,255-r) #反转了当前像素的颜色，通过将每个通道的值减去原始值从而得到反转后的颜色。具体地，对每个通道的值取补，以实现颜色反转
    cv.imshow("result", image)
    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == '__main__':
    pixel_demo()
