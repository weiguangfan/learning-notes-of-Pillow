"""
Image.crop(box=None)
返回这个图像的一个矩形区域。
这个盒子是一个4元组，定义了左、上、右和下像素坐标。
参见Coordinate System.

注意：在Pillow 3.4.0之前，这是一个懒惰的操作。

PARAMETERS:
    box - 裁剪的矩形，是一个（左、上、右、下）的元组。

RETURN TYPE:
    图像

RETURNS:
    一个图像对象。

这将用提供的坐标裁剪输入的图像。
"""
from PIL import Image
with Image.open('../../../female.jpg') as im:
    print(im.size)
    im.show()
    # 图像模块的裁剪方法需要四个坐标作为输入。
    # 右边也可以表示为（左+宽），下面可以表示为（上+高）。
    (left, upper, right, lower) = (20,20,100,100)
    # 在这里，图像 "im "被裁剪并分配给新的变量im_crop
    im_crop = im.crop((left,upper,right,lower))
    print(im_crop.size)
    im_crop.show()