"""
PIL.Image.open(fp, mode='r', formats=None)
打开并识别给定的图像文件。

这是一个懒惰的操作；
这个函数识别了文件，但文件仍然是开放的，实际的图像数据不会从文件中读取，
直到你试图处理数据（或调用load()方法）。
见new()。
见 File Handling in Pillow

PARAMETERS:
    fp - 文件名（字符串）、pathlib.Path对象或一个文件对象。
        文件对象必须实现file.read、file.seek和file.tell方法，
        并且是以二进制模式打开。

    mode - 模式。
        如果给出，这个参数必须是 "r"。

    formats - 尝试加载文件的格式列表或元组。
        这可以用来限制所检查的格式集。
        传递 None 来尝试所有支持的格式。
        你可以通过运行 python3 -m PIL 或使用 PIL.features.pilinfo() 函数来打印可用的格式集。

RETURNS:
    一个图像对象。

RAISES:
    FileNotFoundError - 如果不能找到文件。

    PIL.UnidentifiedImageError - 如果图像不能被打开和识别。

    ValueError - 如果模式不是 "r"，或者如果一个StringIO实例被用于fp。

    TypeError - 如果格式不是None、一个列表或一个元组。


"""