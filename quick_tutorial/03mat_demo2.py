import cv2 as cv
import numpy as np

'''
图像对象的赋值
'''
def mat_demo2():
    image = cv.imread("../images/test.jpg")
    print(image.shape)
    roi = image[100:200,100:200,:]
    blank = np.zeros_like(image)
    blank[100:200,100:200,:] = image[100:200,100:200,:]
    cv.imshow("blank", blank)
    cv.imshow("image", image)
    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == '__main__':
    mat_demo2()
