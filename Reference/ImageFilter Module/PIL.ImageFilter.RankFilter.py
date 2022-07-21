"""
class PIL.ImageFilter.RankFilter(size, rank)
创建一个等级过滤器。
排名过滤器对一个给定大小的窗口中的所有像素进行排序，
并返回排名的值。

PARAMETERS:
    size - 核心的大小，
            以像素为单位。

    rank - 要挑选的像素值。
            用0表示最小值过滤器，
            用size*size/2表示中值过滤器，
            用size*size-1表示最大值过滤器，等等。

"""