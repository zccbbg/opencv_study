import cv2 as cv
import numpy as np

'''
图像对象的赋值
'''
def mat_demo2():
    image = cv.imread("../images/test.jpg")
    print(image.shape)
    '''
    创建一个和加载的图像image具有相同形状的全黑图像
    np.zeros_like函数生成一个与输入图像相同尺寸的全零矩阵，用于存储在变量blank中。
    '''
    blank = np.zeros_like(image)
    '''
    从加载的原始图像image中选择一个特定的区域，
    这个区域的左上角坐标为(100, 100)，右下角坐标为(200, 200)，
    并将这个区域的像素值复制到全黑图像blank的对应位置
    '''
    blank[100:200,100:200,:] = image[100:200,100:200,:]
    cv.imshow("blank", blank)
    cv.imshow("image", image)
    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == '__main__':
    mat_demo2()
