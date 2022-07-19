"""
PIL.ImageShow.register(viewer, order=1)

register()函数用于注册额外的查看器。

PARAMETERS:
    viewer - 要注册的查看器。

    order - 零或一个负整数，将该查看器预置到列表中，一个正整数将其追加。
"""
from PIL import ImageShow
# MyViewer will be used as a last resort
# ImageShow.register(MyViewer())
# MySecondViewer will be prioritised
# ImageShow.register(MySecondViewer(),0)
# XVViewer will be prioritised
# ImageShow.register(ImageShow.XVViewer(),0)
