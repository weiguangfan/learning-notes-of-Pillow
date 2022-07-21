from PIL import Image
with Image.open("../../../../female.jpg") as im:
    im.show()
    im.seek(1)
    try:
        while 1:
            im.seek(im.tell() + 1)
    except EOFError:
        pass
"""
从这个例子中可以看出，
当序列结束时，
你会得到一个 EOFError 异常。

下面的类可以让你使用for语句来循环处理这个序列：
"""


