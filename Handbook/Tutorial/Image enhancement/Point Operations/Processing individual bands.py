from PIL import Image
with Image.open("../../../../female.jpg") as im:
    im.show()
    print(im.mode)
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
    print(source)
    im_meg = Image.merge(im.mode, source)
    im_meg.show()
"""
注意用于创建掩码的语法:
imout = im.point(lambda i: expression and 255)
Python 只对逻辑表达式中确定结果所需的部分进行评估，
并将最后检查的值作为表达式的结果返回。
因此，
如果上面的表达式是false (0)，
Python 就不看第二个操作数，
因此返回 0。
否则，
它返回 255。
"""