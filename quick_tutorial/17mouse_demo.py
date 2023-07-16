import cv2 as cv
import numpy as np

'''
鼠标点击

'''
b1 = cv.imread("../images/test.jpg")
img = np.copy(b1)
x1 =-1
y1 = -1
x2 =-1
y2 =-1
def mouse_drawing(event,x,y,flags,param):
    global x1,y1,x2,y2
    if event == cv.EVENT_LBUTTONDOWN:
        x1 = x
        y1 = y
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
    cv.setMouseCallback("mouse_demo",mouse_drawing)
    while True:
        cv.imshow("mouse_demo",b1)
        c = cv.waitKey(10)
        if c == 27:
            break
    cv.destroyAllWindows()

if __name__ == '__main__':
    demo()