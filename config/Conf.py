import os
from util.YamlUtil import YamlReader

#1、获取项目基本目录
#获取当前项目的绝对路径
current = os.path.abspath(__file__)
BASE_DIR = os.path.dirname(os.path.dirname(current))
#print(BASE_DIR)
#定义config文件夹路径
_config_path = BASE_DIR + os.sep + "config"
#定义data文件夹路径
_data_path = BASE_DIR + os.sep + "data"
#定义data下excel的相关用例数据文件路径
_data_excel_file = _data_path + os.sep + "testdata.xlsx"
#定义conf.yml文件路径
_conf_yml_file = _config_path + os.sep + "conf.yml"
#定义db_conf.yml文件路径
_db_conf_yml_file = _config_path + os.sep + "db_conf.yml"
#print(_conf_yml_file)
#定义log文件夹路径
_log_path = BASE_DIR + os.sep + "logs"

def get_config_path():
    return _config_path
def get_data_path():
    return _data_path
def get_data_excel_file():
    return _data_excel_file
def get_conf_yml_file():
    return _conf_yml_file
def get_db_conf_yml_file():
    return _db_conf_yml_file
def get_log_path():
    return _log_path
#2、读取配置文件
#创建类
class ConfigYaml:
#初始化yaml，读取配置文件
    def __init__(self):
        self.config = YamlReader(get_conf_yml_file()).data()
        self.db_config = YamlReader(get_db_conf_yml_file()).data_all()
#获取excel测试用例文件
    def get_excel_file(self):
        return self.config['BASE']['test']['case_file']
#获取excel测试用例数据
    def get_excel_sheet(self):
        return self.config['BASE']['test']['case_sheet']
#定义方法获取需要的信息(url)
    def get_conf_url(self):
        return self.config['BASE']['test']['url']
#定义方法获取需要的信息(log_level)
    def get_conf_log_level(self):
        return self.config['BASE']['log_level']
#定义方法获取需要的信息(log_extension)
    def get_conf_log_extension(self):
        return self.config['BASE']['log_extension']
#定义方法获取需要的信息(db连接信息)
    def get_db_conf_info(self,db_alias):
        return self.db_config[0][db_alias]

if __name__ == '__main__':
    #print(ConfigYaml().config)
    print(ConfigYaml().db_config)
    #print(ConfigYaml().get_conf_url())
    #print(conf_read.get_conf_log_level())
    #print(conf_read.get_conf_log_extension())
    print(ConfigYaml().get_db_conf_info("db_1"))
    print(ConfigYaml().get_db_conf_info("db_2"))

