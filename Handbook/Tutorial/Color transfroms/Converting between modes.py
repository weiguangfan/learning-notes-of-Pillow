from PIL import Image
with Image.open("../../../female.jpg") as im:
    im.show()
    im = im.convert("L")
    im.show()
"""
该库支持每个支持的模式与 "L "和 "RGB "模式之间的转换。
要在其他模式之间转换，你可能必须使用一个中间图像（通常是 "RGB "图像）。
"""

