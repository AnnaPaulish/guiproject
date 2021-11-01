# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import numpy as np
import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget


from MainApp import *

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Windows')
    window = MainApp()
    # window.receiver.start()
    # window.showMaximized()
    window.show()
    sys.exit(app.exec_())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
