"""
Image.histogram(mask=None, extrema=None)
返回图像的直方图。
直方图以像素计数列表的形式返回，
源图像中每个像素值都有一个。
计数被分组为每个波段的256个bin，
即使图像每个波段有超过8比特。
如果图像有一个以上的波段，
所有波段的直方图将被串联起来（例如，"RGB "图像的直方图包含768个值）。

双层图像（模式 "1"）被此方法视为灰度（"L"）图像。

如果提供了一个遮罩，
该方法将返回图像中遮罩图像为非零的部分的直方图。
遮罩图像的大小必须与图像相同，
并且是一个双级图像（模式 "1"）或灰度图像（"L"）。

PARAMETERS:
    mask - 一个可选的掩码。

    extrema - 一个可选的手动指定的extrema的元组。


RETURNS:
    一个包含像素计数的列表。




"""