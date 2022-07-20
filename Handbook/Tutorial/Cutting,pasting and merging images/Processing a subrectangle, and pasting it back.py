from PIL import Image
box = (100, 100, 400, 400)
with Image.open("../../../female.jpg") as im:
    im.show()
    print(im.size)
    region = im.crop(box)
    region.show()
    region = region.transpose(Image.ROTATE_180)
    region.show()
    im.paste(region, box)
    im.show()
"""
当把区域粘贴回来时，区域的大小必须与给定的区域完全匹配。
此外，该区域不能延伸到图像之外。
然而，原始图像和区域的模式不需要匹配。
如果它们不匹配，该区域在被粘贴之前会被自动转换（详见下面关于颜色转换的部分）。

这里有一个额外的例子:
"""