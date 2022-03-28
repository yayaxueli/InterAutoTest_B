from config.Conf import ConfigYaml
from util.MysqlUtil import Mysql
def init_db(db_alias):
    db_info = ConfigYaml().get_db_conf_info(db_alias)
    host = db_info['db_host']
    user = db_info['db_user']
    password = db_info['db_password']
    database = db_info['db_database']
    charset = db_info['db_charset']
    port = int(db_info['db_port'])
    conn = Mysql(host,user,password,database,charset,port)
    #res = conn.fetchall("select * from tb_users")
    #print(conn)
    return conn

if __name__ == '__main__':
    print(init_db("db_1"))