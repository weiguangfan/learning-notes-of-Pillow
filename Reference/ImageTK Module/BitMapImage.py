"""
class PIL.ImageTk.BitmapImage(image=None, **kw)
一个Tkinter-compatible的bitmap image。
它可以在Tkinter期望有图像对象的地方使用。

给定的图像必须有模式 "1"。
值为0的像素被视为透明。
选项，如果有的话，会传递给Tkinter。
最常用的选项是foreground，
它用于指定非透明部分的颜色。
有关如何指定颜色的信息，请参阅Tkinter文档。

PARAMETERS:
    image - 一个PIL图像。
Methods:
   height()
    获取图像的高度。

    RETURNS:
        高度，单位是像素。

   width()
    获取图像的宽度。

    RETURNS:
        宽度，单位是像素。


"""