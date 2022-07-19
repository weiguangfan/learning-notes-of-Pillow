"""
Image.resize(
            size,
            resample=None,
            box=None,
            reducing_gap=None)
返回该图像的一个调整后的副本。

PARAMETERS:
    size - 请求的尺寸，以像素为单位，是一个2元组：（宽度，高度）。

    resample - 一个可选的重采样过滤器。
            这可以是
            PIL.Image.Resampling.NEAREST、
            PIL.Image.Resampling.BOX、
            PIL.Image.Resampling.BILINEAR、
            PIL.Image.Resampling.HAMMING、
            PIL.Image.Resampling.BICUBIC
            或PIL.Image.Resampling.LANCZOS中的一种。
            如果图像的模式是 "1 "或 "P"，
            它总是被设置为PIL.Image.Resampling.NEAREST。
            如果图像模式指定了一个比特数，比如 "I;16"，
            那么默认的过滤器是PIL.Image.Resampling.NEAREST。
            否则，默认的过滤器是PIL.Image.Resampling.BICUBIC。
            见Filters.

    box - 一个可选的四元组浮点数，提供要缩放的源图像区域。
        这些值必须在（0, 0, width, height）矩形内。
        如果省略或None，则使用整个源。

    reducing_gap - 通过分两步调整图像的大小来进行优化。
                首先，使用reduce()将图像缩小整数倍。
                第二，使用常规重采样调整大小。
                最后一步改变大小不低于reducing_gap倍。
                reducing_gap可以是无（不执行第一步），或者应该大于1.0。
                reducing_gap越大，结果越接近于公平重采样。
                reducing_gap越小，调整大小就越快。
                reducing_gap大于或等于3.0时，在大多数情况下，其结果与公平重采样没有区别。
                默认值是None（没有优化）。

RETURNS:
    一个图像对象。

"""
from PIL import Image
with Image.open('../../../female.jpg') as im:
    im.show()
    print(im.width)
    print(im.height)
    (width, height) = (im.width // 2, im.height // 2)
    print(width)
    print(height)
    im_resized = im.resize((width,height))
    print(im_resized)
    im_resized.show()
