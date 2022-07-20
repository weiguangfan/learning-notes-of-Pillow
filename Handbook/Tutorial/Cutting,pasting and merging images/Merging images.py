from PIL import Image
box1 = (50, 50, 200, 200)
box2 = (100, 100, 400, 400)


def merge(im1,im2):
    w = im1.size[0] + im2.size[0]
    h = max(im1.size[1], im2.size[1])
    im = Image.new("RGBA", (w, h,))
    im.show()
    im.paste(im1)
    im.show()
    im.paste(im2, (im1.size[0], 0))
    im.show()
    return im


with Image.open("../../../female.jpg") as im:
    im.show()
    im_box1 = im.crop(box1)
    print(im_box1.size)
    im_box1.show()
    im_box2 = im.crop(box2)
    print(im_box2.size)
    im_box2.show()
    im_merge = merge(im_box1,im_box2)

"""
对于更高级的技巧，粘贴方法也可以接受一个透明度掩码作为一个可选参数。
在这个掩码中，数值255表示被粘贴的图像在该位置是不透明的（也就是说，被粘贴的图像应该被原样使用）。
值为0表示被粘贴的图像是完全透明的。
介于两者之间的数值表示不同的透明程度。
例如，粘贴一个RGBA图像并将其作为掩码，将粘贴图像的不透明部分，但不粘贴其透明背景。

Python Imaging Library还允许你处理一个多波段图像的各个波段，如RGB图像。
分割方法创建了一组新的图像，每一个都包含了原始多波段图像的一个波段。
合并函数接收一个模式和一个图像的元组，并将它们合并成一个新的图像。
下面的例子是交换一个RGB图像的三个波段。
"""