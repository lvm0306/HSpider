import pymysql


class MysqlUtil():
    def __init__(self, host, user, psw, db):
        self.host = host
        self.user = user
        self.psw = psw
        self.db = db
        self.conn = None
        self.cursor = None

    def init(self):
        self.conn = pymysql.connect(host=self.host, user=self.user, password=self.psw,
                                    db=self.db, charset='utf8')
        self.cursor = self.conn.cursor()

    def executeSql(self,sql):
        self.cursor.execute(sql)
        self.conn.commit()

    def close(self):
        self.cursor.close()
        self.conn.close()
