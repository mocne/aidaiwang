# !/usr/bin/python3

import pymysql

def insert2sql(database, table, values):

    global cmd_insert, cmd_intoDatabase
    if database is 'mocne':
        cmd_intoDatabase = 'use %s' % database
        if database is 'mocne' and table is 'BD_img':
            cmd_insert = 'insert into ' + table + '(img_name, img_url, img_content, img_date) VALUES(' + values['name'] + ', ' + values['content'] + '' + ', ' + ');'

    # 打开数据库连接
    db = pymysql.connect("localhost", "tester", "a1111111", "mocne")

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()

    # 使用 execute()  方法执行 SQL 查询
    cursor.execute(cmd_intoDatabase)
    cursor.execute(cmd_insert)

    # 使用 fetchone() 方法获取单条数据.
    data = cursor.fetchone()

    print("tables : %s " % data)

    # 关闭数据库连接
    db.close()