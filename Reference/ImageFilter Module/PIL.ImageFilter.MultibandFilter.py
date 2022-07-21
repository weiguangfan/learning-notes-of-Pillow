"""
class PIL.ImageFilter.MultibandFilter
一个用于过滤多波段图像的抽象混合器（与filter()一起使用）。

实现者必须提供以下方法：

filter(self, image)
    在多波段图像上应用一个过滤器。

RETURNS:
    一个过滤后的图像副本。
"""