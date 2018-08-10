# -*- coding:utf-8 -*-
import pymysql
import random
from config import mysql_config as sq
from sql_s import search_food,search_hotel,search_view


error = ['select','where','\'','in','from','#','--','-']
def get_things(lengs,lists,type):
    li = lengs/3
    listm = []
    if lengs >= 1:
        if type == 'low':
            for i in range(0, 3):
                try:
                    tt = lists[random.randint(li*2, lengs-1)]
                    if tt not in listm:
                        listm.append(tt)
                    else:
                        pass
                except:
                    pass
            return listm
        elif type == 'mid':
            for i in range(0, 3):
                try:
                    tt = lists[random.randint(li * 1, li*2)]
                    if tt not in listm:
                        listm.append(tt)
                    else:
                        pass
                except:
                    pass
            return listm
        elif type == 'high':
            for i in range(0,3):
                try:
                    tt = lists[random.randint(0, li * 1)]
                    if tt not in listm:
                        listm.append(tt)
                    else:
                        pass
                except:
                    pass
            return listm
    else:
        return None

def get_things2(lengs,lists):
    listm = []
    for i in range(0, 3):
        try:
            tt = lists[random.randint(0, lengs-1)]
            if tt not in listm:
                listm.append(tt)

        except:
            pass
    return listm

def select_database(destination,sex,type1,type2,type3,date):
    #链接数据库
    conn = pymysql.connect(host=sq.sql_host, port=sq.sql_port, user=sq.sql_user, \
                           passwd=sq.sql_passwd, db=sq.sql_db, charset='utf8')
    cursor = conn.cursor()
    #防止sql注入
    for i in error:
        if i in destination:
            return 0

    #初始化sql语句
    sql = search_food(destination)
    #sql = "select * from food where city like '%{0}%' or area like '%{0}%' ".format(destination)
    sql2 = search_view(destination)
    #sql2 = "select * from view where city like '%{0}%'or area like '%{0}%' ".format(destination)
    #sql3 = "select * from hotel where city like '%{0}%' or area like '%{0}%'".format(destination)
    sql3 = search_hotel(destination)
    #print(sql)
    #sql = "insert into {0}(name,area,address,detail,price,city) value('{1}','{2}','{3}','{4}','{5}','{6}');".format(table,name,area,address,detail,price,city)
    #print(sql)

    cursor.execute(sql.sql1)
    food = cursor.fetchall()
    leng = len(food)

    print(food)
    #print(leng)

    cursor.execute(sql2.sql1)
    view = cursor.fetchall()
    leng2 = len(view)
    #print(view)

    cursor.execute(sql3.sql1)
    hotel = cursor.fetchall()
    leng3 = len(hotel)
    #print(leng3)
#得到结果
    food = get_things(leng,food,type1)
    view = get_things2(leng2, view)
    hotel = get_things(leng3,hotel,type3)
    conn.close()

    if food == None and view == None and hotel == None:
        return -1,-1,-1

    return food,view,hotel
