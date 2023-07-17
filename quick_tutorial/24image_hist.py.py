import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
'''
一维直方图
'''

def demo():
    image = cv.imread("../images/test.jpg")
    cv.imshow("input", image)
    color = ('blue', 'green', 'red')
    for i, color in enumerate(color):
        hist = cv.calcHist([image], [i], None, [32], [0, 256])
        print(hist)
        plt.plot(hist, color=color)
        plt.xlim([0, 32])
    plt.show()
    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == '__main__':
    demo()