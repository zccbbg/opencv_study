import numpy as np
import cv2 as cv
# 以灰度图的形式读取图像
img = cv.imread('../images/test.jpg',0)
cv.imshow('img',img)
cv.waitKey(0)
cv.destroyAllWindows()