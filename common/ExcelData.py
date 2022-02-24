from util.ExcelUtil import ExcelReader
from common.ExcelConfig import ExcelConfig
class Data:
    def __init__(self,file,sheet_name):
        self.reader = ExcelReader(file,sheet_name)

    #根据列是否允许 = Y，来执行测试用例
    def get_run_data(self):
        run_list = []
        for line in self.reader.excel_data():
            if str(line[ExcelConfig().is_run]).lower() == 'y':
                run_list.append(line)
        return run_list

