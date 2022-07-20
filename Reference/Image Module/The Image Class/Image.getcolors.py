"""
Image.getcolors(maxcolors=256)

返回该图像中使用的颜色列表。

这些颜色将以图像的模式出现。
例如，RGB图像将返回一个（红、绿、蓝）颜色值的元组，而P图像将返回调色板中的颜色索引。

PARAMETERS:
    maxcolors - 颜色的最大数量。
                如果超过了这个数字，这个方法就会返回None。
                默认限制是256种颜色。

RETURNS:
    一个未经排序的（count, pixel）值的列表。


"""