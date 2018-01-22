#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'sumdy'

from PIL import Image, ImageDraw, ImageFont
from io import BytesIO


# 旋转
def img_rotate(file_name, angle, resample=Image.BICUBIC, expand=True):
    img = Image.open(file_name)
    out = img.rotate(angle, resample, expand)
    # file_handler.close()
    img_bytes = BytesIO()
    out.save(img_bytes, 'PNG')
    return img_bytes


# 加水印
# image: 图片  text：要添加的文本 font：字体

def add_text_to_image(file_name, text, font=ImageFont.truetype('C:\Windows\Fonts\simhei.ttf', 50)):
    image = Image.open(file_name)
    rgba_image = image.convert('RGBA')
    text_overlay = Image.new('RGBA', rgba_image.size, (255, 255, 255, 0))
    image_draw = ImageDraw.Draw(text_overlay)

    text_size_x, text_size_y = image_draw.textsize(text, font=font)
    # 设置文本文字位置
    print(rgba_image)
    text_xy = (rgba_image.size[0] / 2 - text_size_x / 2, rgba_image.size[1] / 2 - text_size_y / 2)
    # 设置文本颜色和透明度
    image_draw.text(text_xy, text, font=font, fill=(0, 0, 0, 300))

    image_with_text = Image.alpha_composite(rgba_image, text_overlay)
    img_bytes = BytesIO()
    image_with_text.save(img_bytes, 'PNG')
    return img_bytes


if __name__ == '__main__':
    img_rotate('5.jpg',60)
    # im_after = add_text_to_image("123.png", '潭州python学院公开课堂')

    # f = open('123.JPG', 'rb')
    # a = img_rotate(f, -30)
# img_f = open('123.png', 'rb')
# img = Image.open(img_f)
# out = img.rotate(30, expand=True)
# # img.show()
# out.show()
# img_f.close()