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
        weathers=hefeng.get_all_weather(7)
        hefengDb=HefengDb()
        hefengDb.save_all(weathers)
        print("show_all")
        hefengDb.show_all()
        self.assertEqual(7,hefengDb.count())
        hefengDb.delete()


if __name__ == '__main__':
    unittest.main()
