import cv2 as cv
import numpy as np

'''
随机数与随机颜色

'''
def demo():
    b1 = np.zeros((512,512,3),dtype=np.uint8)
    while True:
        xx = np.random.randint(0,512,2,dtype=np.int)
        yy = np.random.randint(0,512,2,dtype=np.int)
        bgr = np.random.randint(0,255,3,dtype=np.uint8)
        cv.line(b1,(xx[0],yy[0]),(xx[1],yy[1]),(np.int(bgr[0]),np.int(bgr[1]),np.int(bgr[2])),1,8,0)
        cv.imshow("input",b1)
        c = cv.waitKey(1)
        if c==27:
            break
    cv.destroyAllWindows()

if __name__ == '__main__':
    demo()