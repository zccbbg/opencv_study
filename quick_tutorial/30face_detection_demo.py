import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
'''
实时人脸
'''
# 指定训练好的人脸检测模型的二进制文件路径。
model_bin = "../models/face_detector/opencv_face_detector_uint8.pb"
# 指定人脸检测模型的配置文件的路径，该文件描述了模型的网络结构等信息。
config_text = "../models/face_detector/opencv_face_detector.pbtxt";
def demo():
    '''
    使用 OpenCV 的深度学习模块中的 cv.dnn.readNetFromTensorflow 函数加载了预训练的人脸检测模型。
    '''
    net = cv.dnn.readNetFromTensorflow(model=model_bin, config=config_text)
    cap = cv.VideoCapture("../images/test.mp4")
    while True:
        ret, frame = cap.read()
        if ret is not True:
            break
        h, w, c = frame.shape
        # NCHW
        '''
        将图像转换为神经网络输入的格式。
        这个函数会生成一个四维的 blob，其中包含了经过预处理的图像信息。
        '''
        blob = cv.dnn.blobFromImage(frame, 1.0, (300, 300), (104.0, 177.0, 123.0), False, False)
        # 将 blob 设置为神经网络的输入。
        net.setInput(blob)
        # 通过神经网络进行前向传播，得到输出。这里的输出包含了检测到的人脸框的信息。
        outs = net.forward()  # 1x1xNx7
        # 遍历每个检测到的人脸框。
        for detection in outs[0, 0, :, :]:
            # 如果置信度超过设定的阈值（这里设定为0.5），则认为检测到了有效的人脸。
            score = float(detection[2])
            if score > 0.5:
                # 计算检测到人脸框的左上角和右下角坐标
                left = detection[3] * w
                top = detection[4] * h
                right = detection[5] * w
                bottom = detection[6] * h
                # 在图像上绘制矩形框，标记检测到的人脸。
                cv.rectangle(frame, (int(left), int(top)), (int(right), int(bottom)), (0, 0, 255), 2, 8, 0)
        cv.imshow("frame", frame)
        c = cv.waitKey(1)
        if c == 27:
            break
    cv.destroyAllWindows()
    cap.release()


if __name__ == '__main__':
    demo()