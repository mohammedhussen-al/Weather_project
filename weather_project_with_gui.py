from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QLineEdit, QPushButton, QLabel, QLayout
from PyQt5.QtCore import Qt
import requests
import json
import sys

class mainwindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Wather App")
        self.setFixedSize(300,150)
        self.lable = QLabel("")
        self.lable2 = QLabel("")

        self.line = QLineEdit()
        self.button = QPushButton()
        

        self.initui()
    def initui(self):
        self.hbox = QHBoxLayout()
        self.vbox = QVBoxLayout()
        self.hbox2 = QHBoxLayout()
        self.hbox.addWidget(self.line)
        self.hbox.addWidget(self.button)
        self.vbox.addLayout(self.hbox)
        self.hbox2.addWidget(self.lable)
        self.hbox2.addWidget(self.lable2)
        self.vbox.addLayout(self.hbox2)
        self.setLayout(self.vbox)

        self.lable.setAlignment(Qt.AlignLeft)
        self.lable2.setAlignment(Qt.AlignRight)
        self.city_in_text = self.line.text()
        self.button.clicked.connect(self.start)

    def start(self): 
        self.city_in_text = self.line.text() 
        url1 = "http://api.openweathermap.org/geo/1.0/direct?q={cit},IQ&limit=1&appid={Your weather Api openweathermap.org}".format(cit=self.city_in_text)
        self.geocode_responses = requests.get(url1)
        if self.geocode_responses.status_code == 200:
            self.geocode = self.geocode_responses.json()
            city = self.geocode[0]
            self.weather_func(lat= city["lat"], lon= city["lon"])
    def weather_func(self, lat, lon):
        url2 = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={Your weather Api openweathermap.org}&units=metric"
        self.weather = requests.get(url2)
        if self.weather.status_code == 200:
            self.weather = self.weather.json()
            self.data_weather = self.weather["weather"][0]
            self.date_temp= self.weather["main"]
            self.data_wind= self.weather["wind"]
            self.lable.setText(f"temp: {str(self.date_temp['temp'])}c* \nFeels like: {str(self.date_temp['feels_like'])}c* \n")
            self.lable2.setText(f"{self.data_weather['description']}\nHumidity: {self.date_temp['humidity']}%\nWind speed: {self.data_wind['speed']}km/h")
app = QApplication(sys.argv)
window = mainwindow()
window.show()
sys.exit(app.exec_())



                             
# {
#   "coord": {
#     "lon": 10.99,
#     "lat": 44.34
#   },
#   "weather": [
#     {
#       "id": 501,
#       "main": "Rain",
#       "description": "moderate rain",
#       "icon": "10d"
#     }
#   ],
#   "base": "stations",
#   "main": {
#     "temp": 298.48,
#     "feels_like": 298.74,
#     "temp_min": 297.56,
#     "temp_max": 300.05,
#     "pressure": 1015,
#     "humidity": 64,
#     "sea_level": 1015,
#     "grnd_level": 933
#   },
#   "visibility": 10000,
#   "wind": {
#     "speed": 0.62,
#     "deg": 349,
#     "gust": 1.18
#   },
#   "rain": {
#     "1h": 3.16
#   },
#   "clouds": {
#     "all": 100
#   },
#   "dt": 1661870592,
#   "sys": {
#     "type": 2,
#     "id": 2075663,
#     "country": "IT",
#     "sunrise": 1661834187,
#     "sunset": 1661882248
#   },
#   "timezone": 7200,
#   "id": 3163858,
#   "name": "Zocca",
#   "cod": 200
# }
                             
                           