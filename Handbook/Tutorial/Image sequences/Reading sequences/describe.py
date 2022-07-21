from PIL import Image
with Image.open("../../../../female.jpg") as im:
    im.show()
    im.seek(1)
    try:
        while 1:
            im.seek(im.tell() + 1)
    except EOFError:
        pass



