from PIL import ImageFont, ImageDraw, Image
with Image.open("../../../female.jpg") as im:
    im.show()
    draw = ImageDraw.Draw(im)
    font = ImageFont.load("arial.pil")# 字符串待定
    draw.text((10,10), "hello", font=font)
    draw.show()
    font = ImageFont.truetype("arial.ttf", 15)
    draw.text((10,25), "world", font=font)
    draw.show()