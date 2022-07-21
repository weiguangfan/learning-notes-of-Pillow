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
    # im2 = im.filter(ImageFilter.MinFilter(3))
    # im3 = im.filter(ImageFilter.MinFilter)
    im1.show()
    im2.show()
    # im3.show()
    im4.show()
    im5.show()


# EDGE_ENHANCE
#
# EDGE_ENHANCE_MORE
#
# EMBOSS
#
# FIND_EDGES
#
# SHARPEN
#
# SMOOTH
#
# SMOOTH_MORE


