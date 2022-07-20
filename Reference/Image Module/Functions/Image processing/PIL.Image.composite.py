"""
PIL.Image.composite(image1, image2, mask)
通过使用透明度掩码混合图像来创建合成图像。

PARAMETERS:
    image1 - 第一幅图像。

    image2 - 第二幅图像。
            必须与第一个图像有相同的模式和大小。

    mask - 一个遮罩图像。
        这个图像可以有 "1"、"L "或 "RGBA "模式，
        并且必须有与其他两个图像相同的大小。
"""