import os,sys
from PIL import Image
size = (128,128)
for infile in sys.argv[1:]:
    outfile = os.path.splitext(infile)[0] + ".thumbnail"
    if infile != outfile:
        try:
            with Image.open(infile) as im:
                im.thumbnail(size)
                im.save(outfile,"JPEG")
        except OSError:
            print("cannot create thumbnail for", infile)
"""
需要注意的是，
除非真的需要，
否则库不会对光栅数据进行解码或加载。
当你打开一个文件时，
文件头会被读取以确定文件格式，
并提取诸如模式、大小和其他解码文件所需的属性，
但文件的其他部分直到后来才被处理。

这意味着打开图像文件是一个快速操作，
它与文件大小和压缩类型无关。
这里有一个简单的脚本来快速识别一组图像文件:
"""

