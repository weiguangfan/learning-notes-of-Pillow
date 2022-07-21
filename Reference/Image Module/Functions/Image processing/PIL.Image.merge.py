"""
PIL.Image.merge(mode, bands)
将一组单波段图像合并成一个新的多波段图像。

PARAMETERS:
    mode - 用于输出图像的模式。
        见Modes.

    bands - 一个序列，包含输出图像中每个波段的一个单波段图像。
            所有波段必须有相同的尺寸。

RETURNS:
    一个图像对象。

"""