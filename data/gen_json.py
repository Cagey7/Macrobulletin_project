import json

topics_data = [
    ["1. МАКРОЭКОНОМИКА", "macroeconomics"],
    ["2. РЫНОК ТРУДА", "labor-market"],
    ["3. ПРЕДПРИНИМАТЕЛЬСТВО", "entrepreneurship"],
    ["4. РЕГИОНЫ", "regions"],
]


economic_indices = [
    ['1.2. ИНДЕКС ФИЗИЧЕСКОГО ОБЪЕМА (ИФО)', 'ppi', '1. МАКРОЭКОНОМИКА'],
    ['1.3. ПРОИЗВОДИТЕЛЬНОСТЬ ТРУДА', 'labor-productivity', '1. МАКРОЭКОНОМИКА'],
    ['1.4. ИНВЕСТИЦИИ В ОСНОВНОЙ КАПИТАЛ', 'capital-investment', '1. МАКРОЭКОНОМИКА'],
    ['1.6. ИНДЕКС ПОТРЕБИТЕЛЬСКИХ ЦЕН И ИНДЕКС ЦЕН ПРОИЗВОДИТЕЛЕЙ', 'consumer-price-index', '1. МАКРОЭКОНОМИКА'],
    
    
    ['2.2. СРЕДНЕМЕСЯЧНАЯ ЗАРАБОТНАЯ ПЛАТА ПО ВИДАМ ЭКОНОМИЧЕСКОЙ ДЕЯТЕЛЬНОСТИ (В ТЫС. ТЕНГЕ)', 'avsalary-economic-activity', '2. РЫНОК ТРУДА'],
    ['2.3. ИНДЕКС НОМИНАЛЬНОЙ ЗАРАБОТНОЙ ПЛАТЫ РАБОТНИКОВ', 'nominal-wage-index', '2. РЫНОК ТРУДА'],
    ['2.4. ИНДЕКС РЕАЛЬНОЙ ЗАРАБОТНОЙ ПЛАТЫ РАБОТНИКОВ', 'real-wage-index', '2. РЫНОК ТРУДА'],
    ['2.5. СРЕДНЕМЕСЯЧНАЯ НОМИНАЛЬНАЯ ЗАРАБОТНАЯ ПЛАТА (В ТЫС. ТЕНГЕ) В РАЗРЕЗЕ РЕГИОНОВ', 'avnominal-salary-region', '2. РЫНОК ТРУДА'],
    ['2.6. ИНДЕКС НОМИНАЛЬНОЙ ЗАРАБОТНОЙ ПЛАТЫ В РАЗРЕЗЕ РЕГИОНОВ', 'nomwage-index-region', '2. РЫНОК ТРУДА'],
    ['2.7. ИНДЕКС РЕАЛЬНОЙ ЗАРАБОТНОЙ ПЛАТЫ В РАЗРЕЗЕ РЕГИОНОВ', 'realwage-index-region', '2. РЫНОК ТРУДА'],
    ['2.8. СРЕДНЕДУШЕВЫЕ НОМИНАЛЬНЫЕ ДЕНЕЖНЫЕ ДОХОДЫ НАСЕЛЕНИЯ (В ТЕНГЕ) В РАЗРЕЗЕ РЕГИОНОВ', 'avpercapita-nominal-income', '2. РЫНОК ТРУДА'],
    ['2.9. ИНДЕКС НОМИНАЛЬНЫХ ДЕНЕЖНЫХ ДОХОДОВ В РАЗРЕЗЕ РЕГИОНОВ', 'nomincome-index-region', '2. РЫНОК ТРУДА'],
    ['2.10. ИНДЕКС РЕАЛЬНЫХ ДЕНЕЖНЫХ ДОХОДОВ В РАЗРЕЗЕ РЕГИОНОВ', 'realincome-index-region', '2. РЫНОК ТРУДА'],
    ['2.11. ДОЛЯ НАСЕЛЕНИЯ, ИМЕЮЩЕГО ДОХОДЫ НИЖЕ ВЕЛИЧИНЫ ПРОЖИТОЧНОГО МИНИМУМА', 'popshare-below-povline', '2. РЫНОК ТРУДА'],
    
    
    ['3.2. ОТРАСЛЕВАЯ СПЕЦИАЛИЗАЦИЯ СУБЪЕКТОВ МСП В 2021 ГОДУ, В %', 'sectoral-specialization', '3. ПРЕДПРИНИМАТЕЛЬСТВО'],
    
    
    ['4.1. ВАЛОВЫЙ РЕГИОНАЛЬНЫЙ ПРОДУКТ И ИНДЕКС ФИЗИЧЕСКОГО ОБЪЕМА', 'rgdp-pvi', '4. РЕГИОНЫ'],
    ['4.2. ВАЛОВЫЙ РЕГИОНАЛЬНЫЙ ПРОДУКТ НА ДУШУ НАСЕЛЕНИЯ', 'pcrgdp', '4. РЕГИОНЫ'],
    ['4.3. ВАЛОВЫЙ ВЫПУСК ПРОДУКЦИИ (УСЛУГ) СЕЛЬСКОГО, ЛЕСНОГО И РЫБНОГО ХОЗЯЙСТВА', 'agri-forestry-fishery', '4. РЕГИОНЫ'],
    ['4.4. ОБЪЕМЫ ПРОМЫШЛЕННОГО ПРОИЗВОДСТВА В ДЕЙСТВУЮЩИХ ЦЕНАХ', 'industrial-production-current', '4. РЕГИОНЫ'],
    ['4.5. ЧИСЛЕННОСТЬ НАСЕЛЕНИЯ РЕСПУБЛИКИ КАЗАХСТАН НА НАЧАЛО ГОДА', 'population-beginning-year-kz', '4. РЕГИОНЫ'],
    ['4.6. ЧИСЛЕННОСТЬ НАСЕЛЕНИЯ НА НАЧАЛО ГОДА', 'population-beginning-year', '4. РЕГИОНЫ'],
    ['4.7. УРБАНИЗАЦИЯ (ДОЛЯ ГОРОДСКОГО К ОБЩЕЙ ЧИСЛЕННОСТИ НАСЕЛЕНИЯ РАСЧЁТНО)', 'urbanization-percent', '4. РЕГИОНЫ'],
]


