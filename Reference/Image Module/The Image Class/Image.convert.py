"""
Image.convert(
                mode=None,
                matrix=None,
                dither=None,
                palette=Palette.WEB,
                colors=256)
返回该图像的一个转换副本。
对于 "P "模式，
该方法通过调色板对像素进行转换。
如果省略了模式，
就会选择一种模式，
这样图像中的所有信息和调色板就可以不用调色板来表示。

目前的版本支持 "L"、"RGB "和 "CMYK "之间所有可能的转换。
matrix参数只支持 "L "和 "RGB"。

将灰度（"L"）或 "RGB "图像转换为双水平（模式 "1"）图像的默认方法,
使用Floyd-Steinberg抖动来接近原始图像的亮度水平。
如果dither为 "None"，
所有大于127的值都被设置为255（白色），
所有其他值为0（黑色）。
要使用其他阈值，
请使用point()方法。

当从 "RGBA "转换到 "P "而没有matrix参数时，
这将把操作传递给quantize()，
而dither和palette被忽略。

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
# 当把彩色图像转换为灰度（模式 "L"）时，该库使用ITU-R 601-2 luma变换:
from PIL import Image
rgb2xyz = (
    0.412453, 0.357580, 0.180423, 0,
    0.212671, 0.715160, 0.072169, 0,
    0.019334, 0.119193, 0.950227, 0
)
with Image.open("../../../female.jpg") as im:
    im.show()
    print(im.filename)
    print(im.mode)
    print(im.format)
    print(im.palette)
    print(getattr(im, "is_animated", False))
    print(getattr(im, "n_frames", 1))
    print(im.size)
    print(im.width)
    print(im.height)
    print(im.info)
    print(im.getbands())
    print(im.getcolors())
    print(im.getdata())
    # print(list(im.getdata()))
    print(im.getdata(0))
    # print(im.getdata(1))
    # print(im.getdata(2))
    print(im.getpixel((100, 100)))
    print(im.getprojection())
    print(im.getpalette())
    a,b,c = im.getpixel((100,100))
    print(a,b,c)
    im.putpixel((100,100),(0,0,0))
    print(im.getpixel((100, 100)))
    print(im.getextrema())
    im_getchannel = im.getchannel
    print(im_getchannel)
    im_getcha = im.getchannel(0)
    print(im_getcha)
    # im_getcha = im.getchannel(1)
    # im_getcha = im.getchannel(2)
    print(im_getcha.getcolors())
    print(im_getcha.getextrema())
    print(im_getcha.getbands())
    print(im_getcha.getdata())
    print(im_getcha.getpalette())
    print(im_getcha.mode)
    print(im_getcha.format)
    print(im_getcha.size)
    print(im_getcha.palette)
    print(im_getcha.info)
    # im_getcha.show()
    # L = R * 299/1000 + G * 587/1000 + B * 114/1000
    # print(L)

# 下面的例子将一个RGB图像（根据ITU-R 709线性校准，使用D65发光体）转换为CIE XYZ色彩空间。
    out = im.convert("RGB", rgb2xyz)
    out.show()
