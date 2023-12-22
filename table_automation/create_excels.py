from filltable import FillTable
from sql import *
from table_info import *

def main():
    filltable = FillTable("eri_taldau", "postgres", "123456")
    #1.6
    filltable.create_month_table(cons_index_names, months, cons_index_sql, "consumer_price_index1.xlsx",
                                    "отчетный период к соответствующему периоду прошлого года", 
                                    "ИНДЕКС ПОТРЕБИТЕЛЬСКИХ ЦЕН И ИНДЕКС ЦЕН ПРОИЗВОДИТЕЛЕЙ1,")
    #1.6
    filltable.create_month_table(cons_index_names, months, cons_index_sql, "consumer_price_index2.xlsx",
                                    "отчетный период к предыдущему периоду", "ИНДЕКС ПОТРЕБИТЕЛЬСКИХ ЦЕН И ИНДЕКС ЦЕН ПРОИЗВОДИТЕЛЕЙ2,")
    #2.1
    filltable.create_labor_stats(labor_stats_names, labor_stats_sql, "labor_market_statistics.xlsx", "СТАТИСТИКА ТРУДА")
    #2.2
    filltable.create_quarter_table(industry_types_names, avsalary_byactivity_sql, 
                                    "average_salary_by_economic_activity_in_thousand_tenge.xlsx", "tenge", 
                                    "СРЕДНЕМЕСЯЧНАЯ ЗАРАБОТНАЯ ПЛАТА ПО ВИДАМ ЭКОНОМИЧЕСКОЙ ДЕЯТЕЛЬНОСТИ (В ТЫС. ТЕНГЕ)")
    #2.3
    filltable.create_quarter_table(industry_types_names, nominal_wage_index_sql, "nominal_wage_index.xlsx", "percent", 
                                    "ИНДЕКС НОМИНАЛЬНОЙ ЗАРАБОТНОЙ ПЛАТЫ РАБОТНИКОВ")
    #2.4
    filltable.create_quarter_table(industry_types_names, real_wage_index_sql, 
                                   "real_wage_index.xlsx", "percent", "ИНДЕКС РЕАЛЬНОЙ ЗАРАБОТНОЙ ПЛАТЫ РАБОТНИКОВ")
    #2.5
    filltable.create_quarter_table(region_names, avnomsalary_by_region_sql, "average_nominal_salary_by_region_in_thousand_tenge.xlsx", 
                                    "thousand_tenge", "СРЕДНЕМЕСЯЧНАЯ НОМИНАЛЬНАЯ ЗАРАБОТНАЯ ПЛАТА (В ТЫС. ТЕНГЕ) В РАЗРЕЗЕ РЕГИОНОВ")
    #2.6
    filltable.create_quarter_table(region_names, nomwage_index_by_region_sql, "nominal_wage_index_by_region.xlsx", 
                                    "percent", "ИНДЕКС НОМИНАЛЬНОЙ ЗАРАБОТНОЙ ПЛАТЫ В РАЗРЕЗЕ РЕГИОНОВ")
    #2.7
    filltable.create_quarter_table(region_names, realwage_index_by_region_sql, "real_wage_index_by_region.xlsx", 
                                    "percent", "ИНДЕКС РЕАЛЬНОЙ ЗАРАБОТНОЙ ПЛАТЫ В РАЗРЕЗЕ РЕГИОНОВ")
    #2.8
    filltable.create_quarter_table(region_names, avcapita_nominal_income_by_region_sql, 
                                    "average_per_capita_nominal_income_by_region_in_tenge.xlsx", "thousand_tenge", 
                                    "СРЕДНЕДУШЕВЫЕ НОМИНАЛЬНЫЕ ДЕНЕЖНЫЕ ДОХОДЫ НАСЕЛЕНИЯ (В ТЕНГЕ) В РАЗРЕЗЕ РЕГИОНОВ")
    #2.9
    filltable.create_quarter_table(region_names, nominal_income_index_by_region_sql, 
                                    "nominal_income_index_by_region.xlsx", "percent", 
                                    "ИНДЕКС НОМИНАЛЬНЫХ ДЕНЕЖНЫХ ДОХОДОВ В РАЗРЕЗЕ РЕГИОНОВ")
    #2.10
    filltable.create_quarter_table(region_names, real_income_index_by_region_sql, 
                                    "real_income_index_by_region.xlsx", "percent", 
                                    "ИНДЕКС РЕАЛЬНЫХ ДЕНЕЖНЫХ ДОХОДОВ В РАЗРЕЗЕ РЕГИОНОВ")
    #2.11
    filltable.create_quarter_table(region_names, population_share_below_poverty_line_sql, 
                                    "population_share_below_poverty_line.xlsx", "percent", 
                                    "ДОЛЯ НАСЕЛЕНИЯ, ИМЕЮЩЕГО ДОХОДЫ НИЖЕ ВЕЛИЧИНЫ ПРОЖИТОЧНОГО МИНИМУМА")
    #4.2
    filltable.create_year_table(region_names, gdp_by_one_sql, "per_capita_regional_gross_domestic_product.xlsx",
                                    "thousand_tenge", "ВАЛОВЫЙ РЕГИОНАЛЬНЫЙ ПРОДУКТ НА ДУШУ НАСЕЛЕНИЯ")
    #4.3
    filltable.create_year_table(region_names, gdp_agricultural_sql, "output_of_agricultural_forestry_and_fishery_production.xlsx",
                                    "million_tenge", "ВАЛОВЫЙ ВЫПУСК ПРОДУКЦИИ (УСЛУГ) СЕЛЬСКОГО, ЛЕСНОГО И РЫБНОГО ХОЗЯЙСТВА")
    #4.4
    filltable.create_year_table(region_names, ind_production_volume_sql, "industrial_production_volume_at_current_prices.xlsx",
                                    "million_tenge", "ОБЪЕМЫ ПРОМЫШЛЕННОГО ПРОИЗВОДСТВА В ДЕЙСТВУЮЩИХ ЦЕНАХ")

    filltable.db_disconnect()

if __name__ == '__main__':
    main()