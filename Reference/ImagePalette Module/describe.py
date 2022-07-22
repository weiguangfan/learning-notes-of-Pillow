"""
ImagePalette模块包含一个同名的类，
用来表示调色板映射的图像的调色板。

ImagePalette类有几个方法，
但它们都被标记为 "实验性"。
随你怎么理解。
这个链接在那里是有原因的。

class PIL.ImagePalette.ImagePalette(mode='RGB', palette=None, size=0)
调色板映射图像的调色板

PARAMETERS:
    mode - 调色板要使用的模式。
        见Modes。
        默认为 "RGB"。

    palette - 一个可选的调色板。
        如果给定的话，它必须是一个字节数、一个数组或一个0-255之间的ints列表。
        该列表必须由一种颜色的所有通道组成，然后是下一种颜色（例如：RGBRGBRGB）。
        默认为空调色板。
Methods:
    getcolor(color, image=None)
        给定一个rgb元组，分配调色板条目。
        这个方法是实验性的。

    getdata()
        以适合低级别的im.putpalette基元的格式获取调色板内容。
        这个方法是实验性的。

    save(fp)
        将调色板保存为文本文件。
        这个方法是实验性的。

    tobytes()
        将调色板转换为字节。
        这个方法是实验性的。

    tostring()
        将调色板转换为字符串。
        这个方法是实验性的。
"""