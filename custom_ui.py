
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from defaults import *
import sys


class DataViewFrame(QFrame):
    """
        used to view the weather data;
    """
    
    STYLESHEET = """
        border: 0px solid black;
        border-radius: 15px;
    
    """
    
    WIDTH = 400
    HEIGHT = 200
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.setFixedSize(DataViewFrame.WIDTH, DataViewFrame.HEIGHT)
        self.setStyleSheet(DataViewFrame.STYLESHEET)
        
        self.__setup_ui()
    
    def __setup_ui(self):
        """
            ::ARGS::
                None;
                
            ::INFO::
                setup the ui for the DataViewFrame;
                
            ::RETURNS::
                return None;
        """  
        
        label = QLabel(parent=self, text="TEST")
        
        label.move(10, 10)
        
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