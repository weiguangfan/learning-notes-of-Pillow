from PIL import Image
box = (100, 100, 400, 400)
with Image.open("../../../female.jpg") as im:
    im.show()
    region = im.crop(box)
    region.show()

"""
该区域由一个4元组定义，其中坐标为（左、上、右、下）。
Python Imaging Library使用的坐标系是左上角的（0，0）。
还要注意，坐标指的是像素之间的位置，所以上例中的区域正好是300x300像素。

现在可以对该区域进行一定的处理并粘贴回来。
"""