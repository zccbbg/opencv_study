import cv2 as cv
import numpy as np

'''
绘制多边形

绘制折线或多边形 ：cv.polylines(img, pts, isClosed, color[, thickness[, lineType[, shift]]]) → img
isClosed：表示标志，决定所绘制的多边形是否闭合。若为 True ，则画若干个闭合多边形；若为 False ，则画一条连接所有点的折线。

填充颜色：cv.fillPoly(img, pts, color[, lineType[, shift[, offset]]]) → img

画出图像的轮廓：drawContours(InputOutputArray image, InputArrayOfArrays contours, int contourIdx, const Scalar& color, int thickness=1, int lineType=8, InputArray hierarchy=noArray(), int maxLevel=INT_MAX, Point offset=Point() )
函数参数详解：
其中第一个参数image表示目标图像，
第二个参数contours表示输入的轮廓组，每一组轮廓由点vector构成，
第三个参数contourIdx指明画第几个轮廓，如果该参数为负值，则画全部轮廓，
第四个参数color为轮廓的颜色，
第五个参数thickness为轮廓的线宽，如果为负值或CV_FILLED表示填充轮廓内部，
第六个参数lineType为线型，
第七个参数为轮廓结构信息，
第八个参数为maxLevel
'''
def demo():
    b1 = np.zeros((512, 512, 3), dtype=np.uint8)
    pts = np.array([[100,100],[350,100],[450,280],[320,450],[80,400]])
    # cv.fillPoly(b1,[pts],(255,0,255),8,0)
    cv.polylines(b1,[pts],True,(0,0,255),2,8,0)
    # cv.drawContours(b1,[pts],-1,(255,0,0),-1)
    cv.imshow("input", b1)
    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == '__main__':
    demo()