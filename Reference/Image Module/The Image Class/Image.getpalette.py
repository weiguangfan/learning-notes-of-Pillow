"""
Image.getpalette(rawmode='RGB')
以列表形式返回图像调色板。

PARAMETERS:
    rawmode -
            返回调色板的模式。
            None将以当前模式返回调色板。

            在9.1.0版本中新增。

RETURNS:
    一个颜色值的列表[r, g, b, ...]，如果图像没有调色板，则为 None。

"""