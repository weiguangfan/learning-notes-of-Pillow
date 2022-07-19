"""
Image.info: dict
一个保存与图像相关的数据的字典。
这个字典被文件处理程序用来传递从文件中读取的各种非图像信息。
详情见各种文件处理程序的文档。

大多数方法在返回新图像时忽略了 dictionary；
由于键没有被标准化，方法不可能知道操作是否影响 dictionary。
如果你以后需要这些信息，
请保留对从 open 方法返回的 info dictionary 的引用。

除非在其他地方指出，这个字典不影响保存文件。

"""