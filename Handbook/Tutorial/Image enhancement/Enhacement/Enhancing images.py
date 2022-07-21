from PIL import Image, ImageEnhance
with Image.open("../../../../female.jpg") as im:
    im.show()
    enh = ImageEnhance.Contrast(im)
    enh.enhance(1.3).show("30% more contrast")
