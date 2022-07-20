"""
Image.rotate(
            angle,
            resample=Resampling.NEAREST,
            expand=0,
            center=None,
            translate=None,
            fillcolor=None)
返回此图像的一个旋转副本。
此方法返回此图像的一个副本，围绕中心逆时针旋转给定的度数。

PARAMETERS:
    angle - 逆时针旋转的度数。

    resample - 一个可选的重采样过滤器。
            这可以是PIL.Image.Resampling.NEAREST（使用最近的邻居）、
            PIL.Image.BILINEAR（2x2环境下的线性插值）
            或PIL.Image.Resampling.BICUBIC（4x4环境下的立方样条曲线插值）中的一个。
            如果省略，
            或者图像的模式为 "1 "或 "P"，
            它将被设置为PIL.Image.Resampling.NEAREST。
            参见Filters.

    expand - 可选的扩展标志。
            如果为真，
            扩展输出图像，
            使其足够大以容纳整个旋转的图像。
            如果为假或省略，则
            使输出图像与输入图像的大小相同。
            请注意，
            扩展标志假定围绕中心旋转，
            没有平移。

    center - 可选的旋转中心（一个2元组）。
            原点是左上角。
            默认是图像的中心。

    translate - 可选的旋转后的平移（一个2元组）。

    fillcolor - 可选的旋转图像外的区域的颜色。

RETURNS:
    一个图像对象。

"""
# 这将使输入的图像逆时针旋转θ度。
from PIL import Image
with Image.open("../../../female.jpg") as im:
    im.show()
    theta = 60
    im_rotated = im.rotate(angle=theta)
    im_rotated.show()