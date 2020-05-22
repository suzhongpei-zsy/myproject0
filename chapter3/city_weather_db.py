import pymongo


class HefengDb():
    def __init__(self):
        self.client = pymongo.MongoClient('localhost', 27017)
        self.book_weather =self.client['weather']
        self.sheet_weather = self.book_weather['sheet_Weather_3']

    def save(self,data):
        self.sheet_weather.insert_one(data)

    def show_all(self):
        all=self.sheet_weather.find()
        for each in all:
            print(each)

    def find(self,condition):
        return self.sheet_weather.find(condition)

    def delete(self):
        self.sheet_weather.delete_many({})

    def save_all(self，weathers):
         for each in weathers:
            self.save(each)


     def count(self):
        all = self.sheet_weather.find()
        nums=0
        for each in all:
            nums=nums+1

        for each in all:
            print(each)




if __name__=="__main__":
    #client=pymongo.MongoClient('localhost',27017)
    #book_weather=client['weather']
    #sheet_weather=book_weather['sheet_Weather_3']
    #print(sheet_weather)
    #sheet_weather.insert_one({"name":"suzhongpei","class":"net19049"})
    hefengDb=HefengDb()
    hefengDb.save({"name":"suzhongpei","class":"net19049"})
    hefengDb.show_all()