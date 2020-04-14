import requests
from bs4 import BeautifulSoup


class NowWeather:
    def __init__(self, city):
        self.googurl = 'https://www.google.com/search?q=weather+'
        page = requests.get(self.googurl + city)
        self.soup = BeautifulSoup(page.content, 'lxml')

    def getCity(self):
        temp = str(self.soup.findAll('span', {'class':'BNeawe tAd8D AP7Wnd'})[0].text).split(' ')[0]
        return temp[:-1]

    def getNowDate(self):
        temp = str(self.soup.findAll('div', {'class':'BNeawe tAd8D AP7Wnd'})[0].text).split(' ')
        size = len(temp)
        result = []
        result.append(temp[0].capitalize())
        result.append(str(temp[1][0:5]))
        return " ".join(result)


    def getNowInfo(self):
        temp = str(self.soup.findAll('div', {'class':'BNeawe tAd8D AP7Wnd'})[0].text).split(' ')
        size = len(temp)
        result = []
        result.append(str(temp[1][6:]))
        for x in range(size - 2):
            result.append(str(temp[x+2]))
        return " ".join(result)

    def getNowCelsius(self):
        return self.soup.findAll('div', {'class': 'BNeawe iBp4i AP7Wnd'})[0].text


class DayWeather:
    def __init__(self, city):
        url = 'https://ua.sinoptik.ua/погода-'+city
        page = requests.get(url)
        self.soup =  BeautifulSoup(page.content, 'lxml')

    def getDay(self, day):
        temp = str(self.soup.findAll('div', {'id':'bd'+str(day)})[0].text).split(' ')
        temp_1 = str(self.soup.findAll('div', {'class':'weatherIco'})[day-1])
        inf = ''
        x = 36
        i = temp_1[x]
        while i != '"':
            inf     += i
            x+=1
            i = temp_1[x]
        result = {
            'day': temp[1],
            'inf': inf,
            'num': temp[2],
            'mounth': temp[3],
            'min': temp[8],
            'max': temp[10]
        }
        return result
    def getToday(self):
        temp = str(self.soup.findAll('tr', {'class':'gray time'})[0].text).split(' ')
        time = {
            '2':temp[1]+temp[2],
            '5':temp[4]+temp[5],
            '8':temp[7]+temp[8],
            '11':temp[10]+temp[11],
            '14': temp[13] + temp[14],
            '17': temp[16] + temp[17],
            '20': temp[19] + temp[20],
            '23': temp[22] + temp[23],
            }
        temp = str(self.soup.findAll('tr', {'class':'temperature'})[0].text).split(' ')
        temperature = {
            '2':temp[1],
            '5':temp[2],
            '8':temp[3],
            '11':temp[4],
            '14':temp[5],
            '17':temp[6],
            '20':temp[7],
            '23':temp[8]
        }
        templist = []
        for classNum in range(1, 9):
            temp = str(self.soup.findAll('td', {'class':'p' + str(classNum)})[1])
            num = temp.find('title')
            inf = ''
            x = num+7
            i = temp[x]
            while i != '"':
                inf += i
                x += 1
                i = temp[x]
            templist.append(inf)
        information = {
            '2':templist[0],
            '5':templist[1],
            '8':templist[2],
            '11':templist[3],
            '14':templist[4],
            '17':templist[5],
            '20':templist[6],
            '23':templist[7]
        }
        result = [time, temperature, information]
        return result