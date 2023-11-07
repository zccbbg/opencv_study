import cv2 as cv
import numpy as np
'''
调整图像亮度
'''
def nothing(x):
    print(x)

def adjust_lightness_demo():
    image = cv.imread("../images/test.jpg")
    cv.namedWindow("input",cv.WINDOW_AUTOSIZE)
    cv.createTrackbar("lightness","input",0,100,nothing)
    cv.imshow("input", image)
    blank = np.zeros_like(image)
    while True:
        pos = cv.getTrackbarPos("lightness","input") # 获取名为"lightness"的轨迹条的当前位置，即用户调整的亮度值。
        blank[:,:] = (pos,pos,pos) # 将全黑图像blank的所有像素值设置为(pos, pos, pos)，这意味着将所有像素的颜色设置为灰色，并且灰色的亮度由轨迹条的位置pos决定。
        '''
        使用cv.add函数将原始图像image和灰色图像blank相加，生成一个新的图像result，其中每个像素是对应位置的两个图像像素之和。
        这将导致原始图像中的每个像素的颜色都加了一个灰色的亮度。
        '''
        result=cv.add(image,blank)
        cv.imshow("result",result)
        c=cv.waitKey(1)
        if c==27: # 等待1毫秒，以便捕获用户的键盘输入。会返回相应的ASCII码值。如果用户按下Esc键（ASCII码为27），则退出循环。
            break
    cv.destroyAllWindows()

if __name__ == '__main__':
    adjust_lightness_demo()