table_info = [
    ['1.2. ИНДЕКС ФИЗИЧЕСКОГО ОБЪЕМА (ИФО)', '1-2ppi'],
    ['1.3. ПРОИЗВОДИТЕЛЬНОСТЬ ТРУДА', '1-3labor_productivity'],
    ['1.4. ИНВЕСТИЦИИ В ОСНОВНОЙ КАПИТАЛ', '1-4capital_investment'],
    ['1.6. ИНДЕКС ПОТРЕБИТЕЛЬСКИХ ЦЕН И ИНДЕКС ЦЕН ПРОИЗВОДИТЕЛЕЙ', '1-6consumer_price_index1'],
    ['1.6. ИНДЕКС ПОТРЕБИТЕЛЬСКИХ ЦЕН И ИНДЕКС ЦЕН ПРОИЗВОДИТЕЛЕЙ', '1-6consumer_price_index2'],
    
    
    ['2.2. СРЕДНЕМЕСЯЧНАЯ ЗАРАБОТНАЯ ПЛАТА ПО ВИДАМ ЭКОНОМИЧЕСКОЙ ДЕЯТЕЛЬНОСТИ (В ТЫС. ТЕНГЕ)', '2-2average_salary_by_economic_activity_in_thousand_tenge'],
    ['2.3. ИНДЕКС НОМИНАЛЬНОЙ ЗАРАБОТНОЙ ПЛАТЫ РАБОТНИКОВ', '2-3nominal_wage_index'],
    ['2.4. ИНДЕКС РЕАЛЬНОЙ ЗАРАБОТНОЙ ПЛАТЫ РАБОТНИКОВ', '2-4real_wage_index'],
    ['2.5. СРЕДНЕМЕСЯЧНАЯ НОМИНАЛЬНАЯ ЗАРАБОТНАЯ ПЛАТА (В ТЫС. ТЕНГЕ) В РАЗРЕЗЕ РЕГИОНОВ', '2-5average_nominal_salary_by_region_in_thousand_tenge'],
    ['2.6. ИНДЕКС НОМИНАЛЬНОЙ ЗАРАБОТНОЙ ПЛАТЫ В РАЗРЕЗЕ РЕГИОНОВ', '2-6nominal_wage_index_by_region'],
    ['2.7. ИНДЕКС РЕАЛЬНОЙ ЗАРАБОТНОЙ ПЛАТЫ В РАЗРЕЗЕ РЕГИОНОВ', '2-7real_wage_index_by_region'],
    ['2.8. СРЕДНЕДУШЕВЫЕ НОМИНАЛЬНЫЕ ДЕНЕЖНЫЕ ДОХОДЫ НАСЕЛЕНИЯ (В ТЕНГЕ) В РАЗРЕЗЕ РЕГИОНОВ', '2-8average_per_capita_nominal_income_by_region_in_tenge'],
    ['2.9. ИНДЕКС НОМИНАЛЬНЫХ ДЕНЕЖНЫХ ДОХОДОВ В РАЗРЕЗЕ РЕГИОНОВ', '2-9nominal_income_index_by_region'],
    ['2.10. ИНДЕКС РЕАЛЬНЫХ ДЕНЕЖНЫХ ДОХОДОВ В РАЗРЕЗЕ РЕГИОНОВ', '2-10real_income_index_by_region'],
    ['2.11. ДОЛЯ НАСЕЛЕНИЯ, ИМЕЮЩЕГО ДОХОДЫ НИЖЕ ВЕЛИЧИНЫ ПРОЖИТОЧНОГО МИНИМУМА', '2-11population_share_below_poverty_line'],
    
    
    ['3.2. ОТРАСЛЕВАЯ СПЕЦИАЛИЗАЦИЯ СУБЪЕКТОВ МСП В 2021 ГОДУ, В %', '3-2sectoral_specialization_msp_2021_percentage'],
    
    
    ['4.1. ВАЛОВЫЙ РЕГИОНАЛЬНЫЙ ПРОДУКТ И ИНДЕКС ФИЗИЧЕСКОГО ОБЪЕМА', '4-1regional_gross_domestic_product_and_physical_volume_index'],
    ['4.2. ВАЛОВЫЙ РЕГИОНАЛЬНЫЙ ПРОДУКТ НА ДУШУ НАСЕЛЕНИЯ', '4-2per_capita_regional_gross_domestic_product'],
    ['4.3. ВАЛОВЫЙ ВЫПУСК ПРОДУКЦИИ (УСЛУГ) СЕЛЬСКОГО, ЛЕСНОГО И РЫБНОГО ХОЗЯЙСТВА', '4-3output_of_agricultural_forestry_and_fishery_production'],
    ['4.4. ОБЪЕМЫ ПРОМЫШЛЕННОГО ПРОИЗВОДСТВА В ДЕЙСТВУЮЩИХ ЦЕНАХ', '4-4industrial_production_volume_at_current_prices'],
    ['4.5. ЧИСЛЕННОСТЬ НАСЕЛЕНИЯ РЕСПУБЛИКИ КАЗАХСТАН НА НАЧАЛО ГОДА', '4-5population_at_the_beginning_of_the_year_kz'],
    ['4.6. ЧИСЛЕННОСТЬ НАСЕЛЕНИЯ НА НАЧАЛО ГОДА', '4-6population_at_the_beginning_of_the_year1'],
    ['4.6. ЧИСЛЕННОСТЬ НАСЕЛЕНИЯ НА НАЧАЛО ГОДА', '4-6population_at_the_beginning_of_the_year2'],
    ['4.6. ЧИСЛЕННОСТЬ НАСЕЛЕНИЯ НА НАЧАЛО ГОДА', '4-6population_at_the_beginning_of_the_year3'],
    ['4.7. УРБАНИЗАЦИЯ (ДОЛЯ ГОРОДСКОГО К ОБЩЕЙ ЧИСЛЕННОСТИ НАСЕЛЕНИЯ РАСЧЁТНО)', '4-7urbanization_as_percentage_of_total_population_estimate'],
]

data = []

for i, topic in enumerate(topics_data):
    topic_unit = {
		"model": "macroeconomics.topic",
		"pk": i+1,
		"fields": {
			"name": topic[0],
			"slug": topic[1]
		}
    }
    data.append(topic_unit)

for i, index in enumerate(economic_indices):
    for j, topic in enumerate(topics_data):
        if topic[0] == index[2]:
            i_index = j+1

    index_unit = {
		"model": "macroeconomics.economicindex",
		"pk": i+1,
		"fields": {
			"name": index[0],
			"slug": index[1],
			"macro_topic": i_index
		}
    }
    data.append(index_unit)


for i, table in enumerate(table_info):
    for j, index in enumerate(economic_indices):
        if index[0] == table[0]:
            i_index = j+1
            
    table_unit = {
        "model": "macroeconomics.table",
		"pk": i+1,
        "fields": {
            "excel": f"excels/{table[1]}.xlsx",
			"macro_economic_index": i_index
		}
	}
    data.append(table_unit)

file_name = "macro_data.json"


json_data = json.dumps(data, ensure_ascii=False, indent=2)

with open(file_name, "w", encoding="utf-8") as json_file:
    json_file.write(json_data)

print(f"Данные успешно записаны в файл: {file_name}")