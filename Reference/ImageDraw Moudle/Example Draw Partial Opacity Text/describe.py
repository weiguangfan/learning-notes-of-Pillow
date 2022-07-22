from PIL import Image, ImageDraw, ImageFont
with Image.open("../../../female2.png").convert("RGBA") as base:
    base.show()
    txt = Image.new("RGBA", base.size, (255, 255, 255, 0))
    txt.show()
    ImageFont.truetype()