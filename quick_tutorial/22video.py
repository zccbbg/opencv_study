import cv2 as cv
import numpy as np

'''
摄像头使用
'''

def demo():
    # 打开默认的摄像头（通常是编号为0的摄像头）。如果有多个摄像头，你可以尝试更改参数来选择其他摄像头。
    cap = cv.VideoCapture(0)
    while True:
        # 从摄像头捕获一帧图像。ret 是一个布尔值，表示是否成功读取了图像，frame 是捕获到的图像。
        ret,frame = cap.read()
        if ret is True:
            # 每帧之间暂停10毫秒。
            cv.imshow("frame",frame)
            c = cv.waitKey(10)
            if c == 27:
                break
    cv.destroyAllWindows()

if __name__ == '__main__':
    demo()