#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os, sys
from PySide import QtGui, QtCore
from image_edit import ImageFactory

dst_ext = ".png"

class DropArea(QtGui.QFrame):
    ''' ('v') drag and drop area '''
    def __init__(self):
        super().__init__()
        # ('-') essentials
        self.setObjectName("DropArea")
        self.setAcceptDrops(True)
        self.setFixedSize(120, 120)

    def fileGate(self, event):
        # ('o') detects dragged-in files
        if event.mimeData().hasUrls() \
        and not os.path.isdir([url.toLocalFile() for url in event.mimeData().urls()][0]):
            event.accept()
            return True
        else:
            event.ignore()
            return False


class AreaResizeWidth(DropArea):
    ''' ('v') resize width '''
    def __init__(self):
        super().__init__()
        self.setObjectName("AreaResizeWidth")

        self.sb_width = QtGui.QSpinBox()
        self.sb_width.setObjectName("sb_width")
        self.sb_width.setMinimum(100)
        self.sb_width.setMaximum(2000)
        self.sb_width.setSingleStep(10)
        self.sb_width.setValue(500)
        self.sb_width.setFixedSize(40, 28)
        self.sb_width.setAlignment(QtCore.Qt.AlignCenter)
        self.sb_width.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)

        self.vb = QtGui.QVBoxLayout()
        self.vb.addWidget(self.sb_width)
        self.vb.setAlignment(QtCore.Qt.AlignCenter)
        self.setLayout(self.vb)

    def dragEnterEvent(self, event):
        # ('o') called when files are dragged-in the area
        if self.fileGate(event):
            print("entered in the 'AreaResizeWidth'")
            self.setStyleSheet("QFrame#AreaResizeWidth{border: 1px solid #CCCCCC;}")

    def dragLeaveEvent(self, event):
        # ('o') called when files leave from the area
        print("leaved from the 'AreaResizeWidth'")
        self.setStyleSheet("QFrame#AreaResizeWidth{border: 1px solid #FCFCFC;}")

    def dropEvent(self, event):
        # ('o') called when files are dropped-into the area
        print("dropped into the 'AreaResizeWidth'")
        ext = dst_ext
        width = self.sb_width.value()
        file = [url.toLocalFile() for url in event.mimeData().urls()]
        ImageFactory(file).resize_width(ext, width)
        self.setStyleSheet("QFrame#AreaResizeWidth{border: 1px solid #FCFCFC;}")


class AreaResizeHeight(DropArea):
    ''' ('v') resize height '''
    def __init__(self):
        super().__init__()
        self.setObjectName("AreaResizeHeight")

        self.sb_height = QtGui.QSpinBox()
        self.sb_height.setObjectName("sb_height")
        self.sb_height.setMinimum(100)
        self.sb_height.setMaximum(2000)
        self.sb_height.setSingleStep(10)
        self.sb_height.setValue(500)
        self.sb_height.setFixedSize(40, 28)
        self.sb_height.setAlignment(QtCore.Qt.AlignCenter)
        self.sb_height.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)

        self.vb = QtGui.QVBoxLayout()
        self.vb.addWidget(self.sb_height)
        self.vb.setAlignment(QtCore.Qt.AlignCenter)
        self.setLayout(self.vb)

    def dragEnterEvent(self, event):
        # ('o') called when files are dragged-in the area
        if self.fileGate(event):
            print("entered in the 'AreaResizeHeight'")
            self.setStyleSheet("QFrame#AreaResizeHeight{border: 1px solid #CCCCCC;}")

    def dragLeaveEvent(self, event):
        # ('o') called when files leave from the area
        print("leaved from the 'AreaResizeHeight'")
        self.setStyleSheet("QFrame#AreaResizeHeight{border: 1px solid #FCFCFC;}")

    def dropEvent(self, event):
        # ('o') called when files are dropped-into the area
        print("dropped into the 'AreaResizeHeight'")
        ext = dst_ext
        height = self.sb_height.value()
        file = [url.toLocalFile() for url in event.mimeData().urls()]
        ImageFactory(file).resize_height(ext, height)
        self.setStyleSheet("QFrame#AreaResizeHeight{border: 1px solid #FCFCFC;}")


class AreaRotateRight(DropArea):
    ''' ('v') rotate right '''
    def __init__(self):
        super().__init__()
        self.setObjectName("AreaRotateRight")

    def dragEnterEvent(self, event):
        # ('o') called when files are dragged-in the area
        if self.fileGate(event):
            print("entered in the 'AreaResizeHeight'")
            self.setStyleSheet("QFrame#AreaRotateRight{border: 1px solid #CCCCCC;}")

    def dragLeaveEvent(self, event):
        # ('o') called when files leave from the area
        print("leaved from the 'AreaResizeHeight'")
        self.setStyleSheet("QFrame#AreaRotateRight{border: 1px solid #FCFCFC;}")

    def dropEvent(self, event):
        # ('o') called when files are dropped-into the area
        print("dropped into the 'AreaResizeHeight'")
        ext = dst_ext
        file = [url.toLocalFile() for url in event.mimeData().urls()]
        ImageFactory(file).rotate_right(ext)
        self.setStyleSheet("QFrame#AreaRotateRight{border: 1px solid #FCFCFC;}")


class AreaRotateLeft(DropArea):
    ''' ('v') rotate left '''
    def __init__(self):
        super().__init__()
        self.setObjectName("AreaRotateLeft")

    def dragEnterEvent(self, event):
        # ('o') called when files are dragged-in the area
        if self.fileGate(event):
            print("entered in the 'AreaRotateLeft'")
            self.setStyleSheet("QFrame#AreaRotateLeft{border: 1px solid #CCCCCC;}")

    def dragLeaveEvent(self, event):
        # ('o') called when files leave from the area
        print("leaved from the 'AreaRotateLeft'")
        self.setStyleSheet("QFrame#AreaRotateLeft{border: 1px solid #FCFCFC;}")

    def dropEvent(self, event):
        # ('o') called when files are dropped-into the area
        print("dropped into 'AreaRotateLeft'")
        ext = dst_ext
        file = [url.toLocalFile() for url in event.mimeData().urls()]
        ImageFactory(file).rotate_left(ext)
        self.setStyleSheet("QFrame#AreaRotateLeft{border: 1px solid #FCFCFC;}")

class AreaConcatenateHorizontal(DropArea):
    ''' ('v') concatenate horizontal '''
    def __init__(self):
        super().__init__()
        self.setObjectName("AreaConcatenateHorizontal")

    def dragEnterEvent(self, event):
        # ('o') called when files are dragged-in the area
        if len([url for url in event.mimeData().urls()]) < 2:
            print("'concatenate' requires more than 2 images.")
            event.ignore()
        elif self.fileGate(event):
            print("entered in the 'AreaConcatenateHorizontal'")
            self.setStyleSheet("QFrame#AreaConcatenateHorizontal{border: 1px solid #CCCCCC;}")

    def dragLeaveEvent(self, event):
        # ('o') called when files leave from the area
        print("leaved from the 'AreaConcatenateHorizontal'")
        self.setStyleSheet("QFrame#AreaConcatenateHorizontal{border: 1px solid #FCFCFC;}")

    def dropEvent(self, event):
        # ('o') called when files are dropped-into the area
        print("dropped into the 'AreaConcatenateHorizontal'")
        ext = dst_ext
        file = [url.toLocalFile() for url in event.mimeData().urls()]
        ImageFactory(file).concatenate_horizontal(ext)
        self.setStyleSheet("QFrame#AreaConcatenateHorizontal{border: 1px solid #FCFCFC;}")


class AreaConcatenateVertical(DropArea):
    ''' ('v') concatenate vertical '''
    def __init__(self):
        super().__init__()
        self.setObjectName("AreaConcatenateVertical")

    def dragEnterEvent(self, event):
        # ('o') called when files are dragged-in the area
        if len([url for url in event.mimeData().urls()]) < 2:
            print("'concatenate' requires more than 2 images.")
            event.ignore()
        elif self.fileGate(event):
            print("entered in the 'AreaConcatenateVertical'")
            self.setStyleSheet("QFrame#AreaConcatenateVertical{border: 1px solid #CCCCCC;}")

    def dragLeaveEvent(self, event):
        # ('o') called when files leave from the area
        print("leaved from the 'AreaConcatenateVertical'")
        self.setStyleSheet("QFrame#AreaConcatenateVertical{border: 1px solid #FCFCFC;}")

    def dropEvent(self, event):
        # ('o') called when files are dropped-into the area
        print("dropped into the 'AreaConcatenateVertical'")
        ext = dst_ext
        file = [url.toLocalFile() for url in event.mimeData().urls()]
        ImageFactory(file).concatenate_vertical(ext)
        self.setStyleSheet("QFrame#AreaConcatenateVertical{border: 1px solid #FCFCFC;}")


class AreaPngquant(DropArea):
    ''' ('v') concatenate vertical '''
    def __init__(self):
        super().__init__()
        self.setObjectName("AreaPngquant")

    def dragEnterEvent(self, event):
        # ('o') called when files are dragged-in the area
        if self.fileGate(event):
            f, e = os.path.splitext([url.toLocalFile() for url in event.mimeData().urls()][0])
            if e == ".png":
                print("entered in the 'AreaPngquant'")
                self.setStyleSheet("QFrame#AreaPngquant{border: 1px solid #CCCCCC;}")
            else:
                print("pngquant is only for PNG fiels")
                event.ignore()

    def dragLeaveEvent(self, event):
        # ('o') called when files leave from the area
        print("leaved from the 'AreaPngquant'")
        self.setStyleSheet("QFrame#AreaPngquant{border: 1px solid #FCFCFC;}")

    def dropEvent(self, event):
        # ('o') called when files are dropped-into the area
        print("dropped into the 'AreaPngquant'")
        ext = dst_ext
        file = [url.toLocalFile() for url in event.mimeData().urls()]
        ImageFactory(file).pngquant()
        self.setStyleSheet("QFrame#AreaPngquant{border: 1px solid #FCFCFC;}")


class AreaConvert(DropArea):
    ''' ('v') convert files and can select dst_ext '''
    def __init__(self):
        super().__init__()
        self.setObjectName("AreaConvert")

        self.rb_png = QtGui.QRadioButton()
        self.rb_png.setObjectName("rb_png")
        self.rb_png.setChecked(True)
        self.rb_png.toggled.connect(self.rb_pngToggled)

        self.rb_jpg = QtGui.QRadioButton()
        self.rb_jpg.setObjectName("rb_jpg")
        self.rb_jpg.setChecked(False)
        self.rb_jpg.toggled.connect(self.rb_jpgToggled)

        self.rb_bmp = QtGui.QRadioButton()
        self.rb_bmp.setObjectName("rb_bmp")
        self.rb_bmp.setChecked(False)
        self.rb_bmp.toggled.connect(self.rb_bmpToggled)

        self.vb = QtGui.QVBoxLayout()
        self.vb.addWidget(self.rb_png)
        self.vb.addWidget(self.rb_jpg)
        self.vb.addWidget(self.rb_bmp)
        self.vb.setAlignment(QtCore.Qt.AlignCenter)
        self.setLayout(self.vb)

    def rb_pngToggled(self):
        # ('o') called when rb_png toggled
        if self.rb_png.isChecked():
            global dst_ext
            dst_ext = ".png"
            print("dst_ext: .png")
        else:
            pass

    def rb_jpgToggled(self):
        # ('o') called when rb_jpg toggled
        if self.rb_jpg.isChecked():
            global dst_ext
            dst_ext = ".jpg"
            print("dst_ext: .jpg")
        else:
            pass

    def rb_bmpToggled(self):
        # ('o') called when rb_bmp toggled
        if self.rb_bmp.isChecked():
            global dst_ext
            dst_ext = ".bmp"
            print("dst_ext: .bmp")
        else:
            pass

    def dragEnterEvent(self, event):
        # ('o') called when files are dragged-in the area
        if self.fileGate(event):
            print("entered in the 'AreaConvert'")
            self.setStyleSheet("QFrame#AreaConvert{border: 1px solid #CCCCCC;}")

    def dragLeaveEvent(self, event):
        # ('o') called when files leave from the area
        print("leaved from the 'AreaConvert'")
        self.setStyleSheet("QFrame#AreaConvert{border: 1px solid #FCFCFC;}")

    def dropEvent(self, event):
        # ('o') called when files are dropped-into the area
        print("dropped into the 'AreaConvert'")
        ext = dst_ext
        file = [url.toLocalFile() for url in event.mimeData().urls()]
        ImageFactory(file).convert(ext)
        self.setStyleSheet("QFrame#AreaConvert{border: 1px solid #FCFCFC;}")

class MainWidget(QtGui.QWidget):
    ''' ('v') main window class, contains all of the widgets '''
    def __init__(self):
        super().__init__()
        # ('-') essentials
        self.setObjectName("MainWidget")
        self.setWindowTitle("Gahen")
        self.setFixedSize(580, 300)
        self.setCSS()
        # ('-') yum yum
        self.main_grid = QtGui.QGridLayout()
        self.main_grid.addWidget(AreaResizeWidth(), 0, 0)
        self.main_grid.addWidget(AreaResizeHeight(), 0, 1)
        self.main_grid.addWidget(AreaConcatenateHorizontal(), 0, 2)
        self.main_grid.addWidget(AreaPngquant(), 0, 3)
        self.main_grid.addWidget(AreaRotateLeft(), 1, 0)
        self.main_grid.addWidget(AreaRotateRight(), 1, 1)
        self.main_grid.addWidget(AreaConcatenateVertical(), 1, 2)
        self.main_grid.addWidget(AreaConvert(), 1, 3)
        # self.main_grid.setSpacing(10)
        self.setLayout(self.main_grid)

    def setCSS(self):
        # ('o') set stylesheet from an external file
        with open("stylesheet.css","r") as style:
            self.setStyleSheet("".join(style.readlines()))


def main():
    ''' ('v') main class, run the program '''
    QtCore.QTextCodec.setCodecForCStrings(QtCore.QTextCodec.codecForLocale())
    # ('-') set icon
    app = QtGui.QApplication(sys.argv)
    app_icon = QtGui.QIcon(QtGui.QPixmap("resources/img/icon.png"))
    app.setWindowIcon(app_icon)
    # ('-') show
    win = MainWidget()
    win.show()
    # ('-') execute
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
