from filltable import FillTable
from datetime import datetime, timedelta
import os
from openpyxl import Workbook


class CreatePPITable(FillTable):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


    def get_data_create_ppi_table(self, sql, names, accum_type, minus_num):
        current_date = datetime.now()
        start_year = current_date.year - minus_num
        end_year = start_year + 3

        date_start_year = datetime(start_year, 1, 1)
        date_end_year = datetime(start_year + 4, 1, 1) - timedelta(seconds=1)
        date_start_quarter = datetime(start_year + 4, 1, 1)
        date_end_quarter = datetime(start_year + 5, 1, 1) - timedelta(seconds=1)


        self.cur.execute(
            sql, (
                date_start_year, date_end_year,
                tuple([item[1] for item in names[1:5]]),
                date_start_year, date_end_year,
                date_start_year, date_end_year,
                date_start_year, date_end_year,
                date_start_year, date_end_year,
                date_start_year, date_end_year,
                date_start_year, date_end_quarter,
                date_start_year, date_end_quarter,
                tuple([item[1] for item in names[5:]]),
                date_start_year, date_end_year,
                date_start_year, date_end_quarter,
                date_start_year, date_end_quarter,
                date_start_quarter, date_end_quarter,
                tuple([item[1] for item in names[1:5]]),
                date_start_quarter, date_end_quarter,
                date_start_quarter, date_end_quarter,
                date_start_quarter, date_end_quarter,
                tuple([item[1] for item in names[5:]]),
                date_start_quarter, date_end_quarter,
            )
        )
        sorted_data = self.cur.fetchall()


        max_date, accum_description = self.last_quarter_month(accum_type, sorted_data, date_start_quarter, 3)
        return sorted_data, end_year, start_year, max_date, accum_description

    def create_ppi_table(self, names, accum_type, sql, table_name, index_name):
        excel_path = os.path.join(self.excel_path, table_name)
        workbook = Workbook()
        sheet = workbook.active

        sorted_data, end_year, start_year, max_date, accum_description = self.get_data_create_ppi_table(sql, names, accum_type, 4)
        if max_date.year != end_year+1:
            sorted_data, end_year, start_year, max_date, accum_description = self.get_data_create_ppi_table(sql, names, accum_type, 5)


        data_for_excel = []
        for name in names:
            index_data = []
            index_data.append(name[0])
            data_not_exist = True

            for year in range(start_year, end_year+1):
                data_not_exist = True
                for data in sorted_data:
                    if data[0] == name[1] and (data[2] == f"{year} год" or data[2] == f"Январь - Декабрь {year} г. (мес.)" or data[2] == f"на 1 ноября {year} г."):
                        value = round(float(data[1]),1)
                        index_data.append(value)
                        data_not_exist = False
                if data_not_exist:
                    index_data.append("")

            data_not_exist = True
            for data in sorted_data:
                if data[0] == name[1] and (data[2] == f"{accum_description} {end_year+1} г. (кв.)" or data[2] == f"{accum_description} {end_year+1} г. (мес.)"):
                    value = round(float(data[1]),1)
                    index_data.append(value)
                    data_not_exist = False
            if data_not_exist:
                index_data.append("")
            
            data_for_excel.append(index_data)

        header1 = ["Показатели"]
        empty_row = []
        #заголовок
        end_year_header = end_year+2

        for year in range(start_year, end_year_header):
            if year == end_year+1:
                header1.append(str(year) + f"\n {accum_description}")
            else:
                header1.append(year)


        sheet.append(header1)
        sheet.append(empty_row)
        for data in data_for_excel:
            sheet.append(data)
                
        workbook.save(excel_path)
        workbook.close()

        print(f"Таблица {index_name} создана")