"""
class PIL.ImageTk.PhotoImage(image=None, size=None, **kw)
一个Tkinter-compatible的照片图像。
它可以在Tkinter期望有图像对象的地方使用。
如果图像是RGBA图像，alpha为0的像素被视为透明。

构造函数接收一个PIL图像，或者一个模式和一个尺寸。
另外，你也可以使用文件或数据选项来初始化照片图像对象。

PARAMETERS:
    image - 一个PIL图像，或者一个模式字符串。
            如果使用模式字符串，还必须给出一个尺寸。

    size - 如果第一个参数是一个模式字符串，这定义了图像的大小。

    file - 从一个文件名加载图像（使用Image.open(file)）。

    data - 一个包含图像数据的8位字符串（如从图像文件加载）。
Methods:
   height()
    获取图像的高度。

    RETURNS:
        高度，单位是像素。

   paste(im, box=None)
    将一个PIL图像粘贴到照片图像中。
    注意，如果显示照片图像，这可能会非常慢。

    PARAMETERS:
        im - 一个PIL图像。
            其大小必须与目标区域相匹配。
            如果模式不匹配，该图像将被转换为the bitmap image的模式。

        box - 废弃的。
            这个参数将在Pillow 10（2023-07-01）中删除。

   width()
    获取图像的宽度。

    RETURNS:
        宽度，单位是像素。

"""