import cv2
import numpy as np

'''
cv2.inRange是OpenCV库中的一种函数，用于提取图像中特定颜色范围内的像素值，从而实现颜色分割或物体识别等应用。
'''
# 读取图片
img = cv2.imread('../images/greenback.png')

# 将图片转换为HSV色彩空间
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# 设置颜色范围
lower = np.array([0, 0, 0])
upper = np.array([255, 255, 255])

'''
根据设定的颜色范围，在HSV图像中提取符合条件的像素点，生成一个二值掩码（mask），其中符合条件的像素值被设为255，不符合条件的像素值被设为0。
'''
mask = cv2.inRange(hsv, lower, upper)

# 显示结果
cv2.imshow('mask', mask)
cv2.waitKey(0)
cv2.destroyAllWindows()