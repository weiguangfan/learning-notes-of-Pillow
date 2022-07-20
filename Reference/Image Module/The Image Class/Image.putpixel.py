"""
Image.putpixel(xy, value)
修改给定位置上的像素。
对于单波段图像，颜色是以单一数值给出的，对于多波段图像，则是一个元组。
除此以外，P图像还接受RGB和RGBA图元。

请注意，这种方法相对较慢。
对于更广泛的变化，请使用paste()或ImageDraw模块代替。

见:
paste()
putdata()
ImageDraw

PARAMETERS:
    xy - 像素坐标，以（x，y）的形式给出。
        参见Coordinate System.

    value - 像素的值。



"""