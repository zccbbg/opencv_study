import cv2 as cv
import numpy as np

'''
图像旋转
'''

def demo():
    src = cv.imread("../images/test.jpg")
    cv.imshow("input", src)
    # 获取原始图像的高度（h）、宽度（w）和通道数（c）。
    h, w, c = src.shape
    # 创建一个2x3的矩阵 M，用于存储仿射变换矩阵
    M = np.zeros((2, 3), dtype=np.float32)
    # 计算旋转角度为45度时的cosine和sine值。
    alpha = np.cos(np.pi / 4.0)
    beta = np.sin(np.pi / 4.0)
    print("alpha : ", alpha)

    # 初始旋转矩阵
    # 对角线元素为cosine值，表示沿着x和y轴的缩放。
    M[0, 0] = alpha
    M[1, 1] = alpha
    # 非对角线元素为sine和负sine值，表示旋转。
    M[0, 1] = beta
    M[1, 0] = -beta
    # 原始图像中心的坐标。
    cx = w / 2
    cy = h / 2
    # 平移量，使得旋转后的图像能够完整显示在窗口中。
    tx = (1 - alpha) * cx - beta * cy
    ty = beta * cx + (1 - alpha) * cy
    # 平移部分
    M[0, 2] = tx
    M[1, 2] = ty

    # 算旋转后图像的边界框的宽度和高度。
    bound_w = int(h * np.abs(beta) + w * np.abs(alpha))
    bound_h = int(h * np.abs(alpha) + w * np.abs(beta))

    # 添加中心位置迁移
    M[0, 2] += bound_w / 2 - cx
    M[1, 2] += bound_h / 2 - cy
    # 进行仿射变换，即旋转操作。M 是变换矩阵，(bound_w, bound_h) 是输出图像的大小。
    dst = cv.warpAffine(src, M, (bound_w, bound_h))
    cv.imshow("rotate without cropping", dst)
    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == '__main__':
    demo()