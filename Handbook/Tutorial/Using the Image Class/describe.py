"""
Python Imaging Library 中最重要的类是 Image 类，定义在同名的模块中。
你可以通过几种方式来创建这个类的实例；
或者从文件中加载图像，处理其他图像，或者从头开始创建图像。


"""
from PIL import Image

# 要从文件中加载图像，请使用 Image 模块中的 open() 函数。
im = Image.open('../../../female.jpg')
print(im)
# 如果成功，这个函数返回一个图像对象。现在你可以使用实例属性来检查文件内容:
print(im.mode)
print(im.size)
print(im.format)

