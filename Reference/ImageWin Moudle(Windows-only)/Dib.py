"""
class PIL.ImageWin.Dib(image, size=None)
一个具有指定模式和尺寸的Windows bitmap。
模式可以是 "1"、"L"、"P "或 "RGB "中的一个。

如果显示需要调色板，这个构造函数会创建一个合适的调色板，并将其与图像关联起来。
对于 "L "图像，将分配128个灰度等级。
对于 "RGB "图像，使用一个6x6x6的颜色立方体，以及20个灰度级。

为了确保调色板在Windows下正常工作，你必须在Windows的某些事件中调用调色板方法。

PARAMETERS:
    image - 一个PIL图像，或者一个模式字符串。
        如果使用模式字符串，还必须给出一个尺寸。
        模式可以是 "1"、"L"、"P "或 "RGB "之一。

    size - 如果第一个参数是一个模式字符串，这定义了图像的大小。

Methods:
    draw(handle, dst, src=None)
        与expose相同，但允许你指定绘制图像的位置，以及绘制图像的哪一部分。

        目标区域和源区域是以4元组矩形的形式给出的。
        如果省略了源，整个图像就被复制了。
        如果源区和目的区有不同的大小，图像的大小会根据需要调整。

    expose(handle)
        将bitmap内容复制到设备上下文。

        PARAMETERS:
            handle - 设备上下文 (HDC)，
                    铸成一个 Python 整数，
                    或者一个 HDC 或 HWND 实例。
                    在PythonWin中，你可以使用CDC.GetHandleAttrib()来获得一个合适的句柄。

    frombytes(buffer)
        从字节数据加载显示内存内容。

        PARAMETERS:
            buffer - 包含显示数据的缓冲区（通常是从tobytes()返回的数据）。

    paste(im, box=None)
        将一个PIL图像粘贴到 bitmap中。

        PARAMETERS:
            im - 一个PIL图像。尺寸必须与目标区域匹配。如果模式不匹配，该图像将被转换为bitmap图像的模式。

            box - 一个定义左、上、右和下像素坐标的4元组。见 Coordinate System。如果给出None而不是一个元组，则假定所有的图像都是。

    query_palette(handle)
        在给定的设备上下文中安装与图像相关的调色板。

        这个方法应该在Windows的QUERYNEWPALETTE和PALETTECHANGED事件中被调用。如果这个方法返回一个非零值，说明一个或多个显示调色板条目被改变，图像应该被重新绘制。

        PARAMETERS:
            handle - 设备上下文(HDC)，铸成一个Python整数，或一个HDC或HWND实例。

        RETURNS:
            如果一个或多个条目被改变，则为真值（这表明图像应该被重绘）。

    tobytes()
        拷贝显示内存内容到字节对象。

        RETURNS:
            一个包含显示数据的字节对象。

"""