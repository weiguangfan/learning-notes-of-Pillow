"""
Image.transform(
                size,
                method,
                data=None,
                resample=Resampling.NEAREST,
                fill=1,
                fillcolor=None)

对这个图像进行变换。
这个方法创建一个新的图像，
其大小和原始图像的模式相同，
并使用给定的变换将数据复制到新的图像上。

PARAMETERS:
    size - 输出的尺寸。

    method - 变换方法。
            这是PIL.Image.Transform.EXTENT（切出一个矩形子区域）、
            PIL.Image.Transform.AFFINE（仿射变换）中的一种、
            PIL.Image.Transform.PERSPECTIVE（透视变换）、
            PIL.Image.Transform.QUAD（将一个四边形映射为一个矩形）、
            或PIL.Image.Transform.MESH（在一次操作中映射若干源四边形）中的一种。

    data - 转换方法的额外数据。

    resample - 可选的重采样过滤器。
            它可以是PIL.Image.Resampling.NEAREST（使用最近的邻居）、
            PIL.Image.Resampling.BILINEAR（在2x2环境中进行线性插值）、
            或PIL.Image.BICUBIC（4x4环境下的立方样条插值）中的一个。
            如果省略，或者如果图像有模式 "1 "或 "P"。
            它被设置为PIL.Image.Resampling.NEAREST。
            见Filters.

    fill - 如果方法是一个ImageTransformHandler对象，
        这就是传递给它的参数之一。
        否则，它将不被使用。

    fillcolor - 可选的填充颜色，
                用于输出图像中变换之外的区域。

RETURNS:
    一个图像对象。
"""
from PIL import Image


# 它也可以是一个ImageTransformHandler对象。
class Example(Image.ImageTransformHandler):

    def transform(self,size,data,resample,fill=1):
        pass

# 它也可以是一个具有method.getdata方法的对象，该方法返回一个提供新方法和数据值的元组。
class Example1:
    def getdata(self):
        method = Image.Transform.EXTENT
        data = (0,0,100,100)
        return method,data
