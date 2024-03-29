"""
Python Imaging Library 包含对图像序列（也称为动画格式）的一些基本支持。
支持的序列格式包括FLI/FLC、GIF和一些实验性格式。
TIFF 文件也可以包含一个以上的帧。

当你打开一个序列文件时，PIL自动加载序列中的第一帧。
你可以使用tell和seek方法在不同的帧之间移动:


"""