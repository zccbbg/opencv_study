import cv2 as cv
import numpy as np
'''
自带颜色表操作
'''

def demo():
    '''
    定义了一个列表colormap，其中包含了多种颜色映射的选项，通过在图像上应用不同的颜色映射，可以改变图像的色调和外观。
    共有19种不同的颜色映射选项，可以在cv.applyColorMap函数中使用。
    '''
    colormap = [
        cv.COLORMAP_AUTUMN,
        cv.COLORMAP_BONE,
        cv.COLORMAP_JET,
        cv.COLORMAP_WINTER,
        cv.COLORMAP_RAINBOW,
        cv.COLORMAP_OCEAN,
        cv.COLORMAP_SUMMER,
        cv.COLORMAP_SPRING,
        cv.COLORMAP_COOL,
        cv.COLORMAP_PINK,
        cv.COLORMAP_HOT,
        cv.COLORMAP_PARULA,
        cv.COLORMAP_MAGMA,
        cv.COLORMAP_INFERNO,
        cv.COLORMAP_PLASMA,
        cv.COLORMAP_VIRIDIS,
        cv.COLORMAP_CIVIDIS,
        cv.COLORMAP_TWILIGHT,
        cv.COLORMAP_TWILIGHT_SHIFTED
    ]
    image = cv.imread("../images/test.jpg")
    cv.namedWindow("input",cv.WINDOW_AUTOSIZE)
    cv.imshow("input", image)
    index=0
    while True:
        '''
        使用cv.applyColorMap函数将当前选定的颜色映射应用到原始图像上。
        colormap[index % 19]选择颜色映射列表中的一个颜色映射，index % 19确保索引循环在0到18之间，以便循环应用不同的颜色映射。
        '''
        dst = cv.applyColorMap(image,colormap[index%19])
        index+=1
        cv.imshow("color style",dst)
        c=cv.waitKey(200) # 等待200毫秒
        if c==27:
            break
    cv.destroyAllWindows()

if __name__ == '__main__':
    demo()