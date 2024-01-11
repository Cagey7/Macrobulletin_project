from filltable import FillTable
from create_tables.create_year_table import CreateYearTable
from create_tables.create_quarter_table import CreateQuarterTable
from create_tables.create_month_table import CreateMonthTable
from create_tables.create_labor_stats_table import CreateLaborStatsTable
from create_tables.create_pop_begin_table import CreatePopBeginTable
from create_tables.create_pop_begin_2_table import CreatePopBegin2Table
from create_tables.create_urbanization_table import CreateUrbanizationTable
from create_tables.create_reg_gros_phys_vol_table import CreateRegGrosPhysVolTable
from create_tables.create_sector_spec_msp_table import CreateMSPTable
from create_tables.create_lab_prod_cap_investment_table import CreateLabProdCapInvestmentTable
from create_tables.create_cap_investment_by_funding_table import CreateCapInvestmentByFundingTable
from create_tables.create_ppi_table import CreatePPITable
from sql import *
from table_info import *

def main():

    # # Create PPI table
    # create_ppi_table = CreatePPITable("eri_taldau", "postgres", "123456")
    # create_ppi_table.db_connection()
    # # 1.2
    # create_ppi_table.create_ppi_table(ppi_names, "quarter", ppi_sql, "1-2ppi.xlsx",
    #                                     "1.2. ИНДЕКС ФИЗИЧЕСКОГО ОБЪЕМА (ИФО) ")
    # create_ppi_table.db_disconnect()


    # Create labor productivity and capital investment
    create_lab_prod_cap_investment_table = CreateLabProdCapInvestmentTable("eri_taldau", "postgres", "123456")
    create_lab_prod_cap_investment_table.db_connection()
    # # 1.3
    # create_lab_prod_cap_investment_table.create_lab_prod_cap_investment_table(labor_productivity_names, "quarter", labor_productivity_sql, "1-3labor_productivity.xlsx",
    #                                 "thousand_tenge", "1.3. ПРОИЗВОДИТЕЛЬНОСТЬ ТРУДА ")
    # 1.4
    create_lab_prod_cap_investment_table.create_lab_prod_cap_investment_table(capital_investment_names, "month", capital_investment_sql, "1-4capital_investment1.xlsx",
                                    "million_tenge", "1.4.	ИНВЕСТИЦИИ В ОСНОВНОЙ КАПИТАЛ ")
    create_lab_prod_cap_investment_table.db_disconnect()


    # # Create capital investment by funding source
    # create_cap_investment_by_funding_table = CreateCapInvestmentByFundingTable("eri_taldau", "postgres", "123456")
    # create_cap_investment_by_funding_table.db_connection()
    # # 1.4 2
    # create_cap_investment_by_funding_table.create_cap_investment_by_funding_table(capital_investment_by_funding_names, "month", capital_investment_by_funding_sql, "1-4capital_investment2.xlsx",
    #                                 "million_tenge", "1.4.	ИНВЕСТИЦИИ В ОСНОВНОЙ КАПИТАЛ ПО ИСТОЧНИКАМ ФИНАНСИРОВАНИЯ")
    # create_cap_investment_by_funding_table.db_disconnect()


    # # Month tables
    # create_month_table = CreateMonthTable("eri_taldau", "postgres", "123456")
    # create_month_table.db_connection()
    # #1.6
    # create_month_table.create_month_table(cons_index_names, months, cons_index_sql, "1-6consumer_price_index1.xlsx",
    #                                 "отчетный период к соответствующему периоду прошлого года", 
    #                                 "1.6. ИНДЕКС ПОТРЕБИТЕЛЬСКИХ ЦЕН И ИНДЕКС ЦЕН ПРОИЗВОДИТЕЛЕЙ1,")
    # #1.6
    # create_month_table.create_month_table(cons_index_names, months, cons_index_sql, "1-6consumer_price_index2.xlsx",
    #                                 "отчетный период к предыдущему периоду", "1.6. ИНДЕКС ПОТРЕБИТЕЛЬСКИХ ЦЕН И ИНДЕКС ЦЕН ПРОИЗВОДИТЕЛЕЙ2,")
    # create_month_table.db_disconnect()


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


    # # Create sectoral specialization msp
    # create_sector_spec_msp_table = CreateMSPTable("eri_taldau", "postgres", "123456")
    # create_sector_spec_msp_table.db_connection()
    # # 3.2
    # create_sector_spec_msp_table.create_sector_spec_msp_table(msp_names, msp_query_names, sector_spec_msp_sql, "3-2sectoral_specialization_msp_2021_percentage.xlsx",
    #                                 "3.2.	ОТРАСЛЕВАЯ СПЕЦИАЛИЗАЦИЯ СУБЪЕКТОВ МСП, В %")
    # create_sector_spec_msp_table.db_disconnect()


    # # Create regional gros and physical volume index
    # create_reg_gros_phys_vol_table = CreateRegGrosPhysVolTable("eri_taldau", "postgres", "123456")
    # create_reg_gros_phys_vol_table.db_connection()
    # # 4.1
    # create_reg_gros_phys_vol_table.create_reg_gros_phys_vol_table(region_names, "quarter", reg_gros_phys_vol_sql, "4-1regional_gross_domestic_product_and_physical_volume_index.xlsx",
    #                                 "million_tenge", "4.1. ВАЛОВЫЙ РЕГИОНАЛЬНЫЙ ПРОДУКТ И ИНДЕКС ФИЗИЧЕСКОГО ОБЪЕМА")
    # create_reg_gros_phys_vol_table.db_disconnect()


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


    # # Create population beginning
    # create_pop_begin_table = CreatePopBeginTable("eri_taldau", "postgres", "123456")
    # create_pop_begin_table.db_connection()
    # # 4.5
    # create_pop_begin_table.create_pop_begin_table(region_names, months, pop_at_beginning_year_sql, "4-5population_at_the_beginning_of_the_year_kz.xlsx",
    #                                 "4.5. ЧИСЛЕННОСТЬ НАСЕЛЕНИЯ РЕСПУБЛИКИ КАЗАХСТАН НА НАЧАЛО ГОДА")
    # create_pop_begin_table.db_disconnect()


    # # Create population beginning 2
    # create_pop_begin_2_table = CreatePopBegin2Table("eri_taldau", "postgres", "123456")
    # create_pop_begin_2_table.db_connection()
    # # 4.6
    # create_pop_begin_2_table.create_pop_begin_2_table(region_names, pop_at_beginning_year2_sql, "4-6population_at_the_beginning_of_the_year1.xlsx",
    #                                 "4.6. ЧИСЛЕННОСТЬ НАСЕЛЕНИЯ НА НАЧАЛО ГОДА ")
    # create_pop_begin_2_table.db_disconnect()


    # # Create urbanization
    # create_urbanization_table = CreateUrbanizationTable("eri_taldau", "postgres", "123456")
    # create_urbanization_table.db_connection()
    # # 4.7
    # create_urbanization_table.create_urbanization_table(region_names, months, pop_at_beginning_year_sql, "4-7urbanization_as_percentage_of_total_population_estimate.xlsx",
    #                                 "4.7. УРБАНИЗАЦИЯ")
    # create_urbanization_table.db_disconnect()


if __name__ == '__main__':
    main()