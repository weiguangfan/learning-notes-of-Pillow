"""
Image.quantize(
                colors=256,
                method=None,
                kmeans=0,
                palette=None,
                dither=Dither.FLOYDSTEINBERG)
将图像转换为具有指定颜色数量的 "P "模式。

PARAMETERS:
    colors - 所需的颜色数量，<=256

    method - Quantize.MEDIANCUT（中值切割）,
            Quantize.MAXCOVERAGE（最大覆盖率）,
            Quantize.FASTOCTREE（快速八叉树）,
            Quantize.LIBIMAGEQUANT
            (使用PIL.features.check_feature() with feature="libimagequant "检查支持情况）。

            默认情况下，将使用Quantize.MEDIANCUT。

            RGBA图像是个例外。
            Quantize.MEDIANCUT和Quantize.MAXCOVERAGE不支持RGBA图像，所以默认使用Quantize.FASTOCTREE来代替。

    kmeans - 整数

    palette - 量化为给定的PIL.Image.Image的调色板。

    dither - 抖动方法，在从 "RGB "模式转换为 "P "模式或从 "RGB "或 "L "转换为 "1 "时使用。
            可用的方法是Dither.NONE或Dither.FLOYDSTEINBERG（默认）。

RETURNS:
    一个新的图像







"""