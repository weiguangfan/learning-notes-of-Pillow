"""
ImageEnhance模块包含一些可用于图像增强的类。
"""
# 例子:改变图像的清晰度
from PIL import Image, ImageEnhance
with Image.open("../../female.jpg") as im:
    im.show()
    # enhancer = ImageEnhance.Sharpness(im)
    # enhancer = ImageEnhance.Contrast(im)
    # enhancer = ImageEnhance.Color(im)
    enhancer = ImageEnhance.Brightness(im)
    for i in range(8):
        factor = i / 4.0
        enhancer.enhance(factor).show(f"sharpness {factor:f}" )

# 也请看Scripts/目录下的enhancer.py演示程序。
