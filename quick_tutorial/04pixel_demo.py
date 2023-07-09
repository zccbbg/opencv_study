import cv2 as cv
import numpy as np

'''
图像像素的读写操作
'''
def pixel_demo():
    image = cv.imread("../images/test.jpg")
    cv.imshow("input",image)
    h,w,c = image.shape
    for row in range(h):
        for col in range(w):
            b,g,r = image[row,col]
            image[row,col] = (255-b,255-g,255-r)
    cv.imshow("result", image)
    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == '__main__':
    pixel_demo()
