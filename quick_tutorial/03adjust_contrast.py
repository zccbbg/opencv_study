import cv2 as cv
import numpy as np
'''
调整图像对比度
'''
def nothing(x):
    print(x)

def adjust_contrast_demo():
    image = cv.imread("C:/Users/zccbbg/Pictures/400.png")
    cv.namedWindow("input",cv.WINDOW_AUTOSIZE)
    cv.createTrackbar("lightness","input",0,100,nothing)
    cv.createTrackbar("contrast","input",100,200,nothing)
    cv.imshow("input", image)
    blank = np.zeros_like(image)
    while True:
        light = cv.getTrackbarPos("lightness","input")
        contrast = cv.getTrackbarPos("contrast","input")/100
        print("light:",light,"contrast:",contrast)
        result=cv.addWeighted(image,contrast,blank,0.5,light)
        cv.imshow("result",result)
        c=cv.waitKey(1)
        if c==27:
            break
    cv.destroyAllWindows()

if __name__ == '__main__':
    adjust_contrast_demo()