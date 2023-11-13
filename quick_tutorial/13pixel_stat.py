import cv2 as cv
import numpy as np

'''
图像像素值统计
`cv.meanStdDev` 是 OpenCV 库中的一个函数，用于计算图像或数组的均值和标准差。
具体而言，`cv.meanStdDev` 函数计算给定图像或数组的每个通道的均值和标准差。它返回两个数组，第一个数组是每个通道的均值，第二个数组是每个通道的标准差。
函数的语法如下：
```python
mean, stddev = cv.meanStdDev(src[, mask])
```
其中：
- `src` 是输入图像或数组。
- `mask` 是可选参数，指定用于计算统计量的掩码。如果提供了掩码，则只计算掩码内的像素值。
函数将返回两个值：
- `mean` 是包含每个通道均值的数组。
- `stddev` 是包含每个通道标准差的数组。
这个函数在图像处理和计算机视觉中常用于计算图像的亮度和对比度等统计特征。
'''
def demo():
    b1 = cv.imread("../images/test.jpg")
    print(b1.shape)
    cv.imshow("input",b1)
    '''
    使用cv.meanStdDev函数计算图像的均值和标准差。
    means返回一个包含各通道均值的NumPy数组
    dev返回一个包含各通道标准差的NumPy数组。
    '''
    means,dev = cv.meanStdDev(b1)
    print(means,"dev:",dev)
    cv.waitKey(0)
    cv.destroyAllWindows()



if __name__ == '__main__':
    demo()