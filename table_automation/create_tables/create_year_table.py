from filltable import FillTable
from datetime import datetime, timedelta
import os
from openpyxl import Workbook


class CreateYearTable(FillTable):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


    def get_data_create_year_table(self, sql, names, minus_num):
        current_date = datetime.now()
        start_year = current_date.year - minus_num
        end_year = start_year + 3

        date_start_year = datetime(start_year, 1, 1)
        date_end_year = datetime(start_year + 4, 1, 1) - timedelta(seconds=1)
        date_start_quarter = datetime(start_year + 4, 1, 1)
        date_end_quarter = datetime(start_year + 5, 1, 1) - timedelta(seconds=1)


        self.cur.execute(
            sql, (
                tuple([item[1] for item in names]),
                date_start_year, date_end_year,
                tuple([item[1] for item in names]),
                date_start_quarter, date_end_quarter,
            )
        )
        sorted_data = self.cur.fetchall()


        max_date = max(sorted_data, key=lambda x: x[3])[3]
        return sorted_data, end_year, start_year, max_date

    def create_year_table(self, names, sql, table_name, data_type, index_name):
        excel_path = os.path.join(self.excel_path, table_name)
        workbook = Workbook()
        sheet = workbook.active

        sorted_data, end_year, start_year, max_date = self.get_data_create_year_table(sql, names, 4)
        if max_date.year != end_year+1:
            sorted_data, end_year, start_year, max_date = self.get_data_create_year_table(sql, names, 5)

        for data in sorted_data:
            if data[3] == max_date:
                accum_quarter = data[2]
                break

        data_for_excel = []
        for name in names:
            index_data = []
            index_data.append(name[0])
            data_not_exist = True

            for year in range(start_year, end_year+1):
                data_not_exist = True
                for data in sorted_data:
                    if data[2] == f"{year} год" and data[0] == name[1]:
                        value = self.convert_number(data_type, data[1])
                        index_data.append(value)
                        data_not_exist = False
                if data_not_exist:
                    index_data.append("")

            data_not_exist = True
            for data in sorted_data:
                if data[2] == accum_quarter and data[0] == name[1]:
                    value = self.convert_number(data_type, data[1])
                    index_data.append(value)
                    data_not_exist = False
            if data_not_exist:
                index_data.append("")
            
            data_for_excel.append(index_data)

        if data_type == "thousand_tenge":
            header1 = ["Регионы (тыс. тенге)"]
        elif data_type == "million_tenge":
            header1 = ["Регионы (млн тенге)"]

        #заголовок
        end_year_header = end_year+2
        words = accum_quarter.split()
        if len(words) >= 3:
            acc_quarter_months = ' '.join(words[:3])
        for year in range(start_year, end_year_header):
            if year == end_year+1:
                header1.append(str(year) + f"\n {acc_quarter_months}")
            else:
                header1.append(year)


        sheet.append(header1)
        for data in data_for_excel:
            sheet.append(data)
                
        workbook.save(excel_path)
        workbook.close()

        print(f"Таблица {index_name} создана")