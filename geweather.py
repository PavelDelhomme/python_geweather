import sys
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout


class GeWeather(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.l_city = QLabel('Enter the city name\'s : ')
        self.le_city = QLineEdit()
        self.l_temp = QLabel('')
        self.l_desc = QLabel('')
        self.l_pressure = QLabel('')
        self.l_humidity = QLabel('')
        self.l_wind = QLabel('')
        self.l_error = QLabel('')
        self.btn_get = QPushButton('Obtain weather')
        self.btn_get.clicked.connect(self.get_weather)

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
