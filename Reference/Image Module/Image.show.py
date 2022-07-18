"""
Image.show(title=None)
    显示此图像。
    这个方法主要是为了调试的目的。

    该方法内部调用PIL.ImageShow.show()。
    你可以使用PIL.ImageShow.register()来覆盖其默认行为。

    图像首先被保存到一个临时文件。
    默认情况下，它将是PNG格式的。

    在Unix上，图像随后被使用display、eog或xv工具打开，这取决于可以找到哪个工具。

    在macOS上，图像是用本地预览程序打开的。

    在Windows上，图像是用标准的PNG显示工具打开的。

    PARAMETERS:
        title - 在可能的情况下，为图像窗口使用的可选标题。



"""