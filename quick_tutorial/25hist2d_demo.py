import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
'''
二维直方图
'''

def demo():
    image = cv.imread("../images/test.jpg")
    hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)
    hist = cv.calcHist([hsv], [0, 1], None, [48, 48], [0, 180, 0, 256])
    dst = cv.resize(hist, (400, 400))
    cv.normalize(dst, dst, 0, 255, cv.NORM_MINMAX)
    cv.imshow("image", image)
    dst = cv.applyColorMap(np.uint8(dst), cv.COLORMAP_JET)
    cv.imshow("hist", dst)
    plt.imshow(hist, interpolation='nearest')
    plt.title("2D Histogram")
    plt.show()
    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == '__main__':
    demo()