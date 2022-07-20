"""
Image.transpose(method)
翻转图像（以90度为单位翻转或旋转）。

PARAMETERS:
    method - PIL.Image.Transpose.FLIP_LEFT_RIGHT,
            PIL.Image.Transpose.FLIP_TOP_BOTTOM,
            PIL.Image.Transpose.ROTATE_90
            PIL.Image.Transpose.ROTATE_180。
            PIL.Image.Transpose.ROTATE_270。
            PIL.Image.Transpose.TRANSPOSE
            或PIL.Image.Transpose.TRANSVERSE。
            中的一个。

RETURNS:
    返回该图像的翻转或旋转后的副本。

"""
# 这是通过使用PIL.Image.Transpose.FLIP_LEFT_RIGHT方法来翻转输入图像：
from PIL import Image
with Image.open("../../../female.jpg") as im:
    im.show()
    im_filpped1 = im.transpose(method=Image.FLIP_LEFT_RIGHT)
    im_filpped2 = im.transpose(method=Image.FLIP_TOP_BOTTOM)
    im_filpped3 = im.transpose(method=Image.ROTATE_90)
    im_filpped4 = im.transpose(method=Image.ROTATE_180)
    im_filpped5 = im.transpose(method=Image.ROTATE_270)
    im_filpped6 = im.transpose(method=Image.TRANSPOSE)
    im_filpped7 = im.transpose(method=Image.TRANSVERSE)
    im_filpped1.show()
    im_filpped2.show()
    im_filpped3.show()
    im_filpped4.show()
    im_filpped5.show()
    im_filpped6.show()
    im_filpped7.show()