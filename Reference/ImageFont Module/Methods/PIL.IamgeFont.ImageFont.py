"""
class PIL.ImageFont.ImageFont
PIL字体包装器

getbbox(text, *args, **kwargs)
    返回给定文本的包围盒（以像素为单位）。
    9.2.0版本中的新功能。

    PARAMETERS:
        text - 要渲染的文本。

        mode - 某些图形驱动使用的模式，
            表示该驱动更喜欢哪种模式。
            如果为空，
            渲染器可以返回任一模式。
            请注意，
            模式总是一个字符串，
            以简化C级实现。

    RETURNS:
    (左、上、右、下)包围盒

getlength(text, *args, **kwargs)
    返回给定文本的长度（单位：像素）。
    这是后续文本应该被偏移的量。

    在9.2.0版本中新增。

getmask(text, mode='', *args, **kwargs)
    为文本创建一个位图。

    如果字体使用抗锯齿，
    该位图应该具有模式L并使用最大值255。
    否则，
    它应该有模式1。

    PARAMETERS:
        text - 要渲染的文本。

        mode -

            被一些图形驱动使用，用于指示驱动所偏好的模式。
            如果为空，渲染器可以返回任一模式。
            请注意，模式总是一个字符串，以简化C级实现。

            在1.1.5版本中新增。

    RETURNS:
        一个由PIL.Image.core接口模块定义的PIL内部存储内存实例。

getsize(text, *args, **kwargs)
    自9.2.0版起被废弃。

    使用getbbox()或getlength()代替。

    返回给定文本的宽度和高度（单位：像素）。

    PARAMETERS:
        text - 要测量的文本。

    RETURNS:
        (width, height)

"""