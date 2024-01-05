import os
from sql import *
from table_info import *
from automation import Automation


class FillTable(Automation):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        current_directory = os.path.abspath(os.getcwd())
        parent_directory = os.path.dirname(current_directory)
        self.excel_path = os.path.join(parent_directory, "bulletin", "media", "excels")

    def romam_to_arabic(self, num):
        if num == 1:
            return "I"
        elif num == 2:
            return "II"
        elif num == 3:
            return "III"
        elif num == 4:
            return "IV"

    def convert_number(self, data_type, num):
        if data_type == "tenge" or data_type == "thousand_tenge":
            return float(round(num/1000, 1))
        elif data_type == "percent":
            return float(round(num, 1))
        elif data_type == "million_tenge":
            rev_num = str(round(int(num/1000000)))[::-1]
            return ' '.join([rev_num[i:i+3] for i in range(0, len(rev_num), 3)])[::-1]
        elif data_type == "thousand_tenge_exp":
            if num < 100:
                return float(num)
            else:
                return float(round(num/1000, 1))
