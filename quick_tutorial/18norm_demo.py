import cv2 as cv
import numpy as np

'''
像素类型转换
cv.normalize:OpenCV 中的 normalize 函数是一个用于标准化数组的工具。 它可以将数组中的所有元素的值调整到指定的范围内。 具体而言，它可以将数组中的每个元素的值映射到0 到1 之间，或者将它们映射到某个自定义的范围内。
'''

def demo():
    image = cv.imread("../images/test.jpg")
    cv.namedWindow("norm_demo",cv.WINDOW_AUTOSIZE)
    result= np.zeros_like(np.float32(image))
    cv.normalize(np.float32(image),result,0,1,cv.NORM_MINMAX,dtype=cv.CV_32F)
    cv.imshow("norm_demo",np.uint8(result*255))
    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == '__main__':
    demo()