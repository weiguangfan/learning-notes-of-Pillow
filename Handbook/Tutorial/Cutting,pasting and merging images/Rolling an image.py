from PIL import Image

def roll(im,delta):
    """roll an image sideways"""
    xsize, ysize, = im.size
    delta = delta % xsize
    if delta == 0:
        return im
    part1 = im.crop((0,0,delta,ysize))
    part1.show()
    part2 = im.crop((delta,0,xsize,ysize))
    part2.show()
    im.paste(part1,(xsize - delta,0,xsize,ysize))
    im.show()
    im.paste(part2,(0,0,xsize - delta,ysize))
    im.show()
    return im

with Image.open("../../../female.jpg") as im:
    im.show()
    im = roll(im,20)
"""
或者如果你想把两张图片合并成一张更宽的图片。
"""