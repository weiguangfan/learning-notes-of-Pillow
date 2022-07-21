"""
Image.point(lut, mode=None)
通过一个查找表或函数映射该图像。

PARAMETERS:
    lut - 一个查找表，
        包含图像中每个波段的256（或65536，如果self.mode=="I "和mode=="L"）值。
        可以用一个函数来代替，
        它应该只接受一个参数。
        该函数对每个可能的像素值都会被调用一次，
        得到的表格会应用于图像的所有波段。

    mode - 输出模式（默认与输入相同）。
        在当前版本中，
        只有当源图像的模式为 "L "或 "P"，
        而输出的模式为 "1 "
        或源图像的模式为 "I "而输出的模式为 "L "时才能使用。

RETURNS:
    一个图像对象。
"""
# 它也可以是一个ImagePointHandler对象。
from PIL import Image
class Example(Image.ImagePointHandler):
    def point(self,data):
        pass