#
# -*- coding:utf-8 -*-

import numpy as np

from PIL import Image


# 计算A2 + B3,其中，A和B是一维数组
def pySum():
    a = [0, 1, 2, 3, 4]
    b = [9, 8, 7, 6, 5]
    c = []
    for i in range(len(a)):
        c.append(a[i] ** 2 + b[i] ** 3)
    return c

def npSum():
    a = np.array([0, 1, 2, 3, 4])
    b = np.array([9, 8, 7, 6, 5])

    c = a**2 + b**3
    return c

def show_image():
    filepath = "./shida.jpg"
    im1 = np.array(Image.open(filepath))
    im2 = np.array(Image.open(filepath).convert("L"))
    print(im1.shape, im1.dtype)
    # print(im2)
    # 保存灰度图像
    im2 = Image.fromarray(im2)
    im2.save("./shida-hui.jpg")


if __name__ == '__main__':
    # print(pySum())
    # print(npSum())
    show_image()