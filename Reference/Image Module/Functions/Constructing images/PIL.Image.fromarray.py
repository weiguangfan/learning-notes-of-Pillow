"""
PIL.Image.fromarray(obj, mode=None)
从一个输出数组接口的对象中创建一个图像存储器（使用缓冲区协议）。

如果obj不是连续的，那么就调用tobytes方法并使用frombuffer()。

PARAMETERS:
obj - 具有数组接口的对象

mode - 读取obj时使用的可选模式。
    如果没有，将由类型决定。

RETURNS:
    一个图像对象。

"""