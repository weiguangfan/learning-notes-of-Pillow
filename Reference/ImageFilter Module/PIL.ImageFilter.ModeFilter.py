"""
class PIL.ImageFilter.ModeFilter(size=3)
创建一个模式过滤器。
在一个给定尺寸的盒子里挑选最频繁的像素值。
只出现一次或两次的像素值被忽略。
如果没有像素值出现两次以上，则保留原始像素值。

PARAMETERS:
    size - 核心的大小，以像素为单位。
"""