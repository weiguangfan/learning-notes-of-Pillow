"""
ImageColor模块包含颜色表和从CSS3风格的颜色指定器到RGB图元的转换器。
这个模块被PIL.Image.new()和ImageDraw模块以及其他模块所使用。

Color Names
ImageColor模块支持以下字符串格式:
    十六进制的颜色说明，
        以#rgb、#rgba、#rrggbb或#rrggbbaa的形式给出，
        其中r是红色，
        g是绿色，
        b是蓝色，
        a是alpha（也称为 "不透明度"）。
        例如，
        #ff0000表示纯红色，
        #ff0000cc表示有80%不透明度的红色（cc在十进制中是204，204/255=0.8）。

    RGB函数，
        以rgb(红、绿、蓝)的形式给出，
        其中颜色值是0到255范围内的整数。
        或者，
        颜色值也可以用三个百分比（0%到100%）来表示。
        例如，
        rgb(255,0,0)和rgb(100%,0%,0%)都表示纯红色。

    色相-饱和度-亮度（HSL）函数，
        以hsl(hue, saturation%, lightness%)的形式给出，
        其中色相是以0到360之间的角度给出的颜色（红=0，绿=120，蓝=240），
        饱和度是0%到100%之间的值（灰=0%，全色=100%），
        亮度是0%到100%之间的值（黑=0%，正常=50%，白=100%）。
        例如，hsl(0,100%,50%)是纯红色。

    色相-饱和度-值（HSV）函数，
        以hsv(hue, saturation%, value%)给出，
        其中色相和饱和度与HSL相同，
        value值在0%和100%之间（黑=0%，正常=100%）。
        例如，hsv(0,100%,100%)是纯红色。
        这种格式也被称为色相-饱和度-亮度（HSB），
        可以给出hsb(hue, saturation%, brightness%)，
        其中每个值都是按照HSV中的方式使用。

    常见的HTML颜色名称。
        ImageColor模块提供了大约140个标准的颜色名称，
        是基于X Window系统和大多数网络浏览器所支持的颜色。
        例如，
        red和Red都表示纯红色。

"""