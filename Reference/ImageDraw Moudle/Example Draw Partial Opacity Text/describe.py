from PIL import Image, ImageDraw, ImageFont
with Image.open("../../../female2.png").convert("RGBA") as base:
    base.show()
    txt = Image.new("RGBA", base.size, (255, 255, 255, 0))
    txt.show()
    fnt = ImageFont.truetype("Pillow/fonts/FreeMono.ttf", 40)
    d = ImageDraw.Draw(txt)
    d.text((10,10),"Hello",font=fnt,fill=(255,255,255,128))
    d.text((10,60),"workd",font=fnt,fill=(255,255,255,255))
    out = Image.alpha_composite(base,txt)
    out.show()
