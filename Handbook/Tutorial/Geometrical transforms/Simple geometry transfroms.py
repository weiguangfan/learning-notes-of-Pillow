from PIL import Image
with Image.open("../../../female.jpg") as im:
    im.show()
    print(im.size)
    out1 = im.resize((128,128))
    out1.show()
    out2 = im.rotate(45)
    out2.show()

"""
要以90度为单位旋转图像，
你可以使用rotate()方法或transpose()方法。
后者也可以用来围绕水平或垂直轴翻转图像。
"""