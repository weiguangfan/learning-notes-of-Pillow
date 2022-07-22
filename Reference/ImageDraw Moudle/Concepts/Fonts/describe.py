"""
PIL可以使用位图字体或OpenType/TrueType字体。

位图字体是以PIL自己的格式存储的，
个字体通常由两个文件组成，
一个名为.pil，
另一个通常名为.pbm。
前者包含字体度量，
后者包含光栅数据。

要加载一个位图字体，
请使用ImageFont模块中的加载函数。

要加载一个OpenType/TrueType字体，
请使用ImageFont模块中的truetype函数。
请注意，
这个函数依赖于第三方库，
可能不是在所有的PIL构建中都可用。
"""