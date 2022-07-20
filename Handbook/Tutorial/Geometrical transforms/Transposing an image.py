from PIL import Image
with Image.open("../../../female.jpg") as im:
    im.show()
    im_filpped1 = im.transpose(method=Image.FLIP_LEFT_RIGHT)
    im_filpped2 = im.transpose(method=Image.FLIP_TOP_BOTTOM)
    im_filpped3 = im.transpose(method=Image.ROTATE_90)
    im_filpped4 = im.transpose(method=Image.ROTATE_180)
    im_filpped5 = im.transpose(method=Image.ROTATE_270)
    im_filpped1.show()
    im_filpped2.show()
    im_filpped3.show()
    im_filpped4.show()
    im_filpped5.show()
"""
transpose(ROTATE)操作也可以与rotate()操作相同，
只要expand标志为真，就可以对图像的大小进行同样的改变。

一种更普遍的图像变换形式可以通过transform()方法进行。
"""