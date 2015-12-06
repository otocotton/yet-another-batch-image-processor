import sys
from cx_Freeze import setup, Executable

includes = ["PySide.QtCore", "PySide.QtGui", "image_edit"]

base = None
if sys.platform == "win32":
    base = "Win32GUI"

exe = Executable(script = "hachi-mai.py",
                 icon = "resources/img/icon.ico",
                 base = base)

setup(name = "Hachi-Mai",
      version = "0.0.3",
      description = "batch-image-processor",
      executables = [exe],
      options = {"build_exe": {
                 "includes": includes},
      })