import os
from openpyxl import Workbook
from datetime import datetime, timedelta
from table_info import *
from filltable import FillTable


class CreateLaborStatsTable(FillTable):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def period_counter(self, data, period_name):
        for row in data:
            if period_name == "quarter":
                desc_parts = row[2].split()
                period = desc_parts[0] + " " + desc_parts[1]
                for key in quarter_list:
                    if period == key:
                        quarter_list[key] += 1
            elif period_name == "month_accum":
                desc_parts = row[2].split()
                period = desc_parts[0] + " " + desc_parts[1] + " " + desc_parts[2]
                for key in month_accum_list:
                    if period == key:
                        month_accum_list[key] += 1
        if period_name == "quarter":
            if quarter_list["1 квартал"] == 0:
                return 0
            period_parts = max(quarter_list, key=quarter_list.get).split()
            return period_parts[0]
        elif period_name == "month_accum":
            if month_accum_list["Январь - Январь"] == 0 and month_accum_list["Январь - Март"] == 0:
                return 0
            return max(month_accum_list, key=month_accum_list.get)

    def create_labor_stats_table(self, names, sql, table_name, index_name, start_year=None):
        excel_path = os.path.join(self.excel_path, table_name)

        if start_year is None:
            current_date = datetime.now()
            start_year = current_date.year - 4
        workbook = Workbook()
        sheet = workbook.active
        end_year = start_year + 3

        date_start_year = datetime(start_year, 1, 1)
        date_end_year = datetime(start_year + 4, 1, 1) - timedelta(days=1)
        date_start_quarter = datetime(start_year + 4, 1, 1)
        date_end_quarter = datetime.now()

        condition_values = []
        for name in names[2:21]:
            condition_values.append(name[1])

        self.cur.execute(
            sql, (
                date_start_year, date_end_year,
                date_start_year, date_end_year,
                tuple(condition_values),
                date_start_year, date_end_year,
                date_start_year, date_end_year,
                date_start_year, date_end_year,
                date_start_year, date_end_year,
                date_start_year, date_end_year,
                date_start_year, date_end_year,
                date_start_quarter, date_end_quarter,
                date_start_quarter, date_end_quarter,
                tuple(condition_values),
                date_start_quarter, date_end_quarter,
                date_start_quarter, date_end_quarter,
                date_start_quarter, date_end_quarter,
                date_start_quarter, date_end_quarter,
                date_start_quarter, date_end_quarter,                
            )
        )

        sorted_data = self.cur.fetchall()

        last_year_data = []
        for data in sorted_data:
            if len(data[2].split()) > 2:
                last_year_data.append(data)

        quarter = self.period_counter(last_year_data, "quarter")
        # quarter = 1

        data_for_excel = []
        for name in names:
            index_data = []
            index_data.append(name[0])
            data_not_exist = True

            for year in range(start_year, end_year+1):
                data_not_exist = True
                for data in sorted_data:
                    if data[2] == f"{year} год" and data[0] == name[1]:
                        if data[1] < 100:
                            index_data.append(float(data[1]))
                        else:
                            index_data.append(float(round(data[1]/1000, 1)))
                        data_not_exist = False
                if data_not_exist:
                    index_data.append("")

            if quarter != 0:
                data_not_exist = True
                for data in sorted_data:
                    if data[2] == f"{quarter} квартал {end_year+1} г." and data[0] == name[1]:
                        if data[1] < 100:
                            index_data.append(float(data[1]))
                        else:
                            index_data.append(float(round(data[1]/1000, 1)))
                        data_not_exist = False
                if data_not_exist:
                    index_data.append("")

            data_for_excel.append(index_data)

        #заголовок
        if quarter == 0:
            end_year_header = end_year+1
        else:
            end_year_header = end_year+2
        header1 = ["Показатели"]
        for year in range(start_year, end_year_header):
            if year == end_year+1:
                header1.append(str(year) + f"\n{quarter} кв.")
            else:
                header1.append(year)


        sheet.append(header1)
        for data in data_for_excel:
            sheet.append(data)

        workbook.save(excel_path)
        workbook.close()

        print(f"Таблица {index_name} создана")