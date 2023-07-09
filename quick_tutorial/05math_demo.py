import cv2 as cv
import numpy as np

'''
图像像素的算数操作
'''
def math_demo():
    image = cv.imread("../images/test.jpg")
    cv.imshow("input",image)
    h,w,c = image.shape
    blank = np.zeros_like(image)
    blank[:,:] = (80,80,80)
    cv.imshow("blank",blank)
    result = cv.add(image,blank)
    cv.imshow("result", result)
    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == '__main__':
    math_demo()
