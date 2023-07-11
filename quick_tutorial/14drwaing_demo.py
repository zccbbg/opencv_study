import cv2 as cv
import numpy as np

'''
图像几何形状绘制

矩形：
cv2.rectangle(img, pt1, pt2, color[, thickness[, lineType[, shift]]])
img ： 待绘制矩形的图片；
pt1：矩形的起始坐标，使用元组表示，即（X 坐标，Y 坐标）；
pt2：矩形的结束坐标，使用元组表示，同上；
color：要绘制矩形的边界线颜色，如果是 BGR 格式，那（255,0,0）为蓝色；
thickness：矩形边界线的粗细像素，如果使用 -1 ，将填充整个矩形；
lineType 与 shift 参数，暂时用不上。
cv2.rectangle(img, (bbox.left, bbox.top), (bbox.right, bbox.bottom), (0,0,255), 2)

圆形：
cv2.circle(img, center_coordinates, radius, color, thickness)
img：待绘制圆的图像；
center_coordinates：圆的中心坐标。使用元组表示，即(X 坐标值，Y 坐标值)；
radius：圆的半径；
color：待绘制圆的边界线的颜色。对于 BGR，使用元组表示，例如：(255，0，0)为蓝色；
thickness：它是圆边界线的粗细像素。厚度-1 像素将以指定的颜色填充矩形。

其他函数
使用 OpenCV 在图像上进行标记，还有其他函数，例如 cv2.line() 画线，cv2.ellipse() 画椭圆，cv2.putText() 文字绘制。
看到这里，本能的就注意到文字绘制了，因为这里面经常会出现的一个大坑是中文乱码的问题，
接下来，就实际的尝试一下。
先看一下该函数的语法格式：
cv2.putText(img, text, org, font, fontScale, color[, thickness[, lineType[, bottomLeftOrigin]]])

其中各参数说明如下：
img：待绘制文本的图像。
text：待绘制的文本字符串。
org：图像中文本字符串左下角的坐标。使用元组表示，即(X 坐标值，Y 坐标值)
font：字体类型，一些字体类型是 FONT_HERSHEY_SIMPLEX，FONT_HERSHEY_PLAIN
fontScale：字体比例因子乘以 font-specific 基本大小
color：待绘制的文本字符串的颜色。对于 BGR，使用一个元组表示。例如：(255，0，0)为蓝色。
thickness：它是线的粗细像素。
lineType：可选参数，它给出了要使用的行的类型。
bottomLeftOrigin：可选参数。如果为 true，则图像数据原点位于左下角。否则，它位于左上角。
'''
def demo():
    b1 = np.zeros((512,512,3),dtype=np.uint8)
    cv.rectangle(b1,(50,50),(400,400),(0,0,255),4,8,0)
    cv.circle(b1,(200,200),50,(255,0,0),2,8,0)
    cv.putText(b1, 'OpenCV', (250, 250), cv.FONT_HERSHEY_SIMPLEX,1, (0, 190, 150), 2)
    cv.imshow("input",b1)
    cv.waitKey(0)
    cv.destroyAllWindows()



if __name__ == '__main__':
    demo()