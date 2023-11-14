import cv2 as cv
import numpy as np

'''
鼠标点击

'''
b1 = cv.imread("../images/test.jpg")
img = np.copy(b1)
# 用于存储矩形的起始点 (x1, y1) 和结束点 (x2, y2) 的坐标。
x1 =-1
y1 = -1
x2 =-1
y2 =-1

# 一个回调函数，用于处理鼠标事件
def mouse_drawing(event,x,y,flags,param):
    global x1,y1,x2,y2
    # 当左键按下时 (cv.EVENT_LBUTTONDOWN)，记录当前鼠标位置为矩形的起始点 (x1, y1)。
    if event == cv.EVENT_LBUTTONDOWN:
        x1 = x
        y1 = y
    # 当鼠标移动时 (cv.EVENT_MOUSEMOVE)，如果已经有起始点，记录当前位置为矩形的结束点 (x2, y2)，然后在图像上绘制红色矩形。
    if event == cv.EVENT_MOUSEMOVE:
        if x1<0 or y1<0:
            return
        x2 = x
        y2 = y
        dx = x2 -x1
        dy = y2 -y1
        if dx>0 and dy>0:
            b1[:,:,:] = img[:,:,:]
            cv.rectangle(b1,(x1,y1),(x2,y2),(0,0,255),2,8,0)
    # 当左键释放时 (cv.EVENT_LBUTTONUP)，如果已经有起始点，记录当前位置为矩形的结束点 (x2, y2)，然后在图像上绘制红色矩形并重置起始和结束点。
    if event == cv.EVENT_LBUTTONUP:
        if x1<0 or y1<0:
            return
        x2 = x
        y2 = y
        dx = x2 - x1
        dy = y2 - y1
        if dx > 0 and dy > 0:
            b1[:, :, :] = img[:,:,:]
            cv.rectangle(b1, (x1, y1), (x2, y2), (0, 0, 255), 2, 8, 0)
        x1 = -1
        y1 = -1
        x2 = -1
        y2 = -1
def demo():
    cv.namedWindow("mouse_demo",cv.WINDOW_AUTOSIZE)
    # 将鼠标回调函数 mouse_drawing 注册给 "mouse_demo" 窗口。
    cv.setMouseCallback("mouse_demo",mouse_drawing)
    while True:
        cv.imshow("mouse_demo",b1)
        c = cv.waitKey(10)
        if c == 27:
            break
    cv.destroyAllWindows()

if __name__ == '__main__':
    demo()