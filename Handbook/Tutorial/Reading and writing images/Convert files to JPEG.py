
import os,sys
from PIL import Image
for infile in sys.argv[1:]:
    print(infile)
    f, e = os.path.splitext(infile)
    print(f)
    print(e)
    outfile = f + '.jpg'
    print(outfile)
    if infile != outfile:
        try:
            with Image.open(infile) as im:
                im.save(outfile)
        except OSError:
            print('cannot convert', infile)

"""
可以向save()方法提供第二个参数，明确指定文件格式。
如果你使用一个非标准的扩展名，你必须总是以这种方式指定格式：
"""
