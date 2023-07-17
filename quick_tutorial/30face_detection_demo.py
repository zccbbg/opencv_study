import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
'''
实时人脸
'''

model_bin = "../models/face_detector/opencv_face_detector_uint8.pb"
config_text = "../models/face_detector/opencv_face_detector.pbtxt";
def demo():
    net = cv.dnn.readNetFromTensorflow(model=model_bin, config=config_text)
    cap = cv.VideoCapture("自己找个有人脸的视频")
    while True:
        ret, frame = cap.read()
        h, w, c = frame.shape
        if ret is not True:
            break
        # NCHW
        blob = cv.dnn.blobFromImage(frame, 1.0, (300, 300), (104.0, 177.0, 123.0), False, False)
        net.setInput(blob)
        outs = net.forward()  # 1x1xNx7
        for detection in outs[0, 0, :, :]:
            score = float(detection[2])
            if score > 0.5:
                left = detection[3] * w
                top = detection[4] * h
                right = detection[5] * w
                bottom = detection[6] * h
                cv.rectangle(frame, (np.int(left), np.int(top)), (np.int(right), np.int(bottom)), (0, 0, 255), 2, 8, 0)
        cv.imshow("frame", frame)
        c = cv.waitKey(1)
        if c == 27:
            break
    cv.destroyAllWindows()
    cap.release()


if __name__ == '__main__':
    demo()