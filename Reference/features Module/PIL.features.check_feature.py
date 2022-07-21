"""
PIL.features.check_feature(feature)
检查某项功能是否可用。

PARAMETERS:
    feature - 要检查的特征。

RETURNS:
    如果可用则为真，如果不可用则为假，如果未知则为无。

RAISES:
    ValueError - 如果该特征在Pillow的这个版本中没有定义。
"""