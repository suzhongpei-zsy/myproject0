import unittest

from chapter3.city_weather import HeFeng
from chapter3.city_weather_db import HefengDb


class MyTestCase(unittest.TestCase):

    def test_save(self):
        hefengDb=HefengDb()
        hefengDb.save({"name": "suzhongpei", "class": "net19049"})
        hefengDb.show_all()
        results=hefengDb.find({"name":"suzhongpei"})
        for each in results:
            self.assertEqual("suzhongpei",each['name'])
            self.assertEqual("net19049",each['class'])
        hefengDb.delete()

    def test_save_all(self):
        hefeng=HeFeng()
        #codes=hefeng.get_city_code()
        #for each in codes:
        #    print(next（codes))
        each=(hefeng.get_weather("CN101010200"))
        print(each)
        hefengDb=HefengDb()
        hefengDb.save(each)

if __name__ == '__main__':
    unittest.main()
