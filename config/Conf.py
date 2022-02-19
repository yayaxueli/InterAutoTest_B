#获取项目地址
import os.path
from util.YamlUtil import YamlReader
current = os.path.abspath(__file__)
BASE_DIR = os.path.dirname(os.path.dirname(current))
_config_path = BASE_DIR + os.sep + 'config'
_config_yaml_file = _config_path + os.sep + 'conf.yml'
#print(_config_yaml_file)
def get_config_path():
    return _config_path
def get_config_yaml_file():
    return _config_yaml_file

class ConfigYaml:
    def __init__(self):
        self.config = YamlReader(get_config_yaml_file()).data()

    def get_conf_url(self):
        return self.config['url']

if __name__ == '__main__':
    conf_yaml = ConfigYaml().get_conf_url()
    print(conf_yaml)


