import cv2 as cv
import numpy as np

'''
将一张彩色图像进行归一化处理，然后显示归一化后的图像
归一化（Normalization）是一种数据预处理技术，用于将数据缩放或转换为特定的范围，以便更好地适应模型的训练或算法的要求。在计算机视觉和图像处理中，归一化通常指的是将图像的像素值缩放到一个特定范围，使其更易于处理和分析。
cv.normalize:OpenCV 中的 normalize 函数是一个用于标准化数组的工具。 它可以将数组中的所有元素的值调整到指定的范围内。 具体而言，它可以将数组中的每个元素的值映射到0 到1 之间，或者将它们映射到某个自定义的范围内。
'''
def demo():
    image = cv.imread("../images/test.jpg")
    cv.namedWindow("norm_demo",cv.WINDOW_AUTOSIZE)
    result= np.zeros_like(np.float32(image))
    '''
    使用OpenCV的cv.normalize函数对图像进行归一化。具体来说：
    np.float32(image) 将输入图像的数据类型转换为np.float32。
    result 是存储归一化结果的数组。
    0 是归一化的下界。
    1 是归一化的上界。
    cv.NORM_MINMAX 表示使用最小-最大归一化方法。
    dtype=cv.CV_32F 指定结果的数据类型为np.float32。
    '''
    cv.normalize(np.float32(image),result,0,1,cv.NORM_MINMAX,dtype=cv.CV_32F)
    cv.imshow("norm_demo",np.uint8(result*255))
    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == '__main__':
    demo()