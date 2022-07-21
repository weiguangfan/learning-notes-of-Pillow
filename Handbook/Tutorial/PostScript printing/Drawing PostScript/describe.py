from PIL import Image,PSDraw
with Image.open("../../../../female.jpg") as im:
    im.show()
    title = "female"
    box = (1 * 72, 2 * 72, 7 * 72, 10 * 72)
    ps = PSDraw.PSDraw()
    ps.begin_document(title)
    ps.image(box, im, 75)
    ps.rectangle(box)
    ps.setfont("HelveticalNarrow-Blod", 36)
    ps.text((3 * 72, 4 * 72), title)
    ps.end_document()