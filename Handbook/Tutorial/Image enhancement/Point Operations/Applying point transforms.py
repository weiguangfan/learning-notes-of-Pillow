from PIL import Image
with Image.open("../../../../female.jpg") as im:
    im.show()
    out = im.point(lambda i: i * 1.2)
    out.show()
"""
使用上述技术，你可以快速将任何简单的表达式应用到图像上。
你还可以结合point()和paste()方法来有选择地修改图像：
"""
