from chapter3.city_weather import HeFeng
from chapter3.city_weather_db import HefengDb


if __name__ ==  '__main__':
    hefeng = HeFeng()
    weathers = hefeng.get_all_weather(250)
    hefengDb = HefengDb()
    hefengDb.save_all(weathers)
    hefengDb.show_all()


if __name__ == '__main__':
    # save_all_weather()
    hefengDb=HefengDb()
    #hefengDb.show_all()
    for each in hefengDb.find({'HeWeather6.basic.parent_city':'北京'}):
        print(each)
    print('========================晴天=========================')
    for each in hefengDb.find({'HeWeather6.now.cond_txt':'晴'}):
        print(each['HeWeather6'][0]['basic']['location'])
    print('=============温度大于26===================')
    for each in hefengDb.find({'HeWeather6.now.tmp': {'$gte':'26'}}):
        print(each)




