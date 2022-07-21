from PIL import ImageFilter, Image
with Image.open("../../../../female.jpg") as im:
    im.show()
    out = im.filter(ImageFilter.DETAIL)
    out.show()