import cv2 as cv
import numpy as np

'''
作用是加载一张图像，将其缩小为原始尺寸的 75% 并显示在窗口中。
图像的缩放与插值
src	【必需】原图像
dsize	【必需】输出图像所需大小
fx	【可选】沿水平轴的比例因子
fy	【可选】沿垂直轴的比例因子
interpolation	【可选】插值方式

cv.INTER_NEAREST	最近邻插值
cv.INTER_LINEAR	双线性插值
cv.INTER_CUBIC	三次样条插值
cv.INTER_AREA	使用像素区域关系重新采样。它可能是图像抽取的首选方法，因为它可以提供无莫尔条纹的结果。但是当图像被缩放时，它类似于INTER_NEAREST方法。
'''

def demo():
    image = cv.imread("../images/test.jpg")
    cv.namedWindow("resize",cv.WINDOW_AUTOSIZE)
    '''
    使用OpenCV的cv.resize函数对图像进行缩放。具体来说：

    image 是要缩放的原始图像。
    (0, 0) 表示输出图像的大小，如果为 (0, 0)，则根据缩放因子自动计算输出大小。
    fx=0.75 表示在水平方向（宽度）上的缩放因子为 0.75。
    fy=0.75 表示在垂直方向（高度）上的缩放因子为 0.75。
    interpolation=cv.INTER_NEAREST 表示使用最近邻插值方法进行缩放。
    '''
    dst= cv.resize(image,(0,0),fx=0.75,fy=0.75,interpolation=cv.INTER_NEAREST)
    cv.imshow("resize",dst)
    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == '__main__':
    demo()