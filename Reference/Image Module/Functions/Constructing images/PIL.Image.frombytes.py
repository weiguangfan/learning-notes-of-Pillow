"""
PIL.Image.frombytes(
                    mode,
                    size,
                    data,
                    decoder_name='raw',
                    *args)
从缓冲区中的像素数据创建一个图像存储器的副本。

在其最简单的形式中，
这个函数需要三个参数（模式、大小和未打包的像素数据）。

你也可以使用PIL支持的任何像素解码器。
关于可用的解码器的更多信息，见 Writing Your Own File Codec.

注意，
这个函数只解码像素数据，
而不是整个图像。
如果你有一个字符串中的整个图像，
请将其包裹在一个BytesIO对象中，并使用open()来加载它。

PARAMETERS:
    mode - 图像模式。
        参见Modes.

    size - 图像的大小。

    data - 包含给定模式的原始数据的字节缓冲区。

    decoder_name - 要使用的解码器。

    args - 给定解码器的附加参数。

RETURNS:
    一个图像对象。

"""