"""
class PIL.ImageFilter.Kernel(
                            size,
                            kernel,
                            scale=None,
                            offset=0)
创建一个卷积核。
目前的版本只支持3x3和5x5的整数和浮点内核。

在当前版本中，内核只能应用于 "L "和 "RGB "图像。

PARAMETERS:
    size - 核心尺寸，以（宽度，高度）的形式给出。
        在当前版本中，它必须是（3,3）或（5,5）。

    kernel - 一个包含内核权重的序列。

    scale - 缩放系数。
            如果给定，
            每个像素的结果都要除以这个值。
            默认是内核权重的总和。

    offset - 偏移。
            如果给定，
            在结果除以比例因子后，
            这个值将被添加到结果中。

"""