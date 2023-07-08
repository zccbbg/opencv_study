import cv2 as cv
import numpy as np

def color_space_demo():
    image = cv.imread("C:/Users/zccbbg/Pictures/400.png")
    gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    hsv = cv.cvtColor(image,cv.COLOR_BGR2HSV)

    cv.imshow("gray",gray)
    cv.imshow("hsv",hsv)
    cv.waitKey(0)
    cv.destroyAllWindows()

def mat_demo1():
    image = cv.imread("C:/Users/zccbbg/Pictures/400.png")
    print(image.shape)
    blank = np.zeros_like(image)
    cv.imshow("blank", blank)
    cv.imshow("image", image)
    cv.waitKey(0)
    cv.destroyAllWindows()

def mat_demo2():
    image = cv.imread("C:/Users/zccbbg/Pictures/400.png")
    print(image.shape)
    roi = image[100:200,100:200,:]
    blank = np.zeros_like(image)
    blank[100:200,100:200,:] = image[100:200,100:200,:]
    cv.imshow("blank", blank)
    cv.imshow("image", image)
    cv.waitKey(0)
    cv.destroyAllWindows()

def pixel_demo():
    image = cv.imread("C:/Users/zccbbg/Pictures/400.png")
    cv.imshow("input",image)
    h,w,c = image.shape
    for row in range(h):
        for col in range(w):
            b,g,r = image[row,col]
            image[row,col] = (255-b,255-g,255-r)
    cv.imshow("result", image)
    cv.waitKey(0)
    cv.destroyAllWindows()

def math_demo():
    image = cv.imread("C:/Users/zccbbg/Pictures/400.png")
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
