import cv2 as cv
import numpy as np
'''
调整图像对比度
'''
def nothing(x):
    print(x)

def adjust_contrast_demo():
    image = cv.imread("../images/test.jpg")
    '''
    创建一个窗口，并为它指定一个名称（"input"），
    并使用cv.WINDOW_AUTOSIZE来指定窗口的大小自适应图像的大小。
    '''
    cv.namedWindow("input",cv.WINDOW_AUTOSIZE)
    '''
    这个轨迹条允许用户调整图像的亮度。0是轨迹条的初始值，100是轨迹条的最大值，nothing是一个回调函数，用于响应轨迹条的变化
    '''
    cv.createTrackbar("lightness","input",0,100,nothing)
    cv.createTrackbar("contrast","input",100,200,nothing)
    cv.imshow("input", image)
    blank = np.zeros_like(image)
    while True:
        # 获取名为"lightness"的轨迹条的当前位置，即用户调整的亮度值。
        light = cv.getTrackbarPos("lightness","input")
        # 获取名为"contrast"的轨迹条的当前位置，并将其除以100，以得到用户调整的对比度值。
        contrast = cv.getTrackbarPos("contrast","input")/100
        print("light:",light,"contrast:",contrast)
        # 其中image是原始图像，blank是全黑图像，0.5是权重，light和contrast分别用于亮度和对比度的调整。
        result=cv.addWeighted(image,contrast,blank,0.5,light)
        cv.imshow("result",result)
        c=cv.waitKey(1) # 等待1毫秒，以便捕获用户的键盘输入。会返回相应的ASCII码值。如果用户按下Esc键（ASCII码为27），则退出循环。
        if c==27:
            break
    cv.destroyAllWindows()

if __name__ == '__main__':
    adjust_contrast_demo()