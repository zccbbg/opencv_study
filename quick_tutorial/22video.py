import cv2 as cv
import numpy as np

'''
摄像头使用
'''

def demo():
    cap = cv.VideoCapture(0)
    while True:
        ret,frame = cap.read()
        if ret is True:
            cv.imshow("frame",frame)
            c = cv.waitKey(10)
            if c == 27:
                break
    cv.destroyAllWindows()

if __name__ == '__main__':
    demo()