"""
创建一个可用于在给定图像中绘图的对象。

注意，图像将被就地修改。

PARAMETERS:
    im - 要绘制的图像。

    mode - 用于颜色值的可选模式。
        对于RGB图像，这个参数可以是RGB或RGBA（将绘图融入图像）。
        对于所有其他模式，这个参数必须与图像模式相同。
        如果省略，模式默认为图像的模式。

"""