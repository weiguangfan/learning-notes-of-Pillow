from PIL import Image
with Image.open("../../../../female.jpg") as im:
    im.show()
    source = im.split()
    print(source)
    R,G,B = 0,1,2
    mask = source[R].point(lambda i: i < 100 and 255)
    print(mask)
    mask.show()
    out = source[G].point(lambda i: i * 0.7)
    print(out)
    out.show()
    source[G].paste(out, None, mask)
    # im_meg = Image.merge(im.mode, source)
    # im_meg.show()
