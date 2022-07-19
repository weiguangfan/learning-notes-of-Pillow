"""
Image.save(fp, format=None, **params)
以给定的文件名保存此图像。
如果没有指定格式，
如果可能的话，要使用的格式是由文件名的扩展名决定的。

关键字选项可以用来向写入器提供额外的指示。
如果写入器不识别一个选项，它将被默默地忽略。
可用的选项在每个写入器的图像格式文档中都有描述。

你可以使用一个文件对象而不是文件名。
在这种情况下，你必须始终指定格式。
文件对象必须实现寻找、告诉和写入方法，并以二进制模式打开。

PARAMETERS:
    fp - 文件名（字符串）、pathlib.Path 对象或文件对象。

    format - 可选的格式重写。
        如果省略，要使用的格式由文件名的扩展名决定。
        如果使用的是文件对象而不是文件名，应该总是使用这个参数。

    params - 图像写入器的额外参数。

RETURNS:
    无

RAISES:
    ValueError - 如果不能从文件名确定输出格式。
                使用 format 选项来解决这个问题。

    OSError - 如果文件不能被写入。
                该文件可能已经被创建，并且可能包含部分数据。

"""


