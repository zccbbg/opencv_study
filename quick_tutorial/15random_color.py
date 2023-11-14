import cv2 as cv
import numpy as np

'''
随机数与随机颜色

'''
def demo():
    # 创建一个512x512的黑色图像，数据类型为8位无符号整数。这个图像由3个通道组成，分别表示蓝色、绿色和红色通道
    b1 = np.zeros((512,512,3),dtype=np.uint8)
    while True:
        # 生成两个随机整数，表示直线的 x 坐标起始点和结束点。这些坐标的范围是从0到511。
        xx = np.random.randint(0,512,2,dtype=int)
        # 生成两个随机整数，表示直线的 y 坐标起始点和结束点。这些坐标的范围同样是从0到511
        yy = np.random.randint(0,512,2,dtype=int)
        '''
        生成一个包含三个随机整数的数组，表示颜色值（蓝色、绿色、红色）。
        这些颜色值的范围是从0到254，因为图像的数据类型是8位无符号整数
        '''
        bgr = np.random.randint(0,255,3,dtype=np.uint8)
        '''
        在图像上绘制一条直线。
        参数包括图像数组 b1，
        起始点 (xx[0], yy[0])，
        结束点 (xx[1], yy[1])，
        颜色 (int(bgr[0]), int(bgr[1]), int(bgr[2]))，
        线条宽度 1，
        线条类型 cv.LINE_8，
        连接线条的标志 0。
        '''
        cv.line(b1, (xx[0], yy[0]), (xx[1], yy[1]), (int(bgr[0]), int(bgr[1]), int(bgr[2])), 1, cv.LINE_8, 0)
        cv.imshow("input",b1)
        c = cv.waitKey(1)
        if c==27:
            break
    cv.destroyAllWindows()

if __name__ == '__main__':
    demo()