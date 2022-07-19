from PIL import Image
box = (100, 100, 400, 400)
with Image.open("../../../female.jpg") as im:
    im.show()
    region = im.crop(box)
    region = region.transpose(Image.TRANSPOSE.ROTATE_180)
    im.paste(region, box)
    im.show()