"""
ImageFont模块定义了一个同名的类。
这个类的实例存储位图字体，
并与PIL.ImageDraw.ImageDraw.text()方法一起使用。

PIL使用它自己的字体文件格式来存储位图字体，
限制在256个字符。
你可以使用 pillow-scripts 中的 pilfont.py 将 BDF 和 PCF 字体描述符（X 窗口字体格式）转换成这种格式。

从1.1.4版本开始，
PIL可以被配置为支持TrueType和OpenType字体（以及FreeType库支持的其他字体格式）。
对于早期的版本，
TrueType支持只作为imToolkit软件包的一部分。

"""