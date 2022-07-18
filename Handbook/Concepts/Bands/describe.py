"""
一幅图像可以由一个或多个波段的数据组成。
Python Imaging Library允许你在一张图像中存储多个波段，
前提是它们都有相同的尺寸和深度。
例如，一个PNG图像可能有 "R"、"G"、"B "和 "A "带，
分别代表红色、绿色、蓝色和α透明度值。
许多操作分别作用于每个波段，例如直方图。
把每个像素看成是每个波段有一个值，通常是很有用的。

要获得图像中频段的数量和名称，可以使用getbands()方法。
"""