import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
'''
这段代码用于计算并展示一张图像的二维颜色直方图，包括原始的直方图和热度图。
'''
def demo():
    image = cv.imread("../images/test.jpg")
    '''
    将加载的 BGR 格式图像转换为 HSV（色调、饱和度、亮度）颜色空间。
    这一步的目的是为了在 HSV 空间中进行颜色直方图的计算，因为 HSV 更符合人类感知。
    '''
    hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)
    '''
    使用 OpenCV 的 cv.calcHist 函数计算 HSV 图像的二维直方图。参数解释如下：
    [hsv]：包含图像的列表。
    [0, 1]：要计算直方图的通道索引，0 表示色调（H），1 表示饱和度（S）。
    None：掩码，通常为 None，表示不使用掩码。
    [48, 48]：直方图的 bin 数，即色调和饱和度方向上的 bin 数。
    [0, 180, 0, 256]：像素值的范围，色调的范围是 [0, 180]，饱和度的范围是 [0, 256]。
    '''
    hist = cv.calcHist([hsv], [0, 1], None, [48, 48], [0, 180, 0, 256])
    # 将直方图的大小调整为(400, 400)，以便更好地显示。
    dst = cv.resize(hist, (400, 400))
    # 将直方图数据标准化到 [0, 255] 的范围内，以便显示为热度图。
    cv.normalize(dst, dst, 0, 255, cv.NORM_MINMAX)
    cv.imshow("image", image)
    # 将标准化后的直方图数据应用颜色映射，使用 Jet 色彩映射方案，以便更直观地显示热度。
    dst = cv.applyColorMap(np.uint8(dst), cv.COLORMAP_JET)
    cv.imshow("hist", dst)
    plt.imshow(hist, interpolation='nearest')
    plt.title("2D Histogram")
    plt.show()
    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == '__main__':
    demo()