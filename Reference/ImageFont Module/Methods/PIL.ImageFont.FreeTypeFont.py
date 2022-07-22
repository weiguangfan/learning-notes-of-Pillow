"""
class PIL.ImageFont.FreeTypeFont(
                                font=None,
                                size=10,
                                index=0,
                                encoding='',
                                layout_engine=None)
FreeType字体包装器（需要_imagingft服务）。

font_variant(
            font=None,
            size=None,
            index=None,
            encoding=None,
            layout_engine=None)
    创建这个FreeTypeFont对象的一个副本，
    使用任何指定的参数来覆盖设置。

    参数与用于初始化此对象的参数相同。

    RETURNS:
        一个 FreeTypeFont 对象。

get_variation_axes()
    RETURNS:
        一个变化字体的轴的列表。

    RAISES:
        OSError - 如果该字体不是变化字体。

get_variation_names()
    RETURNS:
        一个以变化字体命名的样式列表。

    RAISES:
        OSError - 如果该字体不是一种变化字体。

getbbox(
        text,
        mode='',
        direction=None,
        features=None,
        language=None,
        stroke_width=0,
        anchor=None)
    当用提供的方向、特征和语言的字体渲染时，
    返回给定文本相对于给定锚点的边界盒（像素）。

    使用getlength()可以获得以下文本的偏移量，
    精度为1/64像素。
    界限框包括一些字体的额外边距，
    例如斜体或重音。

    8.0.0版本中的新内容。

    PARAMETERS:
        text - 要渲染的文本。

        mode - 某些图形驱动使用的模式，
            表示该驱动喜欢的模式。
             如果是空的，渲染器可以返回任一模式。
            请注意，模式总是一个字符串，以简化C级实现。

        direction - 文本的方向。
            可以是'rtl'（从右到左），
            'ltr'（从左到右）
            或'ttb'（从上到下）。
            需要libraqm。

        features - 在文本布局中使用的OpenType字体特征列表。
            这通常用于打开默认不启用的可选字体特征，
            例如'dlig'或'ss01'，
            但也可以用于关闭默认的字体特征，
            例如'-liga'禁用连接符，
            或'-kern'禁用字符间距。
            要获得所有支持的特征，
            请参见https://docs.microsoft.com/en-us/typography/opentype/spec/featurelist Requires libraqm。

        language - 文本的语言。
            不同的语言可能使用不同的字形或连词。
            这个参数告诉字体文本使用的是哪种语言，
            并酌情应用正确的替换方法（如果有的话）。
            它应该是一个BCP47语言代码 需要libraqm。

        stroke_width - 文字笔画的宽度。

        anchor - 文字的锚点排列。
                确定锚点与文本的相对位置。
                默认的对齐方式是左上角。
                有效值见文本锚点。

    RETURNS:
        (左、上、右、下)边界盒

getlength(
            text,
            mode='',
            direction=None,
            features=None,
            language=None)
    当用提供的方向、特征和语言的字体渲染时，
    返回给定文本的长度（像素，精度为1/64）。

    这是后面的文字应该被偏移的数量。
    在某些字体中，
    文字的边框可能会超过这个长度，
    例如，
    当使用斜体或重音符号时。

    结果以浮点数返回；
    如果使用基本布局，
    则为整数。

    请注意，
    由于齿形的原因，
    两个长度的总和可能不等于一个串联的字符串的长度。
    如果你需要调整字距，
    包括以下字符并减去其长度。
    PARAMETERS:
        text - 要测量的文本。

        mode - 某些图形驱动使用的模式，表示驱动更喜欢的模式。
            如果是空的，渲染器可以返回任一模式。
            请注意，模式总是一个字符串，以简化C级实现。

        direction - 文本的方向。
                    可以是'rtl'（从右到左），'ltr'（从左到右）或'ttb'（从上到下）。
                    需要libraqm。

        features - 在文本布局中使用的OpenType字体特征列表。
                这通常用于打开默认不启用的可选字体特征，
                例如'dlig'或'ss01'，
                但也可以用于关闭默认的字体特征，
                例如'-liga'禁用连接符，或'-kern'禁用字符间距。
                要获得所有支持的功能，
                请参见https://docs.microsoft.com/en-us/typography/opentype/spec/featurelist Requires libraqm。

        language -

                文本的语言。
                不同的语言可能使用不同的字形或连词。
                这个参数告诉字体该文本使用的是哪种语言，
                并酌情应用正确的替换，如果有的话。
                它应该是一个BCP 47语言代码 需要libraqm。

    RETURNS:
        水平文本的宽度，垂直文本的高度。

getmask(text,
        mode='',
        direction=None,
        features=None,
        language=None,
        stroke_width=0,
        anchor=None,
        ink=0)
    为文本创建一个位图。

    如果字体使用抗锯齿，
    该位图应该有L模式，
    并使用255的最大值。
    如果字体有内嵌的颜色数据，
    该位图应该有RGBA模式。
    否则，它应该有模式1。

    PARAMETERS:
        text - 要渲染的文本。

        mode - 渲染的文本。
            被一些图形驱动使用，
            用于指示驱动喜欢的模式。
            如果为空，
            渲染器可以返回任一模式。
            请注意，
            模式总是一个字符串，以简化C级实现。

            在1.1.5版本中新增。

        direction -
            文本的方向。
            可以是'rtl'（从右到左），'ltr'（从左到右）或'ttb'（从上到下）。
            需要libraqm。

            在4.2.0版本中新增。

        features –
                在文本布局中使用的OpenType字体特征的列表。
                这通常用于打开默认不启用的可选字体特征，
                例如'dlig'或'ss01'，
                但也可以用于关闭默认的字体特征，
                例如'-liga'禁用连接符，或'-kern'禁用字符间距。
                要获得所有支持的功能，
                请参见https://docs.microsoft.com/en-us/typography/opentype/spec/featurelist Requires libraqm。

                在4.2.0版本中新增。

        language -
                文本的语言。
                不同的语言可能使用不同的字形或连接词。
                这个参数告诉字体该文本使用的是哪种语言，
                并酌情应用正确的替换方法（如果有的话）。
                它应该是一个BCP 47语言代码 需要libraqm。

                在6.0.0版本中新增。

        stroke_width - 描边宽度
                    文字笔画的宽度。
                    在6.2.0版本中新增。

        anchor - 锚点
                文本锚的对齐方式。
                确定锚点与文本的相对位置。
                默认的对齐方式是左上角。
                参见文本锚的有效值。
                在8.0.0版本中新增。

        ink –
            用于在RGBA模式下渲染的前景墨水。
            在8.0.0版本中新增。

    RETURNS:
        一个由PIL.Image.core接口模块定义的PIL内部存储内存实例。

getmask2(
        text,
        mode='',
        fill=<object object>,
        direction=None,
        features=None,
        language=None,
        stroke_width=0,
        anchor=None,
        ink=0,
        *args,
        **kwargs)
    为文本创建一个位图。

    如果字体使用抗锯齿，
    该位图应该有L模式，
    并使用255的最大值。
    如果字体有内嵌的颜色数据，
    该位图应该有RGBA模式。
    否则，
    它应该有模式1。

    PARAMETERS:
        text - 要渲染的文本。

        mode - 渲染的文本。
                被一些图形驱动使用，
                用于指示驱动喜欢的模式。
                如果为空，
                渲染器可以返回任一模式。
                请注意，
                模式总是一个字符串，
                以简化C级实现。

                在1.1.5版本中新增。

        fill -
            可选的填充函数。
            默认情况下，
            将使用一个内部的Pillow函数。

            已废弃。
            这个参数将在Pillow 10 (2023-07-01)中删除。

        direction -
            文本的方向。
            可以是'rtl'（从右到左），'ltr'（从左到右）或'ttb'（从上到下）。
            需要libraqm。
            在4.2.0版本中新增。

        features –
                在文本布局中使用的OpenType字体特征的列表。
                这通常用于打开默认不启用的可选字体特征，
                例如'dlig'或'ss01'，
                但也可以用于关闭默认的字体特征，
                例如'-liga'禁用连接符，或'-kern'禁用字符间距。
                要获得所有支持的功能，
                请参见https://docs.microsoft.com/en-us/typography/opentype/spec/featurelist Requires libraqm。

                在4.2.0版本中新增。

        language -
                文本的语言。
                不同的语言可能使用不同的字形或连接词。
                这个参数告诉字体该文本使用的是哪种语言，
                并酌情应用正确的替换方法（如果有的话）。
                它应该是一个BCP 47语言代码 需要libraqm。

                在6.0.0版本中新增。

        stroke_width - 描边宽度
                    文字笔画的宽度。
                    在6.2.0版本中新增。

        anchor - 锚点
                文本锚的对齐方式。
                确定锚点与文本的相对位置。
                默认的对齐方式是左上角。
                请参阅文本锚的有效值。

                在8.0.0版本中新增。

        ink –
            用于在RGBA模式下渲染的前景墨水。
            在8.0.0版本中新增。

    RETURNS:
        一个由PIL.Image.core接口模块定义的内部PIL存储内存实例的元组，
        以及文本偏移量，
        即起始坐标和第一个标记之间的差距。

getmetrics()
    RETURNS:
    字体上升（从基线到最高轮廓点的距离）和下降（从基线到最低轮廓点的距离，一个负值）的元组。

getname()
    RETURNS:
        字体家族（如Helvetica）和字体样式（如Bold）的一个元组。

getoffset(text)
    从9.2.0版本开始被废弃。

    使用getbbox()代替。

    返回给定文本的偏移量。
    这是起始坐标和第一个标记之间的差距。
    注意，这个间隙包含在getsize()的结果中。

    PARAMETERS:
        text - 要测量的文本。

    RETURNS:
        一个x和y偏移量的元组

getsize(
        text,
        direction=None,
        features=None,
        language=None,
        stroke_width=0)
    从9.2.0版本开始被废弃。

    使用getlength()来测量以下文本的偏移量，精度为1/64像素。
    使用getbbox()来获取基于锚点的精确边界框。

    如果用提供的方向、特征和语言的字体渲染，返回给定文本的宽度和高度（像素）。

    由于历史原因，这个函数从升序线而不是从顶部测量文本高度，见文本锚。
    如果你想从顶部测量文本的高度，建议使用getbbox()的底部值和anchor='lt'来代替。
    PARAMETERS:
        text - 要测量的文本。

        direction –
                文本的方向。
                可以是'rtl'（从右到左），'ltr'（从左到右）或'ttb'（从上到下）。
                需要libraqm。

                在4.2.0版本中新增。

        features –
                在文本布局中使用的OpenType字体特征的列表。
                这通常用于打开默认不启用的可选字体特征，
                例如'dlig'或'ss01'，
                但也可以用于关闭默认的字体特征，
                例如'-liga'禁用连接符，或'-kern'禁用字符间距。
                要获得所有支持的功能，
                请参见https://docs.microsoft.com/en-us/typography/opentype/spec/featurelist Requires libraqm。

                在4.2.0版本中新增。

        language -
                文本的语言。
                不同的语言可能使用不同的字形或连接词。
                这个参数告诉字体该文本使用的是哪种语言，
                并酌情应用正确的替换方法（如果有的话）。
                它应该是一个BCP 47语言代码 需要libraqm。

                在6.0.0版本中新增。

        stroke_width - 描边宽度
                    文字笔画的宽度。

                    在6.2.0版本中新增。

    RETURNS:
        (width, height)

getsize_multiline(
                    text,
                    direction=None,
                    spacing=4,
                    features=None,
                    language=None,
                    stroke_width=0)
    自9.2.0版起被废弃。

    请使用ImageDraw.multiline_textbbox()代替。

    返回给定文本的宽度和高度（以像素为单位），
    如果用提供的方向、特征和语言的字体渲染，同时尊重换行字符。

    PARAMETERS:
        text - 要测量的文本。

        direction - 文字的方向。
                    可以是'rtl'（从右到左）、'ltr'（从左到右）或'ttb'（从上到下）。
                    需要libraqm。

        spacing - 行与行之间的垂直间隔，
                默认为4像素。

        features - 在文本布局中使用的OpenType字体特征列表。
                这通常用于打开默认情况下未启用的可选字体特征，
                例如'dlig'或'ss01'，
                但也可以用于关闭默认的字体特征，
                例如'-liga'禁用连接符，或'-kern'禁用字符间距。
                要获得所有支持的功能，
                请参见https://docs.microsoft.com/en-us/typography/opentype/spec/featurelist Requires libraqm。

        language -
                文本的语言。
                不同的语言可能使用不同的字形或连词。
                这个参数告诉字体该文本使用的是哪种语言，
                并酌情应用正确的替换，如果有的话。
                它应该是一个BCP 47语言代码 需要libraqm。

                在6.0.0版本中新增。

        stroke_width - 描边宽度

                    文字笔画的宽度。

                    在6.2.0版本中新增。

    RETURNS:
        (width, height)

set_variation_by_axes(axes)
    PARAMETERS:
        axes - 每个轴的值的列表。

    RAISES:
        OSError - 如果字体不是变化字体。

set_variation_by_name(name)
    PARAMETERS:
        name - 样式的名称。

    RAISES:
        OSError - 如果该字体不是变化字体。

"""