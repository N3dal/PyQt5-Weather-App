#!/usr/bin/python3
# -----------------------------------------------------------------
#
#
#
#
# Author:N84.
#
# Create Date:Sun Jul 30 16:45:40 2023.
# ///
# ///
# ///
# -----------------------------------------------------------------

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from sys import argv
from main_window import MainWindow


def main():
    
    app = QApplication(argv)
    
    root = MainWindow()
    
    root.show()
    
    exit(app.exec())
    
    
if __name__ == "__main__":
    main()