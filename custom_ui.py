
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
        
        self.__temperature_value:float = 0
        self.__weather_status_value:int = 0
        self.__wind_speed_value:float = 0
        self.__is_day_value:bool = False
        self.__time_value:str = ""
        
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
        
        self.temperature_label = QLabel(parent=self, text=str(self.temperature_value) + "°C")
        self.temperature_label.setStyleSheet("font-size: 38px; background: transparent;")
        self.temperature_label.move((DataViewFrame.WIDTH - len(self.temperature_label.text()) * 18) // 2, 20)
        
        self.weather_status_label = QLabel(parent=self, text=str(self.weather_status))
        self.weather_status_label.setStyleSheet("font-size: 20px;background: transparent;")
        self.weather_status_label.move((DataViewFrame.WIDTH - len(self.weather_status_label.text()) * 9) // 2, 70)
        
        self.wind_speed_label = QLabel(parent=self, text="Wind-Speed: " + str(self.wind_speed_value))
        self.wind_speed_label.setStyleSheet("font-size: 18px; background: transparent;")
        self.wind_speed_label.move(10, 120)
        
        self.is_day_label = QLabel(parent=self, text="State: " + str(self.is_day))
        self.is_day_label.setStyleSheet("font-size: 16px; background: transparent;")
        self.is_day_label.move(270, 120)
        
        self.time_label = QLabel(parent=self, text=self.time_value)
        self.time_label.setStyleSheet("font-size: 20px; background: transparent;")
        self.time_label.move((DataViewFrame.WIDTH - len(self.time_label.text()) * 9) // 2, 170)
        
        # self.wind_direction_label = QLabel(parent=self, text="TEST")
        
        
        return None

    def update_content(self):
        """"""
        self.temperature_label.setText(str(self.temperature_value) + "°C")
        self.weather_status_label.setText(str(self.weather_status))
        self.wind_speed_label.setText("Wind-Speed: " + str(self.wind_speed_value) + "-Km/H")
        self.is_day_label.setText("State: " + "Day" if self.is_day else "Night")
        self.time_label.setText(self.time_value)

        self.temperature_label.move((DataViewFrame.WIDTH - len(self.temperature_label.text()) * 18) // 2, 20)
        self.weather_status_label.move((DataViewFrame.WIDTH - len(self.weather_status_label.text()) * 9) // 2, 70)
        self.wind_speed_label.move(10, 120)
        self.is_day_label.move(270, 120)
        self.time_label.move((DataViewFrame.WIDTH - len(self.time_label.text()) * 9) // 2, 170)
        

        return None
        


    @property
    def temperature_value(self):
        return self.__temperature_value
    
    @property
    def weather_status(self):
        return self.__weather_status_value
    
    @property
    def wind_speed_value(self):
        return self.__wind_speed_value
    
    @property
    def is_day(self):
        return self.__is_day_value
    
    @property
    def time_value(self):
        return self.__time_value
    
    def set_temperature(self, temperature: float):
        
        self.__temperature_value = temperature
        
        return None

    def set_weather_status(self, status: int):
        
        self.__weather_status_value = status
        
        return None
    
    def set_wind_speed(self, speed: float):
        
        self.__wind_speed_value = speed
        
        return None
    
    def set_is_day_value(self, value: bool):
        
        self.__is_day_value = value
        
        return None
    
    def set_time(self, _time: str):
        
        self.__time_value = _time
        
        return None

class SearchWidget(QFrame):
    """
        Docstring;
    """
    
    STYLESHEET = """
        background: transparent;
        border: 2px solid black;
        border-radius: 10px;
        color: white;
        font-size: 24px;
    """
    
    WIDTH = 320
    HEIGHT = 70
    
    MAX_CHAR_COUNT = 35
    
    class Signals(QObject):
        """"""
        
        text_changed = pyqtSignal(str)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.setStyleSheet(SearchWidget.STYLESHEET)
        self.setFixedSize(SearchWidget.WIDTH, SearchWidget.HEIGHT)
        
        self.signals = SearchWidget.Signals()
        
        self.search_text = ""
        
        self.setup_ui()
        
    def setup_ui(self):
        """"""
        
        self.__search_box = QLineEdit(parent=self)
        self.__search_box.setPlaceholderText("City Name")
        self.__search_box.setStyleSheet("border: none;")
        self.__search_box.setFixedSize(SearchWidget.WIDTH - 10, SearchWidget.HEIGHT - 10)
        self.__search_box.setAlignment(Qt.AlignCenter)
        self.__search_box.setMaxLength(SearchWidget.MAX_CHAR_COUNT)
        self.__search_box.textChanged.connect(self.__text_changed_event)
        self.__search_box.move(5, 5)
        
        
    def __text_changed_event(self, text: str):
        """"""
        self.signals.text_changed.emit(text)
        
        return None