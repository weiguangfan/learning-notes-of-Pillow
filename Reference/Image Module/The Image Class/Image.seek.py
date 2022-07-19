"""
Image.seek(frame)
在这个序列文件中搜索到给定的帧。
如果你的搜索超过了序列的末端，
该方法会引发一个EOFError异常。
当一个序列文件被打开时，
该库会自动搜索到第0帧。

参见tell()。

如果定义了，n_frames是指可用的帧的数量。

PARAMETERS:
    frame - 帧数，从0开始。

RAISES:
    EOFError - 如果调用试图在序列的末端之外寻找。

"""