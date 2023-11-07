import cv2 as cv
import numpy as np

'''
图像像素的算数操作
'''
def math_demo():
    image = cv.imread("../images/test.jpg")
    cv.imshow("input",image)
    # 其中h表示高度（行数），w表示宽度（列数），c表示通道数。对于彩色图像，通道数通常为3，表示红色、绿色和蓝色三个通道
    h,w,c = image.shape
    # 创建一个和加载的图像image具有相同形状的全黑图像。np.zeros_like函数生成一个与输入图像相同尺寸的全零矩阵
    blank = np.zeros_like(image)
    # 将全黑图像blank的所有像素值设置为(80, 80, 80)，这意味着将所有像素的颜色设置为灰色
    blank[:,:] = (80,80,80)
    cv.imshow("blank",blank)
    '''
    使用OpenCV的cv.add函数将原始图像image和全黑图像blank相加，
    生成一个新的图像result，其中每个像素是对应位置的两个图像像素之和
    这将导致原始图像中的每个像素的颜色都加了(80, 80, 80)，也就是将原始图像中的颜色亮度增加了
    '''
    result = cv.add(image,blank)
    cv.imshow("result", result)
    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == '__main__':
    math_demo()
