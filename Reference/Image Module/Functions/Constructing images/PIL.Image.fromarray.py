"""
PIL.Image.fromarray(obj, mode=None)
从一个输出数组接口的对象中创建一个图像存储器（使用缓冲区协议）。

如果obj不是连续的，那么就调用tobytes方法并使用frombuffer()。

PARAMETERS:
    obj - 具有数组接口的对象

    mode - 读取obj时使用的可选模式。
        如果没有，将由类型决定。

RETURNS:
    一个图像对象。

"""
import numpy as np
from PIL import Image

# 如果你在NumPy中拥有一个图像:
# im = Image.open("../../../../female.jpg")
# print(im)
# im.show()
# a = np.array(im)
# print(a)
# 然后可以用这个方法将其转换为Pillow图像:
# im2 = Image.fromarray(a)
# print(im2)
# im2.show()

# 这不会用于读取后的数据转换，但会用于改变数据的读取方式:
b = np.full((1,1),300)
print(b)
im = Image.fromarray(b, mode='L')
print(im)
print(im.getpixel((0, 0)))
im2 = Image.fromarray(b, mode="RGB")
print(im2)
print(im2.getpixel((0, 0)))