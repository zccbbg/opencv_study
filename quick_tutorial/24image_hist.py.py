import cv2 as cv
from matplotlib import pyplot as plt
'''
使用OpenCV（cv2）和matplotlib库来计算和绘制一维直方图
'''

def demo():
    image = cv.imread("../images/test.jpg")
    cv.imshow("input", image)
    color = ('blue', 'green', 'red')
    for i, color in enumerate(color):
        '''
        参数解释：
            [image]：包含图像的列表。
            [i]：要计算直方图的通道索引，0表示蓝色通道，1表示绿色通道，2表示红色通道。
            None：掩码，通常为None，表示不使用掩码。
            [32]：直方图的bin数，这里设置为32。
            [0, 256]：像素值的范围，通常为[0, 256]表示完整的像素值范围。
        '''
        hist = cv.calcHist([image], [i], None, [32], [0, 256])
        print(hist)
        # 将直方图数据绘制为折线图。
        plt.plot(hist, color=color)
        # 设置x轴的显示范围，即bin数的范围。
        plt.xlim([0, 32])
    plt.show()
    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == '__main__':
    demo()