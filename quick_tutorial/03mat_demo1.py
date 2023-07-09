import cv2 as cv
import numpy as np
'''
图像对象的创建
numpy.zeros_like：返回与指定数组具有相同形状和数据类型的数组，并且数组中的值都为0。
>>> x = np.arange(6)
>>> x = x.reshape((2, 3))
>>> x
array([[0, 1, 2],
[3, 4, 5]])
>>> np.zeros_like(x)
array([[0, 0, 0],
[0, 0, 0]])
>>>
>>> y = np.arange(3, dtype=float)
>>> y
array([ 0., 1., 2.])
>>> np.zeros_like(y)
array([ 0., 0., 0.])
'''
def mat_demo1():
    image = cv.imread("../images/test.jpg")
    print(image.shape)
    blank = np.zeros_like(image)
    cv.imshow("blank", blank)
    cv.imshow("image", image)
    cv.waitKey(0)
    cv.destroyAllWindows()


if __name__ == '__main__':
    mat_demo1()
