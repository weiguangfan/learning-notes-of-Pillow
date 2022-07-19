"""
Image.convert(
                mode=None,
                matrix=None,
                dither=None,
                palette=Palette.WEB,
                colors=256)
返回该图像的一个转换副本。
对于 "P "模式，该方法通过调色板对像素进行转换。
如果省略了模式，就会选择一种模式，这样图像中的所有信息和调色板就可以不用调色板来表示。

目前的版本支持 "L"、"RGB "和 "CMYK "之间所有可能的转换。
矩阵参数只支持 "L "和 "RGB"。

将灰度（"L"）或 "RGB "图像转换为双水平（模式 "1"）图像的默认方法使用Floyd-Steinberg抖动来接近原始图像的亮度水平。
如果抖动为 "无"，所有大于127的值都被设置为255（白色），所有其他值为0（黑色）。
要使用其他阈值，请使用point()方法。

当从 "RGBA "转换到 "P "而没有矩阵参数时，
这将把操作传递给quantize()，而抖动和调色板被忽略。

PARAMETERS:
    mode - 请求的模式。
        参见Modes.

    matrix - 一个可选的转换矩阵。
            如果给定，这应该是包含浮点值的4-或12-元组。

    dither - 抖动方法，
            在从模式 "RGB "转换到 "P "或从 "RGB "或 "L "转换到 "1 "时使用。
            可用的方法是Dither.NONE或Dither.FLOYDSTEINBERG（默认）。
            注意，当提供矩阵时不使用这个方法。

    palette - 从模式 "RGB "转换到 "P "时使用的调色板。
        可用的调色板是Palette.WEB或Palette.ADAPTIVE。

    colors - 用于Palette.ADAPTIVE调色板的颜色数量。
        默认为256。

RETURN TYPE:
    图像

RETURNS:
    一个图像对象。

"""