import sys
import requests
import random
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout, QStyle
from PyQt5.QtGui import QPalette, QColor
from libs import list_example_towns
from PyQt5.QtWidgets import QMainWindow

class GeWeather(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.app = QApplication([])
        self.app.setStyle("Fusion")
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor(240, 240, 240))
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor(53, 53, 53))
        palette.setColor(QPalette.WindowText, QColor(255, 255, 255))
        palette.setColor(QPalette.Base, QColor(15, 15, 15))
        palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
        palette.setColor(QPalette.ToolTipBase, QColor(255, 255, 255))
        palette.setColor(QPalette.ToolTipText, QColor.white)
        palette.setColor(QPalette.Text, QColor.white)
        palette.setColor(QPalette.Button, QColor(53, 53, 53))
        palette.setColor(QPalette.ButtonText, QColor.white)
        palette.setColor(QPalette.BrightText, QColor.red)
        palette.setColor(QPalette.Link, QColor(42, 130, 218))
        palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
        palette.setColor(QPalette.HighlightedText, QColor.black)
        self.setPalette(palette)

        self.l_city = QLabel('Enter the city name\'s : ')
        self.le_city = QLineEdit()
        self.l_temp = QLabel('')
        self.l_desc = QLabel('')
        self.l_pressure = QLabel('')
        self.l_humidity = QLabel('')
        self.l_wind = QLabel('')
        self.l_error = QLabel('')
        self.btn_get = QPushButton('Obtain weather')

        icon = self.style().standardIcon(getattr(QStyle, "SP_MessageBoxInformation"))
        self.btn_get.setIcon(icon)

        self.btn_get.clicked.connect(self.get_weather)

        self.le_city.setPlaceholderText(f"Ex: {random.choice(list_example_towns)}")
        self.le_city.returnPressed.connect(self.get_weather)

        hbox1 = QHBoxLayout()
        hbox1.addWidget(self.l_city)
        hbox1.addWidget(self.le_city)

        hbox2 = QHBoxLayout()
        hbox2.addWidget(self.l_temp)
        hbox2.addWidget(self.l_desc)

        hbox3 = QHBoxLayout()
        hbox3.addWidget(self.l_pressure)
        hbox3.addWidget(self.l_humidity)

        hbox4 = QHBoxLayout()
        hbox4.addWidget(self.l_wind)

        vbox = QVBoxLayout()
        vbox.addLayout(hbox1)
        vbox.addWidget(self.btn_get)
        vbox.addLayout(hbox2)
        vbox.addLayout(hbox3)
        vbox.addLayout(hbox4)

        self.setLayout(vbox)
        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Geweather App')
        self.show()

    def get_weather(self):
        city = self.le_city.text()
        api_key = "a34a9a778666f31118df724af632c616"
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
        response = requests.get(url)
        print(response.status_code)
        if response.status_code == 200:
            data = response.json()
            temp = data['main']['temp']
            desc = data['weather'][0]['description']
            pressure = data['main']['pressure']
            humidity = data['main']['humidity']
            wind = data['wind']['speed']
            self.l_temp.setText(f"Temperature: {temp}°C")
            self.l_desc.setText(f"Description: {desc}")
            self.l_pressure.setText(f"Pressure: {pressure} hPa")
            self.l_humidity.setText(f"Humidity : {humidity}%")
            self.l_wind.setText(f"Wind Speed : {wind} m/s")
        elif response.status_code == "404":
            self.l_city.setText("Error : Not Found")
            self.l_temp.setText(f"Error : Not Found")
            self.l_desc.setText(f"Error : Not Found")
            self.l_pressure.setText(f"Error : Not Found")
            self.l_humidity.setText(f"Error : Not Found")
            self.l_wind.setText(f"Error : Not Found")
            self.l_error.setText(f"Error : Not Found")
        elif response.status_code == 400:
            self.l_city.setText("Error : Nothing to search")
            self.l_temp.setText(f"Error : Nothing to search")
            self.l_desc.setText(f"Error : Nothing to search")
            self.l_pressure.setText(f"Error : Nothing to search")
            self.l_humidity.setText(f"Error : Nothing to search")
            self.l_wind.setText(f"Error : Nothing to search")
            self.l_error.setText(f"Error : Nothing to search")
        else:
            self.l_temp.setText(f"Error: {response.status_code}")
            self.l_desc.setText(f"Description: {response.status_code}")
            self.l_pressure.setText(f"Pressure: {response.status_code} hPa")
            self.l_humidity.setText(f"Humidity : {response.status_code}%")
            self.l_wind.setText(f"Wind Speed : {response.status_code} m/s")
            self.l_error.setText(f"An error was occured")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    GeWeather_app = GeWeather()
    sys.exit(app.exec_())
