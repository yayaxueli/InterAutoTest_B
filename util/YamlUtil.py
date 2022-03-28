import os

import yaml


class YamlReader:
    def __init__(self,yaml_file):
        if os.path.exists(yaml_file):
            self.yaml_file = yaml_file
            self.yaml_data = None
            self.yaml_data_all = None
        else:
            raise FileNotFoundError("文件不存在")

    #单个文档读取
    def data(self):
        #第一次调用data，读取yaml文件，如果不是，直接返回之前保存的数据
        #if not self.yaml_data:
        with open(self.yaml_file,'r',encoding = 'utf8') as f:
            self.yaml_data = yaml.safe_load(f)
        return self.yaml_data

    #多个文档读取
    def data_all(self):
        #第一次调用data，读取yaml文件，如果不是，直接返回之前保存的数据
        #if not self.yaml_data_all:
        with open(self.yaml_file,'r',encoding = 'utf8') as f:
            self.yaml_data_all = list(yaml.safe_load_all(f))
        return self.yaml_data_all










