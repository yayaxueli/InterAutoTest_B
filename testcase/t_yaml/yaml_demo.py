import yaml
from util.YamlUtil import YamlReader
# with open('./data.yml','r',encoding = 'utf8') as f:
#     r = yaml.safe_load(f)
#     print(r)
#res1 = YamlReader('./data.yml').data()
res2 = YamlReader('./data.yml').data_all()
print(res2)


