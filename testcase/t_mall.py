import requests
from util.RequestsUtil import requests_get
from util.RequestsUtil import requests_post
from util.RequestsUtil import Request
from config.Conf import ConfigYaml

from common.Base import init_db

"""
post json
"""
def login():
    #url = "http://211.103.136.242:8064/authorizations/"
    url = ConfigYaml().get_conf_url() + "/authorizations/"
    data = {
        "username" : "python",
        "password" : "12345678"
    }
    r= Request().post(url,json = data)
    #return r['token']
    print(r)

"""
个人信息，token被拒绝了，无法登陆（已修改返回login方法的token信息）
get 
"""
def info():
    token = login()
    url = "http://211.103.136.242:8064/user/"
    #token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6Ijk1MjY3MzYzOEBxcS5jb20iLCJleHAiOjE2NDUzNDAzNjYsInVzZXJuYW1lIjoicHl0aG9uIiwidXNlcl9pZCI6MX0.KJp-oyK0-xA2guILuLgYQFA8FMX6eDdK3WpCbElD5yA"
    headers = {
        'Authorization' : 'JWT' + token
    }
    #print(token)
    r = requests.get(url, headers = headers)
    print(r.text)

"""
商品列表信息
get 
"""
def goods_list():
    url = "http://211.103.136.242:8064/categories/115/skus/"
    data = {
        "page" : "1",
        "page_size": "10",
        "ordering" : "create_time"
    }
    r= Request().get(url,json = data)
    print(r)



if __name__ == '__main__':
    login()
    #info()
    #goods_list()