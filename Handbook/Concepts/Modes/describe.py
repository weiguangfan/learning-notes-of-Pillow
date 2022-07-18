"""
一个图像的模式是一个字符串，它定义了图像中一个像素的类型和深度。每个像素使用比特深度的全部范围。因此，一个1位像素的范围是0-1，一个8位像素的范围是0-255，以此类推。目前的版本支持以下标准模式。

    1（1位像素，黑与白，每字节存储一个像素）。

    L（8位像素，黑色和白色）

    P（8位像素，使用调色板映射到任何其他模式）

    RGB (3x8位像素，真彩色)

    RGBA（4x8位像素，带透明度遮罩的真彩色）。

    CMYK (4x8位像素，分色)

    YCbCr (3x8位像素，彩色视频格式)

        注意，这指的是JPEG，而不是ITU-R BT.2020，标准。

    LAB（3x8位像素，L*a*b色彩空间）

    HSV（3x8位像素，色调、饱和度、数值色彩空间）。

    I (32位有符号的整数像素)

    F (32位浮点像素)

Pillow还提供了对一些额外模式的有限支持，包括。

    LA (带阿尔法的L)

    PA (带阿尔法的P)

    RGBX（带填充的真彩色）

    RGBa（带预乘法的真彩色）。

    La (带预乘法的L)

    I;16 (16位无符号整数像素)

    I;16L (16位小字节无符号整数像素)

    I;16B （16 位大 endian 无符号整数像素）

    I;16N (16-bit native endian无符号整数像素)

    BGR;15 (15位反转真彩色)

    BGR;16 (16位反转真彩色)

    BGR;24 (24位反转真彩色)

    BGR;32 (32位反转真彩色)

然而，Pillow不支持用户定义的模式；
如果你需要处理上面没有列出的波段组合，请使用图像对象的序列。

你可以通过模式属性读取图像的模式。
这是一个包含上述数值之一的字符串。

"""