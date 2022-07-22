"""
PIL.ImageFont.truetype(
                        font=None,
                        size=10,
                        index=0,
                        encoding='',
                        layout_engine=None)
从一个文件或类文件对象中加载一个TrueType或OpenType字体，
并创建一个字体对象。
这个函数从给定的文件或类文件对象中加载一个字体对象，
并为给定尺寸的字体创建一个字体对象。

Pillow使用FreeType来打开字体文件。
如果你在Windows上同时打开许多字体，
要注意Windows将C语言中可以同时打开的文件数量限制在512个。
如果你接近这个限制，
可能会抛出一个OSError，
报告FreeType "无法打开资源"。

这个函数需要_imagingft服务。

PARAMETERS:
    font - 一个文件名或包含TrueType字体的类文件对象。
        如果在这个文件名中没有找到该文件，
        加载器也可以在其他目录中搜索，
        例如Windows中的fonts/目录
        或macOS中的/Library/Fonts/, /System/Library/Fonts/ 和 ~/Library/Fonts/。

    size - 要求的尺寸，单位是像素。

    index - 要加载的字体面（默认是第一个可用的面）。

    encoding -

            要使用的字体编码（默认为Unicode）。
            可能的编码包括（更多信息见FreeType文档）:

                "unic" (Unicode)

                "symb" (Microsoft Symbol)

                "ADOB" (Adobe Standard)

                "ADBE" (Adobe Expert)

                "ADBC" (Adobe自定义)

                "armn" (Apple Roman)

                "sjis" (Shift JIS)

                "gb" (中华人民共和国)

                "big5"

                "wans" (扩展的Wansung)

                "joha" (Johab)

                "lat1" (Latin-1)

            这指定了要使用的字符集。
            它不会改变后续操作中提供的任何文本的编码。

    layout_engine -

                如果有的话，
                要使用哪一个布局引擎:
                ImageFont.Layout.BASIC或ImageFont.Layout.RAQM。

                你可以使用PIL.features.check_feature()与feature="raqm "检查对Raqm布局的支持。

                4.2.0版本中的新内容。

RETURNS:
    一个字体对象。

RAISES:
    OSError - 如果文件不能被读取。

"""