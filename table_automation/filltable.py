import os
from sql import *
from table_info import *
from automation import Automation
from table_info import *
from datetime import datetime


class FillTable(Automation):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        current_directory = os.path.abspath(os.getcwd())
        parent_directory = os.path.dirname(current_directory)
        self.excel_path = os.path.join(parent_directory, "media", "excels")

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
            
    def last_quarter_month(self, accum_type, sorted_data, date, i):
        if accum_type == "quarter":
            for quarter in reversed(quarters):
                last_month = [x for x in sorted_data if x[i-1] == (f"Январь - {quarter[1]} {date.year} г. (кв.)")]
                if len(last_month) > 2:
                    max_date = max(last_month, key=lambda x: x[i])[i]
                    accum_description =  f"Январь - {quarter[1]}"
                    break
                else:
                    max_date = datetime(1, 1, 1)
                    accum_description = ""
        elif accum_type == "month":
            for month in reversed(months):
                last_month = [x for x in sorted_data if x[i-1] == (f"Январь - {month[1]} {date.year} г. (мес.)")]
                if len(last_month) > 2:
                    max_date = max(last_month, key=lambda x: x[i])[i]
                    accum_description =  f"Январь - {month[1]}"
                    break
                else:
                    max_date = datetime(1, 1, 1)
                    accum_description = ""
        return max_date, accum_description
            
