import weather_app
import time
import design
import sys
from PyQt5 import QtWidgets
import os
from PyQt5.QtGui import QIcon, QPixmap



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
        self.rain = QPixmap('icon/rain.png')
        self.cloudl = QPixmap('icon/cloudly.png')
        self.sun = QPixmap('icon/sun.png')
        # self.icon_1.setScaledContents(True)
        # self.icon_1.setPixmap(sun)
        self.pushSearch.clicked.connect(self.setCity)
        self.pushRefresh.clicked.connect(self.refresh)
        run = True
        if run:
            self.sendWeather('Київ')
            run = False

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
        timelist = [self.time_1, self.time_2, self.time_3, self.time_4, self.time_5, self.time_6, self.time_7,
                    self.time_8]
        timelistinf = [self.time_1_inf, self.time_2_inf, self.time_3_inf, self.time_4_inf, self.time_5_inf,
                       self.time_6_inf, self.time_7_inf, self.time_8_inf]
        iconlist = [self.icon_1, self.icon_2, self.icon_3, self.icon_4, self.icon_5, self.icon_6, self.icon_7, self.icon_8]

        for i in range(8):
            timelist[i].clear()
            timelistinf[i].clear()
            # iconlist[i].clear()
        try:
            wh = weather_app.NowWeather(city)
            city = wh.getCity()
            self.listInfo.setText(wh.getNowDate() + '\n' + wh.getNowInfo())
            self.listCity.setText(city)
            self.listCelsius.setText(wh.getNowCelsius())
        except:
            wh = weather_app.NowWeather('Київ')
            self.listInfo.setText(wh.getNowDate() + '\n' + wh.getNowInfo())
            self.listCity.setText(city)
            self.listCelsius.setText(wh.getNowCelsius())
            self.lineSearch.setText('Місто не знайдено...')

        if wh.getNowInfo().upper().find('ХМАРН') != -1:
            self.iconToday.setPixmap(self.cloudl)
        if wh.getNowInfo().upper().find('ДОЩ') != -1:
            self.iconToday.setPixmap(self.rain)
        if wh.getNowInfo().upper().find('ОНЯЧНО') != -1:
            self.iconToday.setPixmap(self.sun)
        wh = weather_app.DayWeather(city)
        tm = ['2', '5', '8', '11', '14', '17', '20', '23']
        for i in range(8):
            timelist[i].setText(wh.getToday()[0][tm[i]])
            timelistinf[i].setText(wh.getToday()[1][tm[i]] + '\n' + wh.getToday()[2][tm[i]])
            if wh.getToday()[2][tm[i]].upper().find('ХМАРН') != -1:
                iconlist[i].setPixmap(self.cloudl)
            if wh.getToday()[2][tm[i]].upper().find('ДОЩ') != -1:
                iconlist[i].setPixmap(self.rain)
            if wh.getToday()[2][tm[i]].upper().find('ОНЯЧНО') != -1:
                iconlist[i].setPixmap(self.sun)


        day = wh.getDay(1)
        self.listDay_1.setText(
            day['day'] + '\n' + 'Min: ' + day['min'] + '\n' + 'Max: ' + day['max'] + '\n' + day['inf'])

        day = wh.getDay(2)
        self.listDay_2.setText(
            day['day'] + '\n' + 'Min: ' + day['min'] + '\n' + 'Max: ' + day['max'] + '\n' + day['inf'])

        day = wh.getDay(3)
        self.listDay_3.setText(
            day['day'] + '\n' + 'Min: ' + day['min'] + '\n' + 'Max: ' + day['max'] + '\n' + day['inf'])

        day = wh.getDay(4)
        self.listDay_4.setText(
            day['day'] + '\n' + 'Min: ' + day['min'] + '\n' + 'Max: ' + day['max'] + '\n' + day['inf'])


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = App()
    window.setWindowTitle('Arch Weather')

    window.show()

    app.exec_()
