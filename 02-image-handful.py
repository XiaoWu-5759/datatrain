import numpy as np
from PIL import Image


filepath = "./shida.jpg"
def open_image(filepath):
    a = np.array(Image.open(filepath).convert("L"))
    # 利用灰度化，梯度处理图片
    depth = 10    # (0-100)
    grad = np.gradient(a)    # 取图片灰度的梯度值
    grad_x, grad_y = grad    # 分别取横纵图像梯度值
    grad_x = grad_x*depth/100.    # 取梯度的十分之一
    grad_y =grad_y * depth / 100.
    A = np.sqrt(grad_x**2 + grad_y**2 + 1.)

    uni_x = grad_x/A
    uni_y = grad_y/A
    uni_z = 1./A

    uni = (uni_x, uni_y, uni_z)
    return uni

def light_source(uni):
    uni_x, uni_y, uni_z = uni
    vec_el = np.pi/2.2    # 光源的俯视角度，弧度值
    vec_az = np.pi/4.    # 光源的方位角度，弧度制
    dx = np.cos(vec_el) * np.cos(vec_az)    # 光源对x轴的影响
    dy = np.cos(vec_el) * np.sin(vec_az)    # 光源对y轴的影响
    dz = np.sin(vec_el)     # 光源对z轴的影响

    b = 255*(dx*uni_x + dy*uni_y + dz*uni_z)   # 光源归一化
    b = b.clip(0,255)

# def save_image(b):
    im = Image.fromarray(b.astype('uint8'))
    im.save('./shida-hand.jpg')

# im = Image.fromarray(ndarray.astype('uint8'))
# AttributeError: 'NoneType' object has no attribute 'astype'

if __name__ == '__main__':
    a = open_image(filepath)
    b = light_source(a)
    # save_image(b)


