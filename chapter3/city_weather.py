import time

import requests




class HeFeng():
    def __init__(self):
        self.url = "https://cdn.heweather.com/china-city-list.txt"
        self.encoding="utf8"
        self.pre_requests="https://free-api.heweather.net/s6/weather/now?location="
        self.sub_requests="&key=7e71657d03174bbe9f00cb25bc873327"

    def today_weather(self,city_code):
        dict=self.get_weather(city_code)
        print(dict["HeWeather6"][0]['now'])

    def get_all_weather(self,count_of_citys):
        codes=self.get_city_code()
        weathers=[]
        i=0
        while i<count_of_citys:
            each=self.get_weather(next(codes))
            print(each)
            weathers.append(each)
            i=i+1
        return weathers

    def get_weather(self,city_code):
        time.sleep(1)
        url=self.pre_requests+city_code+self.sub_requests
        info=requests.get(url)
        info.encoding=self.encoding
        return info.json()
        #print(info.text)

    def get_city_code(self):
        cities = self.get_citys()
        for each in cities:
            yield each[2:13]

    def get_citys(self):
        html = requests.get(self.url)
        html.encoding = self.encoding
        cities = html.text.split('\n')
        return cities[6:]

if __name__ == '__main__':
    hefeng = HeFeng()
    codes=hefeng.get_city_code()
    for i in range(10):
        dict=hefeng.get_weather(codes.__next__())
        #print(dict["HeWeather6"][0]['now'])
        hefeng.today_weather(codes.__next__())