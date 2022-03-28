import pymysql
#from util.LogUtil import my_log
class Mysql:
    def __init__(self,host,user,password,database,charset = "utf8",port = 3306):
        #self.log = my_log()
        #初始化数据库连接信息
        self.conn = pymysql.connect(
            host = host,
            user = user,
            password = password,
            database = database,
            charset = charset,
            port = port
        )
        # 获取执行sql的光标对象,参数需要注意
        self.cursor = self.conn.cursor(cursor = pymysql.cursors.DictCursor)

    # 单个查询
    def fetchone(self, sql):
        self.cursor.execute(sql)
        return self.cursor.fetchone()
    #多个查询
    def fetchall(self, sql):
        self.cursor.execute(sql)
        return self.cursor.fetchall()
    #执行sql
    def exec(self, sql):
        try:
            if self.conn and self.cursor:
                self.cursor.execute(sql)
        except Exception as ex:
            self.conn.rollback()
            #self.log.error("Mysql 执行失败")
            #self.log.error(ex)
            return False
        return True

    #关闭对象
    def __del__(self):
        if self.cursor is not None:
            self.cursor.close()
        if self.conn is not None:
            self.conn.close()

if __name__ == '__main__':
    mysql = Mysql("211.103.136.242","test","test123456","meiduo",charset = "utf8",port = 7090)
    res = mysql.fetchall("select * from tb_users")
    print(res)




