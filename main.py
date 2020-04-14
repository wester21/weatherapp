import weather_app
import time
import design
import sys
from PyQt5 import QtWidgets
import os


def sendMess(message):
    os.system('notify-send "%s"' % (message))


class App(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.listInfo.clear()
        self.listCelsius.clear()
        self.listCity.clear()
        self.listDay_1.clear()
        self.listDay_2.clear()
        self.listDay_3.clear()
        self.listDay_4.clear()
        self.textMain.setText('ArchWeather')
        self.pushSearch.clicked.connect(self.setCity)
        self.pushRefresh.clicked.connect(self.refresh)


    def setCity(self):
        self.city = self.lineSearch.text()
        self.sendWeather(self.city)

    def refresh(self):
        self.sendWeather(self.city)

    def sendWeather(self, city):
        self.listInfo.clear()
        self.listCelsius.clear()
        self.listCity.clear()
        self.listDay_1.clear()
        self.listDay_2.clear()
        self.listDay_3.clear()
        self.listDay_4.clear()
        wh = weather_app.NowWeather(city)
        city = wh.getCity()
        self.listInfo.setText(wh.getNowInfo() + ', ' + wh.getNowDate())
        self.listCity.setText(city)
        self.listCelsius.setText(wh.getNowCelsius())
        wh = weather_app.DayWeather(city)

        day = wh.getDay(1)
        self.listDay_1.setText(day['day'] + '\n' + 'Min: ' + day['min'] + '\n' + 'Max: ' + day['max'] + '\n' + day['inf'])

        day = wh.getDay(2)
        self.listDay_2.setText(day['day'] + '\n' + 'Min: ' + day['min'] + '\n' + 'Max: ' + day['max'] + '\n' + day['inf'])

        day = wh.getDay(3)
        self.listDay_3.setText(day['day'] + '\n' + 'Min: ' + day['min'] + '\n' + 'Max: ' + day['max'] + '\n' + day['inf'])

        day = wh.getDay(4)
        self.listDay_4.setText(day['day'] + '\n' + 'Min: ' + day['min'] + '\n' + 'Max: ' + day['max'] + '\n' + day['inf'])


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = App()
    window.setWindowTitle('Arch Weather')

    window.show()

    app.exec_()

