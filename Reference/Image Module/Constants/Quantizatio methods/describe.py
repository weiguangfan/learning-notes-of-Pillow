"""
用于指定quantize()方法要使用的量化方法。
class PIL.Image.Quantize
MEDIANCUT
    中位数切割。
    默认方法，除了RGBA图像。
    此方法不支持RGBA图像。

MAXCOVERAGE
    最大覆盖率。
    此方法不支持RGBA图像。

FASTOCTREE
    快速八叉树。
    RGBA图像的默认方法。

LIBIMAGEQUANT
    libimagequant

    使用PIL.features.check_feature()检查支持情况，feature="libimagequant"。

"""