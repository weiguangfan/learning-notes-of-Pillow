"""
Image.thumbnail(
                size,
                resample=Resampling.BICUBIC,
                reducing_gap=2.0)
把这个图像变成一个缩略图。
这个方法将图像修改为包含一个自身的缩略图版本，不大于给定的尺寸。
这个方法计算一个合适的缩略图尺寸以保留图像的长宽，
调用draft()方法来配置文件阅读器（如果适用），
最后调整图像的大小。

注意，这个函数在原地修改了图像对象。
如果你也需要使用全分辨率的图像，
请将此方法应用于原始图像的一个copy()。

PARAMETERS:
    size - 要求的尺寸。

    resample - 可选的重采样过滤器。
            可以是PIL.Image.Resampling.NEAREST中的一个。
            PIL.Image.Resampling.BOX.PIL.Image.Resampling的其中之一。
            PIL.Image.Resampling.BILINEAR。
            PIL.Image.Resampling.HAMMING。
            PIL.Image.Resampling.BICUBIC
            或PIL.Image.Resampling.LANCZOS。
            如果省略，它默认为PIL.Image.Resampling.BICUBIC。
            (在2.5.0版本之前是PIL.Image.Resampling.NEAREST)。
            见: Filters.

    reducing_gap - 通过分两步调整图像的大小来进行优化。
                首先，对JPEG图像使用reduce()或draft()将图像缩小整数倍。
                第二，使用常规重采样调整大小。
                最后一步是改变大小，不低于 reducing_gap 倍。
                reducing_gap可以是无（不执行第一步），或者应该大于1.0。reducing_gap越大，结果越接近于公平重采样。
                reducing_gap越小，调整大小就越快。
                reducing_gap大于或等于3.0时，在大多数情况下，其结果与公平重采样没有区别。
                默认值是2.0（非常接近公平重采样，但在许多情况下仍然更快）。

RETURNS:
    None

"""