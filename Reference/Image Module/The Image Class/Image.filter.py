"""
Image.filter(filter)
使用给定的过滤器过滤此图像。
有关可用过滤器的列表，请参见ImageFilter模块。

PARAMETERS:
    filter - 过滤器内核。

RETURNS:
    一个图像对象。
"""
from PIL import Image, ImageFilter
with Image.open("../../../female.jpg") as im:
    im.show()
    im1 = im.filter(ImageFilter.BLUR)
    im2 = im.filter(ImageFilter.CONTOUR)
    # im3 = im.filter(ImageFilter.DETAIL)
    im4 = im.filter(ImageFilter.EDGE_ENHANCE)
    im5 = im.filter(ImageFilter.EDGE_ENHANCE_MORE)
    im6 = im.filter(ImageFilter.EMBOSS)
    im7 = im.filter(ImageFilter.FIND_EDGES)
    im8 = im.filter(ImageFilter.SHARPEN)
    im9 = im.filter(ImageFilter.SMOOTH)
    im10 = im.filter(ImageFilter.SMOOTH_MORE)
    im11 = im.filter(ImageFilter.MinFilter(3))
    im12 = im.filter(ImageFilter.MinFilter)
    im13 = im.filter(ImageFilter.MaxFilter)
    im14 = im.filter(ImageFilter.MedianFilter)
    im15 = im.filter(ImageFilter.ModeFilter)
    # im1.show()
    # im2.show()
    # im3.show()
    # im4.show()
    # im5.show()
    # im6.show()
    # im7.show()
    # im8.show()
    # im9.show()
    # im10.show()
    # im11.show()
    im12.show()
    im13.show()
    im14.show()
    im15.show()
