import cv2 as cv
import numpy as np
'''
图像对象的创建
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
