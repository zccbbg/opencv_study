import cv2 as cv
import numpy as np

'''
视频处理与保存
'''

def demo():
    cap = cv.VideoCapture("../images/test.mp4")
    # 分别获取视频的帧宽度、帧高度和帧率
    w = cap.get(cv.CAP_PROP_FRAME_WIDTH)
    h = cap.get(cv.CAP_PROP_FRAME_HEIGHT)
    fps = cap.get(cv.CAP_PROP_FPS)

    '''
    创建一个视频写入对象 out，用于将处理后的帧写入新的视频文件（"test1.mp4"）。参数包括：

    "../images/test1.mp4"：新视频文件的路径。
    cv.CAP_ANY：指定视频编码器，cv.CAP_ANY 表示自动选择合适的编码器。
    np.int32(cap.get(cv.CAP_PROP_FOURCC))：获取原视频文件的视频编码器，并将其转换为整数。
    fps：指定输出视频的帧率。
    (np.int32(w), np.int32(h))：指定输出视频的帧宽度和帧高度。
    True：表示输出视频使用彩色帧。
    '''
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