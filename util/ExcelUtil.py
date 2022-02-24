import os
import xlrd2

class ExcelReader:
    def __init__(self,excel_file,sheet_by):
        if os.path.exists(excel_file):
            self.excel_file = excel_file
            self.sheet_by = sheet_by
            self.data_list = []
        else:
            raise FileNotFoundError("文件不存在")

    def excel_data(self):
        if not self.data_list:
            workbook = xlrd2.open_workbook(self.excel_file)
            if type(self.excel_file) not in [int,str]:
                raise ("excel文件类型不正确")
            elif type(self.sheet_by) == int:
                sheet = workbook.sheet_by_index(self.sheet_by)
            elif type(self.sheet_by) == str:
                sheet = workbook.sheet_by_name(self.sheet_by)

            #首行
            title = sheet.row_values(0)

            for row in range(1,sheet.nrows):
                self.data_list.append(dict(zip(title,sheet.row_values(row))))
                #print(sheet.row_values(row))
        return self.data_list


if __name__ == '__main__':
    res = ExcelReader("../data/testdata.xlsx",0).excel_data()
    print(res)


