import cv2 as cv
import numpy as np

'''
通道分离与合并
'''
def demo():
    b1 = cv.imread("../images/test.jpg")
    print(b1.shape)
    cv.imshow("input",b1)
    b2 = b1[:,:,1]
    cv.imshow("b2",b2)

    mv = cv.split(b1)
    print(len(mv))

    mv[0][:,:] = 255
    result = cv.merge(mv)
    cv.imshow("result",result)

    cv.waitKey(0)
    cv.destroyAllWindows()

'''
通道分离与合并:不是很理解，网上又找了另外的例子
为什么得到的是三张不同d灰度图呢？不是已经分离出R，G，B通道了吗？应该是分别是红色图，绿色图，蓝色图才对阿。

原因是：当调用 imshow（R）时，是把图像的R，G，B三个通道的值都变为R的值，所以图像的颜色三通道值为（R，R，R）

同理 imshow（G）和imshow（B）所显示d图像的颜色通道也依次为（G，G，G）和（B，B，B）。

而 当三个通道d值相同时，则为灰度图。
'''
def split():
    image = cv.imread("../images/test.jpg");  # 读取要处理的图片
    B, G, R = cv.split(image);  # 分离出图片的B，R，G颜色通道
    cv.imshow("RED", R);  # 显示三通道的值都为R值时d图片
    cv.imshow("GREEN", G);  # 显示三通道的值都为G值时d图片
    cv.imshow("BLUE", B);  # 显示三通道的值都为B值时d图片
    cv.waitKey(0);  # 不让程序突然结束

'''
下面将使用merge（）函数将某一颜色通道（如R）与零矩阵合并，形成（R，0，0）从而显示只有红色通道的图
'''
def merge():
    image = cv.imread("../images/test.jpg");  # 读取要处理的图片
    B, G, R = cv.split(image);  # 分离出图片的B，R，G颜色通道
    zeros = np.zeros(image.shape[:2], dtype="uint8");  # 创建与image相同大小的零矩阵
    cv.imshow("BLUE", cv.merge([B, zeros, zeros]));  # 显示 （B，0，0）图像
    cv.imshow("GREEN", cv.merge([zeros, G, zeros]));  # 显示（0，G，0）图像
    cv.imshow("RED", cv.merge([zeros, zeros, R]));  # 显示（0，0，R）图像
    cv.waitKey(0);

if __name__ == '__main__':
    merge()