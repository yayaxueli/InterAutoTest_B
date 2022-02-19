import requests


def requests_get(url,**kwargs):
    r= requests.get(url,**kwargs)
    code = r.status_code
    #print(code)
    try:
        body = r.json()
    except Exception as e:
        body = r.text
    res = {}
    res['code'] = code
    res['body'] = body
    return res

def requests_post(url,**kwargs):
    r= requests.post(url,**kwargs)
    code = r.status_code
    #print(code)
    try:
        body = r.json()
    except Exception as e:
        body = r.text
    res = {}
    res['code'] = code
    res['body'] = body
    return res

#重构封装Requests方法
class Request:
    def requests_api(self,url,method = "get",**kwargs):
        if method == "get":
            r = requests.get(url,**kwargs)
        elif method == "post":
            r = requests.post(url,**kwargs)
        code = r.status_code
        try:
            body = r.json()
        except Exception as e:
            body = r.text
        res = {}
        res['code'] = code
        res['body'] = body
        return res

    def get(self,url,**kwargs):
        return self.requests_api(url,method = "get",**kwargs)
    def post(self,url,**kwargs):
        return self.requests_api(url,method = "post",**kwargs)



if __name__ == '__main__':
    data = {
        "page" : "1",
        "page_size": "10",
        "ordering" : "create_time"
    }
    r = requests_get("http://211.103.136.242:8064/categories/115/skus/",headers = None,json = data)
    print(r)







