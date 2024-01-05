from automation import Automation

def main():
    automation = Automation("eri_taldau", "postgres", "123456", create_logs=True)
    automation.db_connection()
    
    # # РАЗДЕЛ 1 МАКРОЭКОНОМИКА
    # # 1.1 ВАЛОВЫЙ ВНУТРЕННИЙ ПРОДУКТ
    # automation.insert_data("gdp", "ВВП", "year", 
    #                     "https://taldau.stat.gov.kz/ru/Api/GetIndexData/2709379?period=7&dics=67", 
    #                     "region", "created_at", "value", "description")
    # automation.insert_data("gdp", "ВВП", "quarter_accum", 
    #                     "https://taldau.stat.gov.kz/ru/Api/GetIndexData/2709379?period=9&dics=67", 
    #                     "region", "created_at", "value", "description")
    
    # # 1.2 ИНДЕКС ФИЗИЧЕСКОГО ОБЪЕМА (ИФО) 
    # automation.insert_data("physical_volume_index", "ИФО", "year", 
    #                     "https://www.taldau.stat.gov.kz/ru/Api/GetIndexData/700917?period=7&dics=67", 
    #                     "region", "created_at", "value", "description")
    # automation.insert_data("physical_volume_index", "ИФО", "quarter_accum", 
    #                     "https://www.taldau.stat.gov.kz/ru/Api/GetIndexData/700917?period=9&dics=67", 
    #                     "region", "created_at", "value", "description")
    # automation.insert_data("physical_volume_index_industry", "ИФО Промышленность", "year", 
    #                     "https://www.taldau.stat.gov.kz/ru/Api/GetIndexData/701625?period=7&dics=68,4303,848", 
    #                     "region", "created_at", "value", "description")
    # automation.insert_data("physical_volume_index_industry", "ИФО Промышленность", "month_accum", 
    #                     "https://www.taldau.stat.gov.kz/ru/Api/GetIndexData/701625?period=8&dics=68,4303,848", 
    #                     "region", "created_at", "value", "description")
    
    # automation.insert_data("physical_volume_index_livestock", "ИФО животноводство", "year", 
    #                     "https://taldau.stat.gov.kz/ru/Api/GetIndexData/701228?period=7&dics=67,915,488,848", 
    #                     "region", "activity_type", "agriculture_type", "periods_corellation", "created_at", "value", "description")
    # automation.insert_data("physical_volume_index_livestock", "ИФО животноводство", "month_accum", 
    #                     "https://taldau.stat.gov.kz/ru/Api/GetIndexData/701228?period=8&dics=67,488,848", 
    #                     "region", "agriculture_type", "periods_corellation", "created_at", "value", "description")
    # automation.insert_data("physical_volume_index_housing_th", "ИФО ввод жилья, в тыс. кв. м", "month_accum", 
    #                     "https://www.taldau.stat.gov.kz/ru/Api/GetIndexData/701925?period=8&dics=68,776,59,853,2987", 
    #                     "region", "area_type", "property_type", "units_type", "facility_type", "created_at", "value", "description")
    # automation.insert_data("physical_volume_index_housing_pr", "ИФО ввод жилья, в %", "month_accum", 
    #                     "https://taldau.stat.gov.kz/ru/Api/GetIndexData/701939?period=8&dics=68,776,848,2987", 
    #                     "region", "area_type", "periods_corellation", "facility_type", "created_at", "value", "description")
    # automation.insert_data("physical_volume_index_activity", "ИФО Виды экономической деятельности", "year", 
    #                     "https://www.taldau.stat.gov.kz/ru/Api/GetIndexData/700917?period=7&dics=67,915", 
    #                     "region", "activity_type", "created_at", "value", "description")
    # automation.insert_data("physical_volume_index_activity", "ИФО Виды экономической деятельности", "quarter_accum", 
    #                     "https://www.taldau.stat.gov.kz/ru/Api/GetIndexData/700917?period=9&dics=67,915", 
    #                     "region", "activity_type", "created_at", "value", "description")

    # # 1.3 ПРОИЗВОДИТЕЛЬНОСТЬ ТРУДА
    # automation.insert_data("labor_productivity", "Производительность труда", "year", 
    #                     "https://taldau.stat.gov.kz/ru/Api/GetIndexData/4023003?period=7&dics=67,915", 
    #                     "region", "activity_type", "created_at", "value", "description")
    # automation.insert_data("labor_productivity", "Производительность труда", "quarter_accum", 
    #                     "https://taldau.stat.gov.kz/ru/Api/GetIndexData/4023003?period=9&dics=67,915", 
    #                     "region", "activity_type", "created_at", "value", "description")
    
    # # 1.4 ИНВЕСТИЦИИ В ОСНОВНОЙ КАПИТАЛ + ИНВЕСТИЦИИ В ОСНОВНОЙ КАПИТАЛ ПО ИСТОЧНИКАМ ФИНАНСИРОВАНИЯ
    # automation.insert_data("fixed_capital_investment", "Инвестиции в оснвовной капитал", "year", 
    #                     "https://taldau.stat.gov.kz/ru/Api/GetIndexData/701830?period=7&dics=68,776,59,459,3028", 
    #                     "region", "area_type", "property_type", "funding_source", "activity_type", "created_at", "value", "description")
    # automation.insert_data("fixed_capital_investment", "Инвестиции в оснвовной капитал", "month_accum", 
    #                     "https://taldau.stat.gov.kz/ru/Api/GetIndexData/701830?period=8&dics=68,90,459,3028", 
    #                     "region", "branch_size", "funding_source", "activity_type", "created_at", "value", "description")

    # # 1.6 ИНДЕКС ПОТРЕБИТЕЛЬСКИХ ЦЕН И ИНДЕКС ЦЕН ПРОИЗВОДИТЕЛЕЙ
    # automation.insert_data("consumer_price_index", "Индекс потребительских цен", "month",
    #                     "https://taldau.stat.gov.kz/ru/Api/GetIndexData/703076?period=4&dics=67,848,2753",
    #                     "region", "periods_correlation", "activity_type", "created_at", "value", "description")
    # automation.insert_data("producer_price_index", "Индекс цен производителей", "month",
    #                     "https://taldau.stat.gov.kz/ru/Api/GetIndexData/703039?period=4&dics=68,848,2513,2854,3068",
    #                     "region", "periods_correlation", "countries", "activity_type", "industrial_products_list", "created_at", "value", "description")
    
    # # 1.7 ИНДЕКС ЦЕН НА СОЦИАЛЬНО-ЗНАЧИМЫЕ ПОТРЕБИТЕЛЬСКИЕ ТОВАРЫ (Индекс цен на социально-значимые продовольственные товары)
    # automation.insert_data("soc_imp_goods_price_index", "Индекс цен на социально-значимые потребительские товары", "week",
    #                     "https://taldau.stat.gov.kz/ru/Api/GetIndexData/18808243?period=2&dics=67,4305,848",
    #                     "region", "social_important_goods", "periods_correlation", "created_at", "value", "description")
    
    
    # # РАЗДЕЛ 2 РЫНОК ТРУДА
    # # 2.1 Статистика Труда
    # automation.insert_data("work_force", "Рабочая сила", "year", 
    #                     "https://taldau.stat.gov.kz/ru/Api/GetIndexData/702835?period=7&dics=67,749,576,1773,1793", 
    #                     "region", "area_type", "gender", "education_level", "age_intervals", "created_at", "value", "description")
    # automation.insert_data("work_force", "Рабочая сила", "quarter", 
    #                     "https://taldau.stat.gov.kz/ru/Api/GetIndexData/702835?period=5&dics=67,749,576,1773,1793", 
    #                     "region", "area_type", "gender", "education_level", "age_intervals", "created_at", "value", "description")
    # automation.insert_data("labor_statistics", "Статистика труда", "year",
    #                     "https://taldau.stat.gov.kz/ru/Api/GetIndexData/702840?period=7&dics=67,915,749,576,1773,1793",
    #                     "region", "activity_type", "area_type", "gender", "education_level", "age_intervals", "created_at", "value", "description")
    # automation.insert_data("labor_statistics", "Статистика труда", "quarter",
    #                     "https://taldau.stat.gov.kz/ru/Api/GetIndexData/702840?period=5&dics=67,2353,749,576,1773,1793",
    #                     "region", "activity_type", "area_type", "gender", "education_level", "age_intervals", "created_at", "value", "description")
    # automation.insert_data("wage_earners", "Наемные работники", "year", 
    #                     "https://taldau.stat.gov.kz/ru/Api/GetIndexData/702882?period=7&dics=67,915,749,576,1773,1793", 
    #                     "region", "activity_type", "area_type", "gender", "education_level", "age_intervals", "created_at", "value", "description")
    # automation.insert_data("wage_earners", "Наемные работники", "quarter", 
    #                     "https://taldau.stat.gov.kz/ru/Api/GetIndexData/702882?period=5&dics=67,915,749,576,1773,1793", 
    #                     "region", "activity_type", "area_type", "gender", "education_level", "age_intervals", "created_at", "value", "description")
    # automation.insert_data("automation_employed", "Самозанятые", "year", 
    #                     "https://taldau.stat.gov.kz/ru/Api/GetIndexData/702935?period=7&dics=67,915,749,576,1773,1793", 
    #                     "region", "activity_type", "area_type", "gender", "education_level", "age_intervals", "created_at", "value", "description")
    # automation.insert_data("automation_employed", "Самозанятые", "quarter", 
    #                     "https://taldau.stat.gov.kz/ru/Api/GetIndexData/702935?period=5&dics=67,2353,749,576,1773,1793", 
    #                     "region", "activity_type", "area_type", "gender", "education_level", "age_intervals", "created_at", "value", "description")
    # automation.insert_data("unemployed_number", "Численность безработных", "year", 
    #                     "https://taldau.stat.gov.kz/ru/Api/GetIndexData/702943?period=7&dics=67,749,576,1773,1793", 
    #                     "region", "area_type", "gender", "education_level", "age_intervals", "created_at", "value", "description")
    # automation.insert_data("unemployed_number", "Численность безработных", "quarter", 
    #                     "https://taldau.stat.gov.kz/ru/Api/GetIndexData/702943?period=5&dics=67,749,576,1773,1793", 
    #                     "region", "area_type", "gender", "education_level", "age_intervals", "created_at", "value", "description")
    # automation.insert_data("unemployment_rate", "Уровень безработицы", "year", 
    #                     "https://taldau.stat.gov.kz/ru/Api/GetIndexData/702944?period=7&dics=67,749,576,1773,1793", 
    #                     "region", "area_type", "gender", "education_level", "age_intervals", "created_at", "value", "description")
    # automation.insert_data("unemployment_rate", "Уровень безработицы", "month", 
    #                     "https://taldau.stat.gov.kz/ru/Api/GetIndexData/702944?period=4&dics=67", 
    #                     "region", "created_at", "value", "description")
    # automation.insert_data("average_wages", "Средняя заработная плата", "year", 
    #                     "https://taldau.stat.gov.kz/ru/Api/GetIndexData/702972?period=7&dics=68,859,776,2813,576", 
    #                     "region", "activity_type", "area_type", "enterprise_dimension", "gender", "created_at", "value", "description")
    # automation.insert_data("average_wages", "Средняя заработная плата", "quarter", 
    #                     "https://taldau.stat.gov.kz/ru/Api/GetIndexData/702972?period=5&dics=68,859,681", 
    #                     "region", "activity_type", "economic_sectors", "created_at", "value", "description")

    # # 2.2, 2.5 СРЕДНЕМЕСЯЧНАЯ ЗАРАБОТНАЯ ПЛАТА
    # automation.insert_data("avmon_nom_wages", "Среднемесячная номинальная заработная плата", "year",
    #                     "https://taldau.stat.gov.kz/ru/Api/GetIndexData/702972?period=7&dics=68,859,776,2813,576",
    #                     "region", "activity_type", "area_type", "enterprise_dimension", "gender", "created_at", "value", "description")
    # automation.insert_data("avmon_nom_wages", "Среднемесячная номинальная заработная плата", "quarter",
    #                     "https://taldau.stat.gov.kz/ru/Api/GetIndexData/702972?period=5&dics=68,859,681",
    #                     "region", "activity_type", "economic_sectors", "created_at", "value", "description")
    
    # # 2.3, 2.6 ИНДЕКС НОМИНАЛЬНОЙ ЗАРАБОТНОЙ ПЛАТЫ РАБОТНИКОВ
    # automation.insert_data("nom_wages_index", "Индекс номинальной заработной платы", "year",
    #                     "https://taldau.stat.gov.kz/ru/Api/GetIndexData/702974?period=7&dics=68,859,2813,576,848",
    #                     "region", "activity_type", "enterprise_dimension", "gender", "periods_correlation", "created_at", "value", "description")
    # automation.insert_data("nom_wages_index", "Индекс номинальной заработной платы", "quarter",
    #                     "https://taldau.stat.gov.kz/ru/Api/GetIndexData/702974?period=5&dics=68,859,2813,848",
    #                     "region", "activity_type", "enterprise_dimension", "periods_correlation", "created_at", "value", "description")
    
    # # 2.4, 2.7 ИНДЕКС РЕАЛЬНОЙ ЗАРАБОТНОЙ ПЛАТЫ РАБОТНИКОВ
    # automation.insert_data("real_wages_index", "Индекс реальной заработной платы", "year",
    #                     "https://taldau.stat.gov.kz/ru/Api/GetIndexData/702976?period=7&dics=68,859,2813,576,848",
    #                     "region", "activity_type", "enterprise_dimension", "gender", "periods_correlation", "created_at", "value", "description")
    # automation.insert_data("real_wages_index", "Индекс реальной заработной платы", "quarter",
    #                     "https://taldau.stat.gov.kz/ru/Api/GetIndexData/702976?period=5&dics=68,859,2813,848",
    #                     "region", "activity_type", "enterprise_dimension", "periods_correlation", "created_at", "value", "description")
    
    # # 2.8 СРЕДНЕДУШЕВЫЕ НОМИНАЛЬНЫЕ ДЕНЕЖНЫЕ ДОХОДЫ НАСЕЛЕНИЯ (В ТЕНГЕ) В РАЗРЕЗЕ РЕГИОНОВ
    # automation.insert_data("avcap_pop_nom_income", "Среднедушевые номинальные денежные доходы населения", "year", 
    #                     "https://taldau.stat.gov.kz/ru/Api/GetIndexData/704447?period=7&dics=67", 
    #                     "region", "created_at", "value", "description")
    # automation.insert_data("avcap_pop_nom_income", "Среднедушевые номинальные денежные доходы населения", "quarter", 
    #                     "https://taldau.stat.gov.kz/ru/Api/GetIndexData/704447?period=5&dics=67", 
    #                     "region", "created_at", "value", "description")
    
    # # 2.9 ИНДЕКС НОМИНАЛЬНЫХ ДЕНЕЖНЫХ ДОХОДОВ В РАЗРЕЗЕ РЕГИОНОВ
    # automation.insert_data("nom_income_index", "Индекс номинальных денежных доходов в разрезе регионов", "year", 
    #                     "https://taldau.stat.gov.kz/ru/Api/GetIndexData/704448?period=7&dics=67", 
    #                     "region", "created_at", "value", "description")
    # automation.insert_data("nom_income_index", "Индекс номинальных денежных доходов в разрезе регионов", "quarter", 
    #                     "https://taldau.stat.gov.kz/ru/Api/GetIndexData/704448?period=5&dics=67", 
    #                     "region", "created_at", "value", "description")
    
    # # 2.10 ИНДЕКС РЕАЛЬНЫХ ДЕНЕЖНЫХ ДОХОДОВ В РАЗРЕЗЕ РЕГИОНОВ
    # automation.insert_data("real_income_index", "Индекс реальных денежных доходов в разрезе регионов", "year", 
    #                     "https://taldau.stat.gov.kz/ru/Api/GetIndexData/704449?period=7&dics=67", 
    #                     "region", "created_at", "value", "description")
    # automation.insert_data("real_income_index", "Индекс реальных денежных доходов в разрезе регионов", "quarter", 
    #                     "https://taldau.stat.gov.kz/ru/Api/GetIndexData/704449?period=5&dics=67", 
    #                     "region", "created_at", "value", "description")
    
    # # 2.11 ДОЛЯ НАСЕЛЕНИЯ, ИМЕЮЩЕГО ДОХОДЫ НИЖЕ ВЕЛИЧИНЫ ПРОЖИТОЧНОГО МИНИМУМА
    automation.insert_data("pop_income_below_subsistence", "Доля населения, имеющего доходы ниже величины прожиточного минимума", "quarter", 
                        "https://taldau.stat.gov.kz/ru/Api/GetIndexData/704498?period=5&dics=67,749", 
                        "region", "area_type", "created_at", "value", "description")
    # automation.insert_data("pop_income_below_subsistence", "Доля населения, имеющего доходы ниже величины прожиточного минимума", "year", 
    #                     "https://taldau.stat.gov.kz/ru/Api/GetIndexData/704498?period=7&dics=67,749", 
    #                     "region", "area_type", "created_at", "value", "description")
    
    
    # # РАЗДЕЛ 3 ПРЕДПРИНИМАТЕЛЬСТВО
    # # 3.1 ОБЩИЕ ПОКАЗАТЕЛИ
    # automation.insert_data("share_sme", "Доля МСП в ВПП", "year", 
    #                     "https://taldau.stat.gov.kz/ru/Api/GetIndexData/19824647?period=7&dics=67", 
    #                     "region", "created_at", "value", "description")
    # automation.insert_data("share_sme_small", "Доля малых МСП в ВПП", "year", 
    #                     "https://taldau.stat.gov.kz/ru/Api/GetIndexData/20380630?period=7&dics=67", 
    #                     "region", "created_at", "value", "description")
    # automation.insert_data("share_sme_medium", "Доля средних МСП в ВПП", "year", 
    #                     "https://taldau.stat.gov.kz/ru/Api/GetIndexData/20380634?period=7&dics=67", 
    #                     "region", "created_at", "value", "description")
    # automation.insert_data("registered_sme_number", "Количество зарегистрированных субъектов МСП", "year", 
    #                     "https://taldau.stat.gov.kz/ru/Api/GetIndexData/19722414?period=7&dics=67,915,90", 
    #                     "region", "activity_type", "enterprise_dimension", "created_at", "value", "description")
    # automation.insert_data("operating_sme_number", "Количество действующих субъектов МСП", "year", 
    #                     "https://taldau.stat.gov.kz/ru/Api/GetIndexData/19722421?period=7&dics=67,915,90", 
    #                     "region", "activity_type", "enterprise_dimension", "created_at", "value", "description")
    # automation.insert_data("employees_number", "Численность занятых", "year", 
    #                     "https://taldau.stat.gov.kz/ru/Api/GetIndexData/18714472?period=7&dics=67,915,90", 
    #                     "region", "activity_type", "enterprise_dimension", "created_at", "value", "description")
    # automation.insert_data("production_output", "Выпуск продукции", "year", 
    #                     "https://taldau.stat.gov.kz/ru/Api/GetIndexData/701176?period=7&dics=67,915,90", 
    #                     "region", "activity_type", "enterprise_dimension", "created_at", "value", "description")
    # automation.insert_data("entities_led_by_under_29", "Количество действующих юр.лиц, руководителями которых является молодежь до 29 лет ", "quarter_accum", 
    #                     "https://taldau.stat.gov.kz/ru/Api/GetIndexData/20612386?period=9&dics=67,915,749,576", 
    #                     "region", "activity_type", "area_type", "gender", "created_at", "value", "description")
    # automation.insert_data("entities_led_by_under_35", "Количество действующих юр.лиц, руководителями которых является молодежь до 35 лет", "quarter_accum", 
    #                     "https://taldau.stat.gov.kz/ru/Api/GetIndexData/77218052?period=9&dics=67,915,749,576", 
    #                     "region", "activity_type", "area_type", "gender", "created_at", "value", "description")
    
    # # 3.2 ОТРАСЛЕВАЯ СПЕЦИАЛИЗАЦИЯ СУБЪЕКТОВ МСП В 2021 ГОДУ, В %
    # automation.insert_data("industry_specialization_sme", "Отраслевая специализация субъектов МСП", "year",
    #                     "https://taldau.stat.gov.kz/ru/Api/GetIndexData/19722414?period=7&dics=67,915,90",
    #                     "region", "activity_type", "enterprise_dimension", "created_at", "value", "description")
    
    
    # # РАЗДЕЛ 4 РЕГИОНЫ
    # # 4.1 ВАЛОВЫЙ РЕГИОНАЛЬНЫЙ ПРОДУКТ И ИНДЕКС ФИЗИЧЕСКОГО ОБЪЕМА
    # automation.insert_data("grp", "Валовый региональный продукт", "year", 
    #                     "https://taldau.stat.gov.kz/ru/Api/GetIndexData/2709379?period=7&dics=67", 
    #                     "region", "created_at", "value", "description")
    # automation.insert_data("grp", "Валовый региональный продукт", "quarter_accum", 
    #                     "https://taldau.stat.gov.kz/ru/Api/GetIndexData/2709379?period=9&dics=67", 
    #                     "region", "created_at", "value", "description")
    # automation.insert_data("grp_volume_index", "ИФО для валового внутреннего продукта", "quarter_accum", 
    #                     "https://taldau.stat.gov.kz/ru/Api/GetIndexData/2979005?period=9&dics=67", 
    #                     "region", "created_at", "value", "description")
    # automation.insert_data("grp_volume_index", "ИФО для валового внутреннего продукта", "year", 
    #                     "https://taldau.stat.gov.kz/ru/Api/GetIndexData/2979005?period=7&dics=67", 
    #                     "region", "created_at", "value", "description")
    
    # # 4.2 ВАЛОВЫЙ РЕГИОНАЛЬНЫЙ ПРОДУКТ НА ДУШУ НАСЕЛЕНИЯ
    # automation.insert_data("grp_per_capita", "Валовый региональный продукт на душу населения", "year", 
    #                     "https://taldau.stat.gov.kz/ru/Api/GetIndexData/2709380?period=7&dics=67", 
    #                     "region", "created_at", "value", "description")
    # automation.insert_data("grp_per_capita", "Валовый региональный продукт на душу населения", "quarter_accum", 
    #                     "https://taldau.stat.gov.kz/ru/Api/GetIndexData/2709380?period=9&dics=67", 
    #                     "region", "created_at", "value", "description")
    
    # # 4.3	ВАЛОВЫЙ ВЫПУСК ПРОДУКЦИИ (УСЛУГ) СЕЛЬСКОГО, ЛЕСНОГО И РЫБНОГО ХОЗЯЙСТВА
    # automation.insert_data("gop_agriculture_forest_fish", "Валовой выпуск продукции (услуг) сельского, лесного и рыбного хозяйства", "year", 
    #                     "https://taldau.stat.gov.kz/ru/Api/GetIndexData/701188?period=7&dics=67,773", 
    #                     "region", "price_measurement", "created_at", "value", "description")
    # automation.insert_data("gop_agriculture_forest_fish", "Валовой выпуск продукции (услуг) сельского, лесного и рыбного хозяйства", "month_accum", 
    #                     "https://taldau.stat.gov.kz/ru/Api/GetIndexData/701188?period=8&dics=67,488,773", 
    #                     "region", "household_category", "price_measurement", "created_at", "value", "description")
     
    #  # 4.4 ОБЪЕМЫ ПРОМЫШЛЕННОГО ПРОИЗВОДСТВА В ДЕЙСТВУЮЩИХ ЦЕНАХ 
    # automation.insert_data("industrial_production_volumes", "Объемы промышленного производства", "year", 
    #                     "https://taldau.stat.gov.kz/ru/Api/GetIndexData/701592?period=7&dics=68,4303", 
    #                     'region', "activity_type", "created_at", "value", "description")
    # automation.insert_data("industrial_production_volumes", "Объемы промышленного производства", "month_accum", 
    #                     "https://taldau.stat.gov.kz/ru/Api/GetIndexData/701592?period=8&dics=68,776,4303,524", 
    #                     'region', "area_type", "activity_type", "periods_correlation", "created_at", "value", "description")
    
    # # 4.5 ЧИСЛЕННОСТЬ НАСЕЛЕНИЯ РЕСПУБЛИКИ КАЗАХСТАН НА НАЧАЛО ГОДА
    # automation.insert_data("population_of_kazakhstan", "Численность населения Республики Казахстан", "year", 
    #                      "https://taldau.stat.gov.kz/ru/Api/GetIndexData/703831?period=7&dics=67,749,576,3198", 
    #                      "region", "area_type", "gender", "age_groups", "created_at", "value", "description")
    # automation.insert_data("population_of_kazakhstan", "Численность населения Республики Казахстан", "month", 
    #                      "https://taldau.stat.gov.kz/ru/Api/GetIndexData/703831?period=4&dics=67,749", 
    #                      "region", "area_type", "created_at", "value", "description")
    
    # # 4.6 ЧИСЛЕННОСТЬ НАСЕЛЕНИЯ НА НАЧАЛО ГОДА 
    # automation.insert_data("population_year_beginning", "Численность населения на начало года", "year", 
    #                     "https://taldau.stat.gov.kz/ru/Api/GetIndexData/703831?period=7&dics=67,749,576,1433", 
    #                     'region', "area_type", "gender", "population_group", "created_at", "value", "description")

    automation.db_disconnect()

if __name__ == '__main__':
    main()