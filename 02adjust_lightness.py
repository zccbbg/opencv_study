import cv2 as cv
import numpy as np
'''
调整图像亮度
'''
def nothing(x):
    print(x)

def adjust_lightness_demo():
    image = cv.imread("C:/Users/zccbbg/Pictures/400.png")
    cv.namedWindow("input",cv.WINDOW_AUTOSIZE)
    cv.createTrackbar("lightness","input",0,100,nothing)
    cv.imshow("input", image)
    blank = np.zeros_like(image)
    while True:
        pos = cv.getTrackbarPos("lightness","input")
        blank[:,:] = (pos,pos,pos)
        result=cv.add(image,blank)
        cv.imshow("result",result)
        c=cv.waitKey(1)
        if c==27:
            break
    cv.destroyAllWindows()

if __name__ == '__main__':
    adjust_lightness_demo()