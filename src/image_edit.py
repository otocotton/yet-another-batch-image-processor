#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os, sys
from PIL import Image

accepted_formats = [
    ".gif",
    ".jpg", ".jpeg", ".jfif", ".jfi", ".jp2", ".j2c",
    ".png",
    ".tiff", ".tif",
    ".webp",
    ".bmp"
]

class ImageFactory():
    def __init__(self, file):
        super().__init__()
        print("'ImageFactory' is called")
        self.file = file
        for srcfile in self.file:
            f, e = os.path.splitext(srcfile)
            if e.lower() in accepted_formats:
                print("'file' is in 'accepted_formats'")
            else:
                print("cannot open", srcfile)
                print("accepted_formats:", accepted_formats)

    def convert(self, ext):
        print("'convert' is called")
        file = self.file
        for srcfile in file:
            f, e = os.path.splitext(srcfile)
            dstfile = f + ext
            try:
                print("open:" + os.path.basename(srcfile))
                with Image.open(srcfile) as img:
                    img.save(dstfile)
                    print("converted:", os.path.basename(dstfile))
                    print("'convert' finished")
            except IOError:
                print("cannot convert", srcfile)

    def resize_width(self, ext, width):
        print("'resize_width' is called")
        file = self.file
        for srcfile in file:
            f, e = os.path.splitext(srcfile)
            dstfile = f + "_tw" + ext
            try:
                print("open:" + os.path.basename(srcfile))
                with Image.open(srcfile) as img:
                    print("original size:", img.size)
                    size = (width, img.size[1])
                    img.thumbnail(size)
                    img.save(dstfile)
                    print("resized:", img.size)
                    print("'resize_width' finished")
            except IOError:
                print("cannot resize", srcfile)

    def resize_height(self, ext, height):
        print("'resize_height' is called")
        file = self.file
        for srcfile in file:
            f, e = os.path.splitext(srcfile)
            dstfile = f + "_th" + ext
            try:
                print("open:" + os.path.basename(srcfile))
                with Image.open(srcfile) as img:
                    print("original size:", img.size)
                    size = (img.size[0], height)
                    img.thumbnail(size)
                    img.save(dstfile)
                    print("resized:", img.size)
                    print("'resize_height' finished")
            except IOError:
                print("cannot resize", srcfile)

    def rotate_right(self, ext):
        print("'rotate_right' is called")
        file = self.file
        for srcfile in file:
            f, e = os.path.splitext(srcfile)
            dstfile = f + "_rr" + ext
            try:
                print("open:" + os.path.basename(srcfile))
                with Image.open(srcfile) as img:
                    print("'direction' is 'right'")
                    img.transpose(Image.ROTATE_270).save(dstfile)
                    print("'rotate_right' finished")
            except IOError:
                print("cannot rotate", srcfile)

    def rotate_left(self, ext):
        print("'rotate_left' is called")
        file = self.file
        for srcfile in file:
            f, e = os.path.splitext(srcfile)
            dstfile = f + "_rl" + ext
            try:
                print("open:" + os.path.basename(srcfile))
                with Image.open(srcfile) as img:
                    print("'direction' is 'right'")
                    img.transpose(Image.ROTATE_90).save(dstfile)
                    print("'rotate_left' finished")
            except IOError:
                print("cannot rotate", srcfile)

    def concatenate_horizontal(self, ext):
        print("'concatenate_horizontal' is called")
        file = self.file
        print("file:", file)

        f, e = os.path.splitext(file[0])
        dstfile = f + "_ch" + ext
        min_height = min(Image.open(i).size[1] for i in file)
        print("min_height:", min_height)

        width_list = []
        for srcfile in file:
            with Image.open(srcfile) as img:
                size = (img.size[0], min_height)
                img.thumbnail(size)
                width_list.append(img.size[0])
        print("width_list:", width_list)
        sum_width = sum(width_list)
        print("sum_width:", sum_width)
        canvas_size = (sum_width, min_height)
        canvas = Image.new("RGBA", canvas_size)
        print("canvas.size:", canvas.size)

        pos_x = 0
        try:
            for srcfile in file:
                with Image.open(srcfile) as img:
                    size = (img.size[0], min_height)
                    img.thumbnail(size)
                    print("img.size:", img.size)
                    canvas.paste(img, (pos_x, 0))
                    pos_x += img.size[0]
            print("dstfile.size:", canvas.size)
            canvas.save(dstfile)
        except IOError:
            print("cannot 'concatenate_horizontal'", srcfile)

    def concatenate_vertical(self, ext):
        print("'concatenate_vertical' is called")
        file = self.file
        print("file:", file)

        f, e = os.path.splitext(file[0])
        dstfile = f + "_cv.png"
        min_width = min(Image.open(i).size[0] for i in file)
        print("min_width:", min_width)

        height_list = []
        for srcfile in file:
            with Image.open(srcfile) as img:
                size = (min_width, img.size[1])
                img.thumbnail(size)
                height_list.append(img.size[1])
        print("height_list:", height_list)
        sum_height = sum(height_list)
        print("sum_height:", height_list)
        canvas_size = (min_width, sum_height)
        canvas = Image.new("RGBA", canvas_size)
        print("canvas.size:", canvas.size)

        pos_y = 0
        try:
            for srcfile in file:
                with Image.open(srcfile) as img:
                    size = (min_width, img.size[1])
                    img.thumbnail(size)
                    print("img.size:", img.size)
                    canvas.paste(img, (0, pos_y))
                    pos_y += img.size[1]
            print("dstfile.size:", canvas.size)
            canvas.save(dstfile)
        except IOError:
            print("cannot 'concatenate_vertical'", srcfile)

    def pngquant(self):
        print("'pngquant' is called")
        pq = "resources\\pngquant\\pngquant.exe"
        op = " --force --verbose --ext _256.png 256 "
        file = self.file
        for srcfile in file:
            print(srcfile)
            try:
                cmd = pq + op + srcfile
                os.system(cmd)
            except IOError:
                print("cannot convert with pngquant", srcfile)
        print("'pngquant' finished")
