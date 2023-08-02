"""
    Docstring;
"""

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from defaults import *
import sys


class TitleBar(QFrame):
    """
        Docstring;
    """
    
    WIDTH = MAIN_WINDOW_MAX_WIDTH
    HEIGHT = 30
    
    STYLESHEET = """
        background-color: #718aab;
        color: black;
        border-top-right-radius: 10px;
        border-top-left-radius: 10px;
        border-bottom-right-radius: 0px;
        border-bottom-left-radius: 0px;
    """
    
    TITLE_LABEL_STYLESHEET = """
        color: black;
        font-size: 20px;
    """
    
    
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.__title = ""
        
        self.setStyleSheet(TitleBar.STYLESHEET)
        self.setFixedSize(TitleBar.WIDTH, TitleBar.HEIGHT)
        
        self.__setup_ui()
        
        
    def __setup_ui(self):
        """
            ::ARGS::
                None;
                
            ::INFO::
                setup the ui for the title bar;
                
            ::RETURNS::
                return None;
        """
        
        self.__close_button = QPushButton(parent=self)
        self.__close_button.setIcon(QIcon(CLOSE_BUTTON_IMAGE_PATH))
        self.__close_button.setIconSize(QSize(24, 24))
        self.__close_button.setCursor(Qt.PointingHandCursor)
        self.__close_button.clicked.connect(self.__close_button_event)
        self.__close_button.move(MAIN_WINDOW_MAX_WIDTH - 24 - 10, 3)
        
        self.__minimize_button = QPushButton(parent=self)
        self.__minimize_button.setIcon(QIcon(MINIMIZE_BUTTON_IMAGE_PATH))
        self.__minimize_button.setIconSize(QSize(24, 24))
        self.__minimize_button.setCursor(Qt.PointingHandCursor)
        self.__minimize_button.clicked.connect(self.__minimize_button_event)
        self.__minimize_button.move(MAIN_WINDOW_MAX_WIDTH - 24 * 3 - 10, 3)
        
        self.__title_label = QLabel(parent=self)
        self.__title_label.setStyleSheet(TitleBar.TITLE_LABEL_STYLESHEET)
        self.__title_label.setText(self.__title)
        self.__title_label.move((TitleBar.WIDTH - (len(self.__title) * 10)) // 2, 6)
        
    
    def __close_button_event(self):
        """
            ::ARGS::
                None;
                
            ::INFO::
                event call when the close button is clicked;
                
            ::RETURNS::
                return None;
        """ 
        
        sys.exit(0)
        
        return None
      
    def __minimize_button_event(self):
        """
            ::ARGS::
                None;
                
            ::INFO::
                event call when the minimize button is clicked;
                
            ::RETURNS::
                return None;
        """ 
        
        self.parent().showMinimized()
        
        return None
        
    def set_title(self, title:str) -> None:
        """
            ::ARGS::
                title:str => the new title for the title bar;
                
            ::INFO::
                set a new value for the title bar;
                
            ::RETURNS::
                return None;
        """
        
        self.__title = title
        
        self.__title_label.setText(self.__title)
        self.__title_label.move((TitleBar.WIDTH - (len(self.__title) * 10)) // 2, 6)
        
        
        return None 


class MainFrame(QFrame):
    
    windows = []
    
    STYLESHEET = """
        background-color: qlineargradient(x1: 0, x2: 3, stop: 0 #1f4284, stop: 1 #56caef);
        border-top-right-radius: 0px;
        border-top-left-radius: 0px;
        border-bottom-right-radius: 10px;
        border-bottom-left-radius: 10px;
        
    """
    
    WIDTH = MAIN_WINDOW_MAX_WIDTH
    HEIGHT = MAIN_WINDOW_MAX_HEIGHT - TitleBar.HEIGHT
    
    
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        if MainFrame.windows:
            raise Exception("You can't create more than one main window")
        
        self.setStyleSheet(MainFrame.STYLESHEET)
        
        self.setFixedSize(MainFrame.WIDTH, MainFrame.HEIGHT)
        
        
        
        MainFrame.windows.append(self)


class MainWindow(QMainWindow):
    """
        Docstring;
    """
    
    TITLE = "Weather App"
    
    STYLESHEET = """"""
    
    WIDTH = MAIN_WINDOW_MAX_WIDTH
    HEIGHT = MAIN_WINDOW_MAX_HEIGHT
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.setStyleSheet(MainWindow.STYLESHEET)
        self.setFixedSize(MainWindow.WIDTH, MainWindow.HEIGHT)
        
        
        # to remove the default title bar;
        self.setWindowFlag(Qt.FramelessWindowHint)
        
        # to hide the main window;
        self.setAttribute(Qt.WA_TranslucentBackground)
        
        
        # set the title bar;
        self.title_bar = TitleBar(parent=self)
        self.title_bar.setWindowOpacity(1)
        self.title_bar.set_title(MainWindow.TITLE)
        self.title_bar.move(0, 0)
        
        # set the main frame;
        self.main_frame = MainFrame(parent=self)
        self.main_frame.setWindowOpacity(1)
        self.main_frame.move(0, TitleBar.HEIGHT)
        self.main_frame.show()