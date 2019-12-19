import requests
import json

import pymysql.cursors

MYSQL_HOST = '127.0.0.1'
MYSQL_USER = "root"
MYSQL_PASSWORD = '123456'
MYSQL_DB = 'shi'
url1 = 'https://m2.qiushibaike.com/article/list/day?page='
url2 = '&count=12&readarticles=[121534300]'
for i in range(431,1000):
    info = requests.get(url1+str(i+1)+url2).text
    print(i+1)
    print(info)
    # res = json.loads(info)
    # print(res['items'])
    # for i in res['items']:
    #     print(i)

    connection = pymysql.connect(host=MYSQL_HOST,
                                 user=MYSQL_USER,
                                 password=MYSQL_PASSWORD,
                                 db=MYSQL_DB,
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)

    try:

        with connection.cursor() as cursor:
            sql = "insert into qushibaike_normal(page,info) values (%s,%s)"
            cursor.execute(sql,(str(i+1),info))
            connection.commit()
            # print(result)

    finally:
        connection.close()
