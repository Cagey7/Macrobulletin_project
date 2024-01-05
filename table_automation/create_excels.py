from filltable import FillTable
from create_tables.create_year_table import CreateYearTable
from create_tables.create_quarter_table import CreateQuarterTable
from create_tables.create_month_table import CreateMonthTable
from create_tables.create_labor_stats_table import CreateLaborStatsTable
from sql import *
from table_info import *

def main():

    # Month tables
    create_month_table = CreateMonthTable("eri_taldau", "postgres", "123456")
    create_month_table.db_connection()
    #1.6
    create_month_table.create_month_table(cons_index_names, months, cons_index_sql, "1-6consumer_price_index1.xlsx",
                                    "отчетный период к соответствующему периоду прошлого года", 
                                    "1.6. ИНДЕКС ПОТРЕБИТЕЛЬСКИХ ЦЕН И ИНДЕКС ЦЕН ПРОИЗВОДИТЕЛЕЙ1,")
    #1.6
    create_month_table.create_month_table(cons_index_names, months, cons_index_sql, "1-6consumer_price_index2.xlsx",
                                    "отчетный период к предыдущему периоду", "1.6. ИНДЕКС ПОТРЕБИТЕЛЬСКИХ ЦЕН И ИНДЕКС ЦЕН ПРОИЗВОДИТЕЛЕЙ2,")
    create_month_table.db_disconnect()

    # # Create labor stats
    # create_labor_stats_table = CreateLaborStatsTable("eri_taldau", "postgres", "123456")
    # create_labor_stats_table.db_connection()
    # #2.1
    # create_labor_stats_table.create_labor_stats_table(labor_stats_names, labor_stats_sql, "2-1labor_market_statistics.xlsx", "2.1. СТАТИСТИКА ТРУДА")
    # create_labor_stats_table.db_disconnect()

    # # Quarter tables
    # create_quarter_table = CreateQuarterTable("eri_taldau", "postgres", "123456")
    # create_quarter_table.db_connection()
    # # 2.2
    # create_quarter_table.create_quarter_table(industry_types_names, avsalary_byactivity_sql, 
    #                                 "2-2average_salary_by_economic_activity_in_thousand_tenge.xlsx", "tenge", 
    #                                 "2.2. СРЕДНЕМЕСЯЧНАЯ ЗАРАБОТНАЯ ПЛАТА ПО ВИДАМ ЭКОНОМИЧЕСКОЙ ДЕЯТЕЛЬНОСТИ (В ТЫС. ТЕНГЕ)")
    # #2.3
    # create_quarter_table.create_quarter_table(industry_types_names, nominal_wage_index_sql, "2-3nominal_wage_index.xlsx", "percent", 
    #                                 "2.3. ИНДЕКС НОМИНАЛЬНОЙ ЗАРАБОТНОЙ ПЛАТЫ РАБОТНИКОВ")
    # #2.4
    # create_quarter_table.create_quarter_table(industry_types_names, real_wage_index_sql, 
    #                                "2-4real_wage_index.xlsx", "percent", "2.4. ИНДЕКС РЕАЛЬНОЙ ЗАРАБОТНОЙ ПЛАТЫ РАБОТНИКОВ")
    # #2.5
    # create_quarter_table.create_quarter_table(region_names, avnomsalary_by_region_sql, "2-5average_nominal_salary_by_region_in_thousand_tenge.xlsx", 
    #                                 "thousand_tenge", "2.5. СРЕДНЕМЕСЯЧНАЯ НОМИНАЛЬНАЯ ЗАРАБОТНАЯ ПЛАТА (В ТЫС. ТЕНГЕ) В РАЗРЕЗЕ РЕГИОНОВ")
    # #2.6
    # create_quarter_table.create_quarter_table(region_names, nomwage_index_by_region_sql, "2-6nominal_wage_index_by_region.xlsx", 
    #                                 "percent", "2.6. ИНДЕКС НОМИНАЛЬНОЙ ЗАРАБОТНОЙ ПЛАТЫ В РАЗРЕЗЕ РЕГИОНОВ")
    # #2.7
    # create_quarter_table.create_quarter_table(region_names, realwage_index_by_region_sql, "2-7real_wage_index_by_region.xlsx", 
    #                                 "percent", "2.7. ИНДЕКС РЕАЛЬНОЙ ЗАРАБОТНОЙ ПЛАТЫ В РАЗРЕЗЕ РЕГИОНОВ")
    # #2.8
    # create_quarter_table.create_quarter_table(region_names, avcapita_nominal_income_by_region_sql, 
    #                                 "2-8average_per_capita_nominal_income_by_region_in_tenge.xlsx", "thousand_tenge", 
    #                                 "2.8. СРЕДНЕДУШЕВЫЕ НОМИНАЛЬНЫЕ ДЕНЕЖНЫЕ ДОХОДЫ НАСЕЛЕНИЯ (В ТЕНГЕ) В РАЗРЕЗЕ РЕГИОНОВ")
    # #2.9
    # create_quarter_table.create_quarter_table(region_names, nominal_income_index_by_region_sql, 
    #                                 "2-9nominal_income_index_by_region.xlsx", "percent", 
    #                                 "2.9. ИНДЕКС НОМИНАЛЬНЫХ ДЕНЕЖНЫХ ДОХОДОВ В РАЗРЕЗЕ РЕГИОНОВ")
    # #2.10
    # create_quarter_table.create_quarter_table(region_names, real_income_index_by_region_sql, 
    #                                 "2-10real_income_index_by_region.xlsx", "percent", 
    #                                 "2.10. ИНДЕКС РЕАЛЬНЫХ ДЕНЕЖНЫХ ДОХОДОВ В РАЗРЕЗЕ РЕГИОНОВ")
    # #2.11
    # create_quarter_table.create_quarter_table(region_names, population_share_below_poverty_line_sql, 
    #                                 "2-11population_share_below_poverty_line.xlsx", "percent", 
    #                                 "2.11. ДОЛЯ НАСЕЛЕНИЯ, ИМЕЮЩЕГО ДОХОДЫ НИЖЕ ВЕЛИЧИНЫ ПРОЖИТОЧНОГО МИНИМУМА")
    # create_quarter_table.db_disconnect()



    # # Year tables
    # create_year_table = CreateYearTable("eri_taldau", "postgres", "123456")
    # create_year_table.db_connection()
    # # 4.2
    # create_year_table.create_year_table(region_names, gdp_by_one_sql, "4-2per_capita_regional_gross_domestic_product.xlsx",
    #                                 "thousand_tenge", "4.2. ВАЛОВЫЙ РЕГИОНАЛЬНЫЙ ПРОДУКТ НА ДУШУ НАСЕЛЕНИЯ")
    # # 4.3
    # create_year_table.create_year_table(region_names, gdp_agricultural_sql, "4-3output_of_agricultural_forestry_and_fishery_production.xlsx",
    #                                 "million_tenge", "4.3. ВАЛОВЫЙ ВЫПУСК ПРОДУКЦИИ (УСЛУГ) СЕЛЬСКОГО, ЛЕСНОГО И РЫБНОГО ХОЗЯЙСТВА")
    # # 4.4
    # create_year_table.create_year_table(region_names, ind_production_volume_sql, "4-4industrial_production_volume_at_current_prices.xlsx",
    #                                 "million_tenge", "4.4. ОБЪЕМЫ ПРОМЫШЛЕННОГО ПРОИЗВОДСТВА В ДЕЙСТВУЮЩИХ ЦЕНАХ")
    # create_year_table.db_disconnect()


if __name__ == '__main__':
    main()