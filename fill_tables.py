from datetime import datetime
import os
from openpyxl import Workbook
from taldau import Automation

class FillTable(Automation):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.excel_path = os.path.join(os.getcwd(), "bulletin", "macroeconomics", "static", "tables")


    def consumer_price_index_fill_table(self, start_month=None, start_year=None, end_month=None, end_year=None):
        excel_path = os.path.join(self.excel_path, "consumer_price_index.xlsx")
        workbook = Workbook()
        sheet = workbook.active

        if end_month is None or end_year is None:
            current_date = datetime.now()
            end_month = current_date.month
            end_year = current_date.year
        
        if start_month is None or start_year is None:
            current_date = datetime.now()
            start_month = 12
            start_year = current_date.year - 2


        months = [
            ["янв", 'Январь'], 
            ["фев", 'Февраль'], 
            ["мар", 'Март'], 
            ["апр", 'Апрель'], 
            ["май", 'Май'], 
            ["июн", 'Июнь'], 
            ["июл", 'Июль'], 
            ["авг", 'Август'], 
            ["сен", 'Сентябрь'], 
            ["окт", 'Октябрь'], 
            ["ноя", 'Ноябрь'], 
            ["дек", 'Декабрь']
        ]

        bull_name = [
            ["Потребительские цены", 'Товары и услуги'], 
            ["Продовольственные товары", 'Продовольственные товары'], 
            ["Непродовольственные товары", 'Непродовольственные товары'], 
            ["Платные услуги", 'Платные услуги'], 
            ["Цены производителей", 'Промышленность']
        ]


        # Создание мест списку для поиска
        condition = ",".join(["%s"] * len(bull_name))

        join_views = f"""
        SELECT 
            activity_type, 
            value, 
            description, 
            created_at
        FROM 
            consumer_price_index_month 
        WHERE 
            region = 'РЕСПУБЛИКА КАЗАХСТАН' 
            AND periods_correlation = 'отчетный период к соответствующему периоду прошлого года'  
            AND activity_type IN ({condition}) 
            AND created_at BETWEEN '{start_year}-{start_month}-01' AND '{end_year}-{end_month}-01'
        UNION
        SELECT 
            activity_type, 
            value, 
            description, 
            created_at
        FROM 
            producer_price_index_month 
        WHERE 
            region = 'РЕСПУБЛИКА КАЗАХСТАН' 
            AND periods_correlation = 'отчетный период к соответствующему периоду прошлого года' 
            AND countries = 'Всего'
            AND activity_type = 'Промышленность'
            AND industrial_products_list = 'Всего'
            AND created_at BETWEEN '{start_year}-{start_month}-01' AND '{end_year}-{end_month}-01'
        ORDER BY 
            created_at;
        """

        self.cur.execute(join_views, [item[1] for item in bull_name])
        sorted_data = self.cur.fetchall()

        # sorted_data = [('Продовольственные товары', Decimal('109.9'), 'Декабрь 2021 г.', date(2021, 12, 31)), ('Промышленность', Decimal('146.1'), 'Декабрь 2021 г.', date(2021, 12, 31)), ('Платные услуги', Decimal('106.5'), 'Декабрь 2021 г.', date(2021, 12, 31)), ('Непродовольственные товары', Decimal('108.5'), 'Декабрь 2021 г.', date(2021, 12, 31)), ('Товары и услуги', Decimal('108.4'), 'Декабрь 2021 г.', date(2021, 12, 31)), ('Продовольственные товары', Decimal('109.9'), 'Январь 2022 г.', date(2022, 1, 31)), ('Товары и услуги', Decimal('108.5'), 'Январь 2022 г.', date(2022, 1, 31)), ('Промышленность', Decimal('139.7'), 'Январь 2022 г.', date(2022, 1, 31)), ('Непродовольственные товары', Decimal('108.5'), 'Январь 2022 г.', date(2022, 1, 31)), ('Платные услуги', Decimal('106.8'), 'Январь 2022 г.', date(2022, 1, 31)), ('Промышленность', Decimal('139.1'), 'Февраль 2022 г.', date(2022, 2, 28)), ('Продовольственные товары', Decimal('110'), 'Февраль 2022 г.', date(2022, 2, 28)), ('Товары и услуги', Decimal('108.7'), 'Февраль 2022 г.', date(2022, 2, 28)), ('Непродовольственные товары', Decimal('108.6'), 'Февраль 2022 г.', date(2022, 2, 28)), ('Платные услуги', Decimal('107.1'), 'Февраль 2022 г.', date(2022, 2, 28)), ('Промышленность', Decimal('147.1'), 'Март 2022 г.', date(2022, 3, 31)), ('Платные услуги', Decimal('108.3'), 'Март 2022 г.', date(2022, 3, 31)), ('Непродовольственные товары', Decimal('110.9'), 'Март 2022 г.', date(2022, 3, 31)), ('Товары и услуги', Decimal('112'), 'Март 2022 г.', date(2022, 3, 31)), ('Продовольственные товары', Decimal('115.4'), 'Март 2022 г.', date(2022, 3, 31)), ('Товары и услуги', Decimal('113.2'), 'Апрель 2022 г.', date(2022, 4, 30)), ('Продовольственные товары', Decimal('117.9'), 'Апрель 2022 г.', date(2022, 4, 30)), ('Непродовольственные товары', Decimal('111.1'), 'Апрель 2022 г.', date(2022, 4, 30)), ('Платные услуги', Decimal('108.9'), 'Апрель 2022 г.', date(2022, 4, 30)), ('Промышленность', Decimal('141.3'), 'Апрель 2022 г.', date(2022, 4, 30)), ('Товары и услуги', Decimal('114'), 'Май 2022 г.', date(2022, 5, 31)), ('Промышленность', Decimal('129'), 'Май 2022 г.', date(2022, 5, 31)), ('Платные услуги', Decimal('109.1'), 'Май 2022 г.', date(2022, 5, 31)), ('Непродовольственные товары', Decimal('111.9'), 'Май 2022 г.', date(2022, 5, 31)), ('Продовольственные товары', Decimal('119'), 'Май 2022 г.', date(2022, 5, 31)), ('Промышленность', Decimal('128.2'), 'Июнь 2022 г.', date(2022, 6, 30)), ('Непродовольственные товары', Decimal('113.2'), 'Июнь 2022 г.', date(2022, 6, 30)), ('Продовольственные товары', Decimal('119.2'), 'Июнь 2022 г.', date(2022, 6, 30)), ('Платные услуги', Decimal('109.2'), 'Июнь 2022 г.', date(2022, 6, 30)), ('Товары и услуги', Decimal('114.5'), 'Июнь 2022 г.', date(2022, 6, 30)), ('Продовольственные товары', Decimal('119.7'), 'Июль 2022 г.', date(2022, 7, 31)), ('Промышленность', Decimal('130.1'), 'Июль 2022 г.', date(2022, 7, 31)), ('Товары и услуги', Decimal('115'), 'Июль 2022 г.', date(2022, 7, 31)), ('Непродовольственные товары', Decimal('114.2'), 'Июль 2022 г.', date(2022, 7, 31)), ('Платные услуги', Decimal('109.2'), 'Июль 2022 г.', date(2022, 7, 31)), ('Платные услуги', Decimal('110.1'), 'Август 2022 г.', date(2022, 8, 31)), ('Товары и услуги', Decimal('116.1'), 'Август 2022 г.', date(2022, 8, 31)), ('Промышленность', Decimal('125.3'), 'Август 2022 г.', date(2022, 8, 31)), ('Непродовольственные товары', Decimal('115.5'), 'Август 2022 г.', date(2022, 8, 31)), ('Продовольственные товары', Decimal('120.8'), 'Август 2022 г.', date(2022, 8, 31)), ('Промышленность', Decimal('121.8'), 'Сентябрь 2022 г.', date(2022, 9, 30)), ('Товары и услуги', Decimal('117.7'), 'Сентябрь 2022 г.', date(2022, 9, 30)), ('Непродовольственные товары', Decimal('117'), 'Сентябрь 2022 г.', date(2022, 9, 30)), ('Платные услуги', Decimal('112.3'), 'Сентябрь 2022 г.', date(2022, 9, 30)), ('Продовольственные товары', Decimal('122.2'), 'Сентябрь 2022 г.', date(2022, 9, 30)), ('Товары и услуги', Decimal('118.8'), 'Октябрь 2022 г.', date(2022, 10, 31)), ('Непродовольственные товары', Decimal('117.9'), 'Октябрь 2022 г.', date(2022, 10, 31)), ('Промышленность', Decimal('117'), 'Октябрь 2022 г.', date(2022, 10, 31)), ('Продовольственные товары', Decimal('123.1'), 'Октябрь 2022 г.', date(2022, 10, 31)), ('Платные услуги', Decimal('113.5'), 'Октябрь 2022 г.', date(2022, 10, 31)), ('Товары и услуги', Decimal('119.6'), 'Ноябрь 2022 г.', date(2022, 11, 30)), ('Платные услуги', Decimal('114.1'), 'Ноябрь 2022 г.', date(2022, 11, 30)), ('Промышленность', Decimal('110'), 'Ноябрь 2022 г.', date(2022, 11, 30)), ('Продовольственные товары', Decimal('124.1'), 'Ноябрь 2022 г.', date(2022, 11, 30)), ('Непродовольственные товары', Decimal('118.6'), 'Ноябрь 2022 г.', date(2022, 11, 30)), ('Непродовольственные товары', Decimal('119.4'), 'Декабрь 2022 г.', date(2022, 12, 31)), ('Платные услуги', Decimal('114.1'), 'Декабрь 2022 г.', date(2022, 12, 31)), ('Промышленность', Decimal('109.4'), 'Декабрь 2022 г.', date(2022, 12, 31)), ('Товары и услуги', Decimal('120.3'), 'Декабрь 2022 г.', date(2022, 12, 31)), ('Продовольственные товары', Decimal('125.3'), 'Декабрь 2022 г.', date(2022, 12, 31)), ('Продовольственные товары', Decimal('125.7'), 'Январь 2023 г.', date(2023, 1, 31)), ('Товары и услуги', Decimal('120.7'), 'Январь 2023 г.', date(2023, 1, 31)), ('Непродовольственные товары', Decimal('120.2'), 'Январь 2023 г.', date(2023, 1, 31)), ('Платные услуги', Decimal('114.2'), 'Январь 2023 г.', date(2023, 1, 31)), ('Промышленность', Decimal('107.1'), 'Январь 2023 г.', date(2023, 1, 31)), ('Продовольственные товары', Decimal('126.2'), 'Февраль 2023 г.', date(2023, 2, 28)), ('Платные услуги', Decimal('115'), 'Февраль 2023 г.', date(2023, 2, 28)), ('Промышленность', Decimal('104.5'), 'Февраль 2023 г.', date(2023, 2, 28)), ('Товары и услуги', Decimal('121.3'), 'Февраль 2023 г.', date(2023, 2, 28)), ('Непродовольственные товары', Decimal('120.5'), 'Февраль 2023 г.', date(2023, 2, 28)), ('Непродовольственные товары', Decimal('118.1'), 'Март 2023 г.', date(2023, 3, 31)), ('Товары и услуги', Decimal('118.1'), 'Март 2023 г.', date(2023, 3, 31)), ('Продовольственные товары', Decimal('120.5'), 'Март 2023 г.', date(2023, 3, 31)), ('Платные услуги', Decimal('114.4'), 'Март 2023 г.', date(2023, 3, 31)), ('Промышленность', Decimal('92.4'), 'Март 2023 г.', date(2023, 3, 31)), ('Платные услуги', Decimal('113.7'), 'Апрель 2023 г.', date(2023, 4, 30)), ('Продовольственные товары', Decimal('117.9'), 'Апрель 2023 г.', date(2023, 4, 30)), ('Промышленность', Decimal('90.6'), 'Апрель 2023 г.', date(2023, 4, 30)), ('Товары и услуги', Decimal('116.8'), 'Апрель 2023 г.', date(2023, 4, 30)), ('Непродовольственные товары', Decimal('118.2'), 'Апрель 2023 г.', date(2023, 4, 30)), ('Продовольственные товары', Decimal('116.5'), 'Май 2023 г.', date(2023, 5, 31)), ('Товары и услуги', Decimal('115.9'), 'Май 2023 г.', date(2023, 5, 31)), ('Непродовольственные товары', Decimal('117.2'), 'Май 2023 г.', date(2023, 5, 31)), ('Платные услуги', Decimal('113.5'), 'Май 2023 г.', date(2023, 5, 31)), ('Промышленность', Decimal('96.7'), 'Май 2023 г.', date(2023, 5, 31)), ('Промышленность', Decimal('93.5'), 'Июнь 2023 г.', date(2023, 6, 30)), ('Продовольственные товары', Decimal('114.6'), 'Июнь 2023 г.', date(2023, 6, 30)), ('Платные услуги', Decimal('113.3'), 'Июнь 2023 г.', date(2023, 6, 30)), ('Товары и услуги', Decimal('114.6'), 'Июнь 2023 г.', date(2023, 6, 30)), ('Непродовольственные товары', Decimal('115.8'), 'Июнь 2023 г.', date(2023, 6, 30)), ('Платные услуги', Decimal('113.6'), 'Июль 2023 г.', date(2023, 7, 31)), ('Продовольственные товары', Decimal('113.5'), 'Июль 2023 г.', date(2023, 7, 31)), ('Товары и услуги', Decimal('114'), 'Июль 2023 г.', date(2023, 7, 31)), ('Промышленность', Decimal('88.8'), 'Июль 2023 г.', date(2023, 7, 31)), ('Непродовольственные товары', Decimal('115'), 'Июль 2023 г.', date(2023, 7, 31)), ('Промышленность', Decimal('92.3'), 'Август 2023 г.', date(2023, 8, 31)), ('Платные услуги', Decimal('113.9'), 'Август 2023 г.', date(2023, 8, 31)), ('Товары и услуги', Decimal('113.1'), 'Август 2023 г.', date(2023, 8, 31)), ('Продовольственные товары', Decimal('112.4'), 'Август 2023 г.', date(2023, 8, 31)), ('Непродовольственные товары', Decimal('113.5'), 'Август 2023 г.', date(2023, 8, 31))]
        # print(sorted_data)

        dates = [item[3] for item in sorted_data]
        latest_month = max(dates).month
        latest_year = max(dates).year

        if latest_month < end_month:
            end_month = latest_month
        if latest_year < end_year:
            end_year = latest_year

        
        months_list = [""]

        data_for_excel = []
        for bull_name_i, economic_index in enumerate(bull_name):
            index_data = []
            index_data.append(economic_index[0])
            for year in range(start_year, end_year+1):
                for i, m in enumerate(months, start=1):
                    if year == start_year and i < start_month: continue
                    if year == end_year and i > end_month: continue
                    # получешние месяцев для заголовка
                    if bull_name_i == 0:
                        months_list.append(m[0])
                    
                    data_not_exist = True
                    for data in sorted_data:
                        t_month, t_year, _ = data[2].split()
                        t_year = int(t_year)
                        if economic_index[1] == data[0] and t_month == m[1] and t_year == year:
                            index_data.append(float(data[1]))
                            data_not_exist = False
                    if data_not_exist:
                        index_data.append("")
            data_for_excel.append(index_data)

        # заголовок 
        year_list = list(range(start_year, end_year + 1))
        start_cell = 2
        end_cell = 12-start_month+start_cell
        sheet.cell(row=1, column=1, value="Показатели")
        for i, year in enumerate(year_list):
            sheet.cell(row=1, column=start_cell, value=year)
            sheet.merge_cells(start_row=1, start_column=start_cell, end_row=1, end_column=end_cell)
            start_cell = end_cell+1
            if i+2 == len(year_list):
                end_cell += end_month
            else:
                end_cell += 12



        sheet.append(months_list)
        for data in data_for_excel:
            sheet.append(data)
        
        workbook.save(excel_path)


fillTable = FillTable("testtest", "postgres", "123456")

fillTable.consumer_price_index_fill_table()
fillTable.db_disconnect()