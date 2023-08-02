
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from defaults import *
import sys


class DataViewWidget(QWidget):
    """
        used to view the weather data;
    """
    
    STYLESHEET = """
        border: solid black 2px;
    
    """
    
    WIDTH = 200
    HEIGHT = 200
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.setFixedSize(DataViewWidget.WIDTH, DataViewWidget.HEIGHT)
        self.setStyleSheet(DataViewWidget.STYLESHEET)
        
        self.__setup_ui()
    
    def __setup_ui(self):
        """
            ::ARGS::
                None;
                
            ::INFO::
                setup the ui for the DataViewWidget;
                
            ::RETURNS::
                return None;
        """  
        
        return None

class SearchWidget(QWidget):
    """
        Docstring;
    """
    
    STYLESHEET = """
    
    """
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        pass