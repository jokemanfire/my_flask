# -*- coding:utf-8 -*-

#直接按价格排序语句

#search food
class search_food():
    def __init__(self,destination):
        self.destination = destination
        #按降序
        self.sql1 = "select * from food where price != -1 and (city like '%{0}%' or area like '%{0}%') order by price  desc".format(self.destination)
        #按升序
        self.sql2 = "select * from food where price != -1 and (city like '%{0}%' or area like '%{0}%') order by price  asc".format(self.destination)


#search view
class search_view():
    def __init__(self,destination):
        self.destination = destination
        #按降序
        self.sql1 = "select * from view where (city like '%{0}%' or area like '%{0}%') order by price  desc".format(self.destination)
        #按升序
        self.sql2 = "select * from view where (city like '%{0}%' or area like '%{0}%') order by price  asc".format(self.destination)

#search hotel
class search_hotel():
    def __init__(self,destination):
        self.destination = destination
        #按降序
        self.sql1 = "select * from hotel where price != -1 and (city like '%{0}%' or area like '%{0}%') order by price  desc".format(self.destination)
        #按升序
        self.sql2 = "select * from hotel where price != -1 and (city like '%{0}%' or area like '%{0}%') order by price  asc".format(self.destination)
