from PIL import ImageSequence, Image
with Image.open("../../../../female.jpg") as im:
    im.show()
    for frame in ImageSequence.Iterator(im):
        pass



