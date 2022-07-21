"""
Pillow可以读取GIF87a和GIF89a版本的GIF文件格式。
该库默认以GIF87a写文件，
除非使用了GIF89a功能或已经在使用GIF89a。
文件是用LZW编码写的。

GIF文件最初是作为灰度（L）或调色板模式（P）图像被读取的。
在P模式的图像中寻求以后的帧，
将把图像改为RGB（或RGBA，如果第一帧有透明度）。

P模式图像被改变为RGB，
因为GIF的每一帧都可能包含它自己的独立调色板，
最多256种颜色。
当一个新的帧被放在前一个帧上时，
这些颜色的组合可能会超过P模式256种颜色的限制。
相反，图像被转换为RGB处理。

open()方法设置以下信息属性：
    background
        默认的背景颜色（一个调色板颜色索引）。

    transparency
        透明度的颜色索引。
        如果图像不透明，这个键就省略。

    version
        版本（GIF87a或GIF89a）。

    duration
        可能不存在。
        显示GIF当前帧的时间，以毫秒计。

    loop
        可能不存在。
        GIF应该循环的次数。
        0意味着它将永远循环。

    comment
        可能不存在。
        关于图像的评论。
        这是在当前帧的图像之前发现的最后一个注释。

    extension
        可能不存在。
        包含应用程序的具体信息。







"""
# 如果你希望第一个P图像帧也是RGB，
# 这样每个P帧都被转换为RGB或RGBA模式，
# 有一个设置可用。
from PIL import GifImagePlugin
# GifImagePlugin.LOADING_STRATEGY = GifImagePlugin.LoadingStrategy.RGB_ALWAYS

# 然而，GIF框架并不总是包含单独的调色板。
# 如果只有一个全局调色板，那么所有的颜色都可以适合P模式。
# 如果你希望在这种情况下，帧保持为P模式，也有一个设置可用:

# GifImagePlugin.LOADING_ATRATEGY = GifImagePlugin.LoadingStrategy.RGB_AFTER_DIFFERENT_PALETTE_ONLY


# 恢复默认行为，即P模式图像只在第一帧后转换为RGB或RGBA:
# GifImagePlugin.LOADING_STRATEGY = GifImagePlugin.LoadingStrategy.RGB_AFTER_FIRST


