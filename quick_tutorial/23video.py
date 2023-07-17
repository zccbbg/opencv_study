import cv2 as cv
import numpy as np

'''
视频处理与保存
'''

def demo():
    cap = cv.VideoCapture("../images/test.mp4")
    w = cap.get(cv.CAP_PROP_FRAME_WIDTH)
    h = cap.get(cv.CAP_PROP_FRAME_HEIGHT)
    fps = cap.get(cv.CAP_PROP_FPS)
    out = cv.VideoWriter("../images/test1.mp4", cv.CAP_ANY, np.int32(cap.get(cv.CAP_PROP_FOURCC)), fps, (np.int32(w), np.int32(h)),True)
    print(w, h, fps)
    while True:
        ret, frame = cap.read()
        if ret is not True:
            break
        cv.imshow("frame", frame)
        hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
        cv.imshow("result", hsv)
        out.write(hsv)
        c = cv.waitKey(10)
        if c == 27:
            break
    cv.destroyAllWindows()

    out.release()
    cap.release()

if __name__ == '__main__':
    demo()