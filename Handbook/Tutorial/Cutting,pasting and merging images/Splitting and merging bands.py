from PIL import Image
with Image.open("../../../female.jpg") as im:
    im.show()
    r, g, b = im.split()
    print(r)
    print(g)
    print(b)
    im_mer1 = Image.merge("RGB", (b, g, r))
    im_mer2 = Image.merge("RGB", (g, b, r))
    im_mer1.show()
    im_mer2.show()

"""
注意，
对于单色带图像，
split()返回图像本身。
要处理单个色带，
你可能想先将图像转换为 "RGB"。
"""