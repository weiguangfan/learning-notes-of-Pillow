"""
Pillow读取JPEG、JFIF和Adobe JPEG文件，其中包含L、RGB或CMYK数据。
它可以写入标准和渐进的JFIF文件。

使用draft()方法，
你可以通过将RGB图像转换为L来加快速度，
并在加载图像时将其大小调整为原始大小的1/2、1/4或1/8。

默认情况下，
Pillow不允许加载截断的JPEG文件，
设置ImageFile.LOAD_TRUNCATED_IMAGES来覆盖这一点。

open()方法可以设置以下信息属性（如果有）:
    jfif
        发现JFIF应用标记。如果该文件不是JFIF文件，则不存在此键。

    jfif_version
        一个代表jfif版本的元组，（主要版本，次要版本）。

    jfif_density
        一个元组，代表图像的像素密度，单位为jfif_unit。

    jfif_unit
        jfif_density的单位。
            0 - 没有单位
            1 - 每英寸的像素
            2 - 每厘米的像素

    dpi
        一个元组，代表报告的像素密度，单位是每英寸像素，如果文件是jfif文件，单位是英寸。

    adobe
        找到的Adobe应用程序标记。如果该文件不是 Adobe JPEG 文件，则此键不存在。

    adobe_transform
        供应商专用标记。

    progression
        表示这是一个渐进式的JPEG文件。

    icc_profile
        该图像的ICC颜色配置文件。

    exif
        图片的原始EXIF数据。

    comment
        关于图像的评论。
        7.1.0版的新内容。

save()方法支持以下选项:

    quality
        图像质量，从0（最差）到95（最佳），或者字符串keep。
        默认值是75。
        应避免使用高于95的值；
        100会禁用部分JPEG压缩算法，
        并导致大文件，
        而图像质量几乎没有任何提高。
        keep这个值只对JPEG文件有效，
        它将保留原始图像质量水平、子采样和qtables。

    optimize
        如果存在并且为真，
        表示编码器应该对图像进行额外的处理，
        以便选择最佳的编码器设置。

    progressive
        如果存在且为真，
        表示该图像应被存储为渐进式JPEG文件。

    dpi
        一个代表像素密度的整数组，(x,y)。

    icc_profile
        如果存在并为真，
        该图像将以提供的ICC配置文件存储。
        如果没有提供这个参数，
        图像在保存时将不附带配置文件。
        要保留现有的配置文件。
        im.save(filename, 'jpeg', icc_profile=im.info.get('icc_profile')

    exif
        如果存在，图像将与提供的原始EXIF数据一起存储。

    subsampling
        如果存在，为编码器设置子采样。
            keep: 仅对JPEG文件有效，将保留原始图像设置。
            4：4：4，4：2：2，4：2：0：具体的采样值
            0: 相当于4:4:4
            1: 相当于4:2:2
            2: 相当于4:2:0
        如果没有，设置将由libjpeg或libjpeg-turbo决定。

    qtables
        如果存在，
        设置编码器的qtables。
        这在JPEG文档中被列为向导的高级选项。
        谨慎使用。
        qtables可以是几种类型的值之一。
            一个字符串，命名一个预设，例如：keep、web_low 或 web_high
            一个64个整数的列表、元组或字典（整数key=range(len(key))）。必须有2到4个表。
        在2.5.0版本中新增。

Note
    要启用 JPEG 支持，
    你需要在构建 Python Imaging Library之前构建并安装 IJG JPEG 库。
    详情见发行版README。
"""