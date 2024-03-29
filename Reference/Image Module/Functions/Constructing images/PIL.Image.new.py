"""
PIL.Image.new(mode, size, color=0)
以给定的模式和尺寸创建一个新图像。

PARAMETERS:
    mode - 新图像要使用的模式。
        参见 Modes.

    size - 一个2元组，包含（宽度，高度）的像素。

    color - 图像要使用什么颜色。
            默认是黑色。
            如果给定，对于单波段模式，这应该是一个单一的整数或浮点值，
            对于多波段模式，应该是一个元组（每个波段一个值）。
            当创建RGB图像时，你也可以使用ImageColor模块所支持的颜色字符串。
            如果颜色是None，图像就不会被初始化。

RETURNS:
    一个图像对象。

"""