"""
Image.getchannel(channel)
返回一个包含源图像单通道的图像。

PARAMETERS:
    channel - 要返回的通道。
            可以是索引（0代表 "RGB "的 "R "通道）
            或通道名称（"A "代表 "RGBA "的alpha通道）。

RETURNS:
    一个 "L "模式的图像。

在4.3.0版本中新增。

"""