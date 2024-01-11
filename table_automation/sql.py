cons_index_sql = """
SELECT 
    activity_type, 
    value, 
    description, 
    created_at
FROM 
    consumer_price_index_month 
WHERE 
    region = 'РЕСПУБЛИКА КАЗАХСТАН' 
    AND periods_correlation = %s
    AND activity_type IN %s
    AND created_at BETWEEN %s AND %s
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
    AND periods_correlation = %s 
    AND countries = 'Всего'
    AND activity_type = 'Промышленность'
    AND industrial_products_list = 'Всего'
    AND created_at BETWEEN %s AND %s;
"""


avsalary_byactivity_sql = '''
SELECT 
    activity_type,
    value,
    description,
    created_at
FROM 
    avmon_nom_wages_year 
WHERE 
    region = 'РЕСПУБЛИКА КАЗАХСТАН' 
    AND activity_type IN %s
    AND area_type = 'Всего' 
    AND enterprise_dimension = 'Всего' 
    AND gender = 'Всего' 
    AND created_at BETWEEN %s AND %s
UNION
SELECT 
    activity_type, 
    value, 
    description, 
    created_at 
FROM
    avmon_nom_wages_quarter 
WHERE 
    region = 'РЕСПУБЛИКА КАЗАХСТАН' AND activity_type IN %s
    AND economic_sectors = 'Экономика в целом'
    AND created_at BETWEEN %s AND %s;
'''

nominal_wage_index_sql = '''
SELECT
    activity_type,
    value,
    description,
    created_at
FROM
    nom_wages_index_year
WHERE
    region = 'РЕСПУБЛИКА КАЗАХСТАН'
    AND activity_type IN %s
    AND enterprise_dimension = 'Всего'
    AND gender = 'Всего'
    AND periods_correlation = 'отчетный период к предыдущему периоду'
    AND created_at BETWEEN %s AND %s
UNION
SELECT
    activity_type,
    value,
    description,
    created_at
FROM
    nom_wages_index_quarter
WHERE
    region = 'РЕСПУБЛИКА КАЗАХСТАН'
    AND activity_type IN %s
    AND enterprise_dimension = 'Всего'
    AND periods_correlation = 'отчетный период к соответствующему периоду прошлого года'
    AND created_at BETWEEN %s AND %s;
'''

real_wage_index_sql = '''
SELECT
    activity_type,
    value,
    description,
    created_at
FROM
    real_wages_index_year
WHERE
    region = 'РЕСПУБЛИКА КАЗАХСТАН'
    AND activity_type IN %s
    AND enterprise_dimension = 'Всего'
    AND gender = 'Всего'
    AND periods_correlation = 'отчетный период к предыдущему периоду'
    AND created_at BETWEEN %s AND %s
UNION
SELECT
    activity_type,
    value,
    description,
    created_at
FROM
    real_wages_index_quarter
WHERE
    region = 'РЕСПУБЛИКА КАЗАХСТАН'
    AND activity_type IN %s
    AND enterprise_dimension = 'Всего'
    AND periods_correlation = 'отчетный период к соответствующему периоду прошлого года'
    AND created_at BETWEEN %s AND %s;
'''

avnomsalary_by_region_sql = '''
SELECT 
    region,
    value,
    description,
    created_at
FROM 
    avmon_nom_wages_year 
WHERE 
    activity_type = 'Всего' 
    AND region IN %s
    AND area_type = 'Всего' 
    AND enterprise_dimension = 'Всего' 
    AND gender = 'Всего' 
    AND created_at BETWEEN %s AND %s
UNION
SELECT 
    region, 
    value, 
    description, 
    created_at 
FROM
    avmon_nom_wages_quarter 
WHERE 
    activity_type = 'Всего' AND region IN %s
    AND economic_sectors = 'Экономика в целом'
    AND created_at BETWEEN %s AND %s;
'''

nomwage_index_by_region_sql = '''
    SELECT
        region,
        value,
        description,
        created_at
    FROM
        nom_wages_index_year
    WHERE
        activity_type = 'Всего'
        AND region IN %s
        AND enterprise_dimension = 'Всего'
        AND gender = 'Всего'
        AND periods_correlation = 'отчетный период к предыдущему периоду'
        AND created_at BETWEEN %s AND %s
    UNION
    SELECT
        region,
        value,
        description,
        created_at
    FROM
        nom_wages_index_quarter
    WHERE
        activity_type = 'Всего'
        AND region IN %s
        AND enterprise_dimension = 'Всего'
        AND periods_correlation = 'отчетный период к соответствующему периоду прошлого года'
        AND created_at BETWEEN %s AND %s;
'''


realwage_index_by_region_sql = '''
SELECT
    region,
    value,
    description,
    created_at
FROM
    real_wages_index_year
WHERE
    activity_type = 'Всего'
    AND region IN %s
    AND enterprise_dimension = 'Всего'
    AND gender = 'Всего'
    AND periods_correlation = 'отчетный период к предыдущему периоду'
    AND created_at BETWEEN %s AND %s
UNION
SELECT
    region,
    value,
    description,
    created_at
FROM
    real_wages_index_quarter
WHERE
    activity_type = 'Всего'
    AND region IN %s
    AND enterprise_dimension = 'Всего'
    AND periods_correlation = 'отчетный период к соответствующему периоду прошлого года'
    AND created_at BETWEEN %s AND %s;
'''

#2.8
avcapita_nominal_income_by_region_sql = '''
SELECT 
    region, 
    value, 
    description, 
    created_at 
FROM 
    avcap_pop_nom_income_year
WHERE
    region IN %s
    AND created_at BETWEEN %s AND %s
UNION
SELECT
    region, 
    value, 
    description, 
    created_at 
FROM
    avcap_pop_nom_income_quarter
WHERE
    region IN %s
    AND created_at BETWEEN %s AND %s;
'''

#2.9
nominal_income_index_by_region_sql = '''
SELECT
    region,
    value,
    description,
    created_at
FROM
    nom_income_index_year
WHERE
    region IN %s
    AND created_at BETWEEN %s AND %s
UNION
SELECT
    region,
    value,
    description,
    created_at
FROM
    nom_income_index_quarter
WHERE
    region IN %s
    AND created_at BETWEEN %s AND %s;
'''

#2.10
real_income_index_by_region_sql = '''
SELECT
    region,
    value,
    description,
    created_at
FROM
    real_income_index_year
WHERE
    region IN %s
    AND created_at BETWEEN %s AND %s
UNION
SELECT
    region,
    value,
    description,
    created_at
FROM
    real_income_index_quarter
WHERE
    region IN %s
    AND created_at BETWEEN %s AND %s;
'''

#2.11
population_share_below_poverty_line_sql = '''
SELECT
    region,
    value,
    description,
    created_at
FROM 
    pop_income_below_subsistence_year
WHERE
    region IN %s
    AND area_type = 'Всего'
    AND created_at BETWEEN %s AND %s
UNION
SELECT
    region,
    value,
    description,
    created_at
FROM 
    pop_income_below_subsistence_quarter
WHERE
    region IN %s
    AND area_type = 'Всего'
    AND created_at BETWEEN %s AND %s;
'''

#2.1
labor_stats_sql = '''
SELECT 	
    'Рабочая сила', 
    value, 
    description, 
    created_at  
FROM 
    work_force_year
WHERE
    region = 'РЕСПУБЛИКА КАЗАХСТАН'
    AND area_type = 'Всего'
    AND gender = 'Всего'
    AND education_level = 'Всего'
    AND age_intervals = 'Всего'
    AND created_at BETWEEN %s AND %s
UNION
SELECT         
    'Занятость', 
    value, 
    description, 
    created_at 
FROM 
    labor_statistics_year
WHERE
    region = 'РЕСПУБЛИКА КАЗАХСТАН'
    AND activity_type = 'Всего'
    AND area_type = 'Всего'
    AND gender = 'Всего'
    AND education_level = 'Всего'
    AND age_intervals = 'Всего'
    AND created_at BETWEEN %s AND %s
UNION
SELECT         
    activity_type, 
    value, 
    description, 
    created_at 
FROM 
    labor_statistics_year
WHERE
    region = 'РЕСПУБЛИКА КАЗАХСТАН'
    AND activity_type IN %s
    AND area_type = 'Всего'
    AND gender = 'Всего'
    AND education_level = 'Всего'
    AND age_intervals = 'Всего'
    AND created_at BETWEEN %s AND %s
UNION
SELECT 	
    'Наемные работники', 
    value, 
    description, 
    created_at  
FROM 
    wage_earners_year 
WHERE 	
    region = 'РЕСПУБЛИКА КАЗАХСТАН'
    AND activity_type = 'Всего'
    AND area_type = 'Всего'
    AND gender = 'Всего'
    AND education_level = 'Всего'
    AND age_intervals = 'Всего'
    AND created_at BETWEEN %s AND %s
UNION
SELECT         
    'Самозанятые', 
    value, 
    description, 
    created_at  
FROM 
    self_employed_year
WHERE
    region = 'РЕСПУБЛИКА КАЗАХСТАН'
    AND activity_type = 'Всего'
    AND area_type = 'Всего'
    AND gender = 'Всего'
    AND education_level = 'Всего'
    AND age_intervals = 'Всего'
    AND created_at BETWEEN %s AND %s
UNION
SELECT 	
    'Численность безработных', 
    value, 
    description, 
    created_at  
FROM 
    unemployed_number_year 
WHERE 	
    region = 'РЕСПУБЛИКА КАЗАХСТАН'
    AND area_type = 'Всего'
    AND gender = 'Всего'
    AND education_level = 'Всего'
    AND age_intervals = 'Всего'
    AND created_at BETWEEN %s AND %s
UNION
SELECT 	
    'Уровень безработицы', 
    value, 
    description, 
    created_at  
FROM 
    unemployment_rate_year 
WHERE 	
    region = 'РЕСПУБЛИКА КАЗАХСТАН'
    AND area_type = 'Всего'
    AND gender = 'Всего'
    AND education_level = 'Всего'
    AND age_intervals = 'Всего'
    AND created_at BETWEEN %s AND %s
UNION
SELECT 
    'Средняя заработная плата',     
    value, 
    description, 
    created_at  
FROM 
    average_wages_year
WHERE
    region = 'РЕСПУБЛИКА КАЗАХСТАН'
    AND activity_type = 'Всего'
    AND area_type = 'Всего'
    AND enterprise_dimension = 'Всего'
    AND gender = 'Всего'
    AND created_at BETWEEN %s AND %s
UNION
SELECT 	
    'Рабочая сила', 
    value, 
    description, 
    created_at  
FROM 
    work_force_quarter
WHERE
    region = 'РЕСПУБЛИКА КАЗАХСТАН'
    AND area_type = 'Всего'
    AND gender = 'Всего'
    AND education_level = 'Всего'
    AND age_intervals = 'Всего'
    AND created_at BETWEEN %s AND %s
UNION
SELECT         
    'Занятость', 
    value, 
    description, 
    created_at 
FROM 
    labor_statistics_quarter
WHERE
    region = 'РЕСПУБЛИКА КАЗАХСТАН'
    AND activity_type = 'Всего'
    AND area_type = 'Всего'
    AND gender = 'Всего'
    AND education_level = 'Всего'
    AND age_intervals = 'Всего'
    AND created_at BETWEEN %s AND %s
UNION
SELECT         
    activity_type, 
    value, 
    description, 
    created_at 
FROM 
    labor_statistics_quarter
WHERE
    region = 'РЕСПУБЛИКА КАЗАХСТАН'
    AND activity_type IN %s
    AND area_type = 'Всего'
    AND gender = 'Всего'
    AND education_level = 'Всего'
    AND age_intervals = 'Всего'
    AND created_at BETWEEN %s AND %s
UNION
SELECT 	
    'Наемные работники', 
    value, 
    description, 
    created_at  
FROM 
    wage_earners_quarter
WHERE 	
    region = 'РЕСПУБЛИКА КАЗАХСТАН'
    AND activity_type = 'Всего'
    AND area_type = 'Всего'
    AND gender = 'Всего'
    AND education_level = 'Всего'
    AND age_intervals = 'Всего'
    AND created_at BETWEEN %s AND %s
UNION
SELECT         
    'Самозанятые', 
    value, 
    description, 
    created_at  
FROM 
    self_employed_quarter
WHERE
    region = 'РЕСПУБЛИКА КАЗАХСТАН'
    AND activity_type = 'Всего'
    AND area_type = 'Всего'
    AND gender = 'Всего'
    AND education_level = 'Всего'
    AND age_intervals = 'Всего'
    AND created_at BETWEEN %s AND %s
UNION
SELECT 	
    'Численность безработных', 
    value, 
    description, 
    created_at  
FROM 
    unemployed_number_quarter 
WHERE 	
    region = 'РЕСПУБЛИКА КАЗАХСТАН'
    AND area_type = 'Всего'
    AND gender = 'Всего'
    AND education_level = 'Всего'
    AND age_intervals = 'Всего'
    AND created_at BETWEEN %s AND %s
UNION
SELECT 
    'Средняя заработная плата',     
    value, 
    description, 
    created_at  
FROM 
    average_wages_quarter
WHERE
    region = 'РЕСПУБЛИКА КАЗАХСТАН'
    AND activity_type = 'Всего'
    AND economic_sectors = 'Экономика в целом'
    AND created_at BETWEEN %s AND %s
ORDER BY 
    created_at;
'''

# 4.2
gdp_by_one_sql = '''
SELECT
	region,
	value,
	description,
	created_at
FROM 
	grp_per_capita_year
WHERE
	region IN %s
	AND created_at BETWEEN %s AND %s
UNION
SELECT
	region,
	value,
	description,
	created_at
FROM
	grp_per_capita_quarter_accum
WHERE
	region IN %s
	AND created_at BETWEEN %s AND %s
'''

# 4.3
gdp_agricultural_sql = '''
SELECT
	region,
	value,
	description,
	created_at
FROM 
	gop_agriculture_forest_fish_year
WHERE
	region IN %s
	AND price_measurement = 'В действующих ценах'
	AND created_at BETWEEN %s AND %s
UNION
SELECT
	region,
	value,
	description,
	created_at
FROM
	gop_agriculture_forest_fish_month_accum
WHERE
	region IN %s
	AND price_measurement = 'В действующих ценах'
	AND household_category = 'Все категории хозяйств'
	AND created_at BETWEEN %s AND %s;
'''

# 4.4
ind_production_volume_sql = '''
SELECT
	region,
	value,
	description,
	created_at
FROM 
	industrial_production_volumes_year
WHERE
	region IN %s
	AND activity_type = 'Промышленность'
	AND created_at BETWEEN %s AND %s
UNION
SELECT
	region,
	value,
	description,
	created_at
FROM
	industrial_production_volumes_month_accum
WHERE
	region IN %s
	AND area_type = 'Всего'
	AND activity_type = 'Промышленность'
	AND periods_correlation = 'За отчетный период'
	AND created_at BETWEEN %s AND %s;
'''

# 4.5
pop_at_beginning_year_sql = '''
SELECT 
	region,
	area_type,
	value,
	description,
	created_at
FROM
	population_of_kazakhstan_year
WHERE
	region IN %s
	AND gender = 'Всего'
	AND age_groups = 'Всего'
	AND created_at BETWEEN %s AND %s
UNION
SELECT 
	region,
	area_type,
	value,
	description,
	created_at
FROM
	population_of_kazakhstan_month
WHERE
	region IN %s
	AND created_at BETWEEN %s AND %s
ORDER BY 
	created_at;
'''

# 4.6
pop_at_beginning_year2_sql = '''
SELECT
	region,
	gender,
	population_group,
	value,
	description,
	created_at
FROM
	population_year_beginning_year
WHERE
	region IN %s
	AND area_type = 'Всего'
	AND created_at BETWEEN %s AND %s
ORDER BY 
	created_at;
'''

# 4.1
reg_gros_phys_vol_sql = '''
SELECT 
	region, 
    'percent',
	value,
	description,
	created_at
FROM 
	grp_volume_index_year
WHERE 
	region IN %s
AND created_at BETWEEN %s AND %s
UNION
SELECT 
	region, 
    'tenge',
	value,
	description,
	created_at
FROM 
	grp_year
WHERE 
	region IN %s
AND created_at BETWEEN %s AND %s
UNION
SELECT 
	region, 
    'percent',
	value,
	description,
	created_at
FROM 
	grp_volume_index_quarter_accum
WHERE 
	region IN %s
AND created_at BETWEEN %s AND %s
UNION
SELECT 
	region, 
    'tenge',
	value,
	description,
	created_at
FROM 
	grp_quarter_accum
WHERE 
	region IN %s
AND created_at BETWEEN %s AND %s
ORDER BY
	created_at;
'''

# 3.2
sector_spec_msp_sql = '''
SELECT 
	'ПРОМЫШЛЕННОСТЬ' AS activity,
	enterprise_dimension,
	SUM(value),
	description,
	created_at
FROM
	industry_specialization_sme_year
WHERE
	region = 'РЕСПУБЛИКА КАЗАХСТАН'
	AND activity_type IN %s
	AND enterprise_dimension != 'Всего'
	AND created_at BETWEEN %s AND %s
GROUP BY
	enterprise_dimension, description, created_at
UNION
SELECT 
	'УСЛУГИ' AS activity,
	enterprise_dimension,
	SUM(value),
	description,
	created_at
FROM
	industry_specialization_sme_year
WHERE
	region = 'РЕСПУБЛИКА КАЗАХСТАН'
	AND activity_type IN %s
	AND enterprise_dimension != 'Всего'
	AND created_at BETWEEN %s AND %s
GROUP BY
	enterprise_dimension, description, created_at
UNION
SELECT 
	activity_type  AS activity,
	enterprise_dimension,
	value,
	description,
	created_at
FROM
	industry_specialization_sme_year
WHERE
	region = 'РЕСПУБЛИКА КАЗАХСТАН'
	AND activity_type IN %s
	AND enterprise_dimension != 'Всего'
	AND created_at BETWEEN %s AND %s
ORDER BY 
    created_at;
'''

# 1.3
labor_productivity_sql = '''
SELECT 
	'Производительность труда' AS activity_type, 
	'tenge', 
	value, 
	description, 
	created_at 
FROM 
	labor_productivity_ind_quarter_accum 
WHERE 
	region = 'РЕСПУБЛИКА КАЗАХСТАН' 
	AND created_at BETWEEN %s AND %s
UNION
SELECT 
	'Производительность труда' AS activity_type, 
	'percent', 
	value, 
	description, 
	created_at 
FROM 
	labor_productivity_ind_indeces_quarter_accum 
WHERE 
	region = 'РЕСПУБЛИКА КАЗАХСТАН' 
	AND created_at BETWEEN %s AND %s
UNION
SELECT 
	activity_type, 
	'tenge', 
	value, 
	description, 
	created_at 
FROM 
	labor_productivity_quarter_accum 
WHERE 
	region = 'РЕСПУБЛИКА КАЗАХСТАН' 
	AND activity_type IN %s
	AND created_at BETWEEN %s AND %s
UNION
SELECT 
	activity_type, 
	'percent', 
	value, 
	description, 
	created_at 
FROM 
	labor_productivity_indeces_quarter_accum 
WHERE 
	region = 'РЕСПУБЛИКА КАЗАХСТАН' 
	AND activity_type IN %s
	AND created_at BETWEEN %s AND %s
ORDER BY 
	created_at;
'''

# 1.4
capital_investment_sql = '''
SELECT 
	activity_type, 
	'tenge', 
	value, 
	description, 
	created_at 
FROM 
	fixed_capital_investment_month_accum 
WHERE 
	region = 'РЕСПУБЛИКА КАЗАХСТАН' 
	AND activity_type IN %s
	AND branch_size = 'Всего' 
	AND funding_source = 'Всего' 
	AND created_at BETWEEN %s AND %s
UNION
SELECT 
	activity_type, 
	'percent', 
	value, 
	description, 
	created_at 
FROM 
	fixed_capital_investment_indeces_month_accum
WHERE 
	region = 'РЕСПУБЛИКА КАЗАХСТАН' 
	AND activity_type IN %s
	AND area_type = 'Всего' 
	AND periods_corellation = 'отчетный период к соответствующему периоду прошлого года' 
	AND created_at BETWEEN %s AND %s
ORDER BY 
	 created_at;
'''

# 1.4 2
capital_investment_by_funding_sql = '''
SELECT 
	funding_source, 
	value, 
	description, 
	created_at 
FROM 
	fixed_capital_investment_month_accum 
WHERE 
	region = 'РЕСПУБЛИКА КАЗАХСТАН' 
	AND activity_type = 'Всего'
	AND branch_size = 'Всего' 
	AND funding_source IN %s 
	AND created_at BETWEEN %s AND %s
UNION
SELECT 
	'Бюджетные средства',  
	SUM(value), 
	description, 
	created_at 
FROM 
	fixed_capital_investment_month_accum 
WHERE 
	region = 'РЕСПУБЛИКА КАЗАХСТАН' 
	AND activity_type = 'Всего'
	AND branch_size = 'Всего' 
	AND funding_source IN ('Республиканский бюджет ', 'Местный бюджет') 
	AND created_at BETWEEN %s AND %s
GROUP BY
	description,
	created_at
UNION
SELECT 
	'Сумма', 
	value, 
	description, 
	created_at 
FROM 
	fixed_capital_investment_month_accum 
WHERE 
	region = 'РЕСПУБЛИКА КАЗАХСТАН' 
	AND activity_type = 'Всего'
	AND branch_size = 'Всего' 
	AND funding_source  = 'Всего' 
	AND created_at BETWEEN %s AND %s
ORDER BY 
	 created_at;
'''

# 1.2
ppi_sql = '''
SELECT
	'ИФО', 
	value, 
	description, 
	created_at 
FROM 
	physical_volume_index_year 
WHERE 
	region = 'РЕСПУБЛИКА КАЗАХСТАН' 
	AND created_at BETWEEN %s AND %s
UNION
SELECT 
	activity_type, 
	value, 
	description, 
	created_at 
FROM 
	physical_volume_index_industry_year 
WHERE 
	region = 'РЕСПУБЛИКА КАЗАХСТАН' 
	AND activity_type IN %s
	AND periods_corellation = 'отчетный период к предыдущему периоду' 
	AND created_at BETWEEN %s AND %s
UNION
SELECT 
	'растениеводство', 
	value, 
	description, 
	created_at 
FROM 
	physical_volume_index_crop_year 
WHERE 
	region = 'РЕСПУБЛИКА КАЗАХСТАН' 
	AND agriculture_type = 'Все категории хозяйств' 
	AND periods_corellation = 'отчетный период к соответствующему периоду прошлого года' 
	AND created_at BETWEEN %s AND %s
UNION
SELECT 
	'зерна', 
	value/1000000000, 
	description, 
	created_at 
FROM 
	physical_volume_index_grains_year 
WHERE 
	region = 'РЕСПУБЛИКА КАЗАХСТАН' 
	AND soil_type = 'Всего' 
	AND agriculture_type = 'Все категории хозяйств' 
	AND crop_type = 'Зерновые (включая рис) и бобовые культуры' 
	AND created_at BETWEEN %s AND %s
UNION
SELECT 
	'зерна', 
	value/1000000000, 
	description, 
	created_at 
FROM 
	physical_volume_index_grains_year_once 
WHERE 
	region = 'РЕСПУБЛИКА КАЗАХСТАН' 
	AND soil_type = 'Всего' 
	AND agriculture_type = 'Все категории хозяйств' 
	AND crop_type = 'Зерновые (включая рис) и бобовые культуры' 
	AND created_at BETWEEN %s AND %s
UNION
SELECT 
	'животноводство', 
	value, 
	description, 
	created_at 
FROM 
	physical_volume_index_livestock_year 
WHERE 
	region = 'РЕСПУБЛИКА КАЗАХСТАН' 
	AND activity_type = 'Животноводство' 
	AND agriculture_type = 'Все категории хозяйств' 
	AND periods_corellation = 'отчетный период к соответствующему периоду прошлого года' 
	AND created_at BETWEEN %s AND %s
UNION
SELECT 
	'жилье квадрат', 
	ROUND(value/1000, 0), 
	description, 
	created_at 
FROM 
	physical_volume_index_housing_th_month_accum 
WHERE 
	region = 'РЕСПУБЛИКА КАЗАХСТАН' 
	AND area_type = 'Всего' 
	AND property_type = 'Всего' 
	AND units_type = 'Всего' 
	AND facility_type = 'Всего' 
	AND created_at BETWEEN %s AND %s
UNION
SELECT 
	'жилье процент', 
	value, 
	description, 
	created_at 
FROM 
	physical_volume_index_housing_pr_month_accum 
WHERE 
	region = 'РЕСПУБЛИКА КАЗАХСТАН' 
	AND area_type = 'Всего'
	AND periods_corellation = 'отчетный период к соответствующему периоду прошлого года' 
	AND facility_type = 'Жилые здания' 
	AND created_at BETWEEN %s AND %s
UNION
SELECT 
	activity_type, 
	value, 
	description, 
	created_at 
FROM 
	physical_volume_index_activity_year 
WHERE 
	region = 'РЕСПУБЛИКА КАЗАХСТАН' 
	AND activity_type IN %s
	AND created_at BETWEEN %s AND %s
UNION
SELECT 
	'оптовая торговля', 
	value, 
	description, 
	created_at 
FROM 
	physical_volume_index_opt_month_accum 
WHERE 
	region = 'РЕСПУБЛИКА КАЗАХСТАН' 
	AND selling_type = 'Всего' 
	AND periods_corellation = 'отчетный период к соответствующему периоду прошлого года' 
	AND created_at BETWEEN %s AND %s
UNION 
SELECT 
    'розничная торговля', 
    value, 
    description, 
    created_at 
FROM 
    physical_volume_index_roz_month_accum 
WHERE 
    region = 'РЕСПУБЛИКА КАЗАХСТАН' 
    AND area_type = 'Всего' 
    AND periods_corellation = 'отчетный период к соответствующему периоду прошлого года' 
    AND product_structure = 'Всего' 
    AND created_at BETWEEN %s AND %s
UNION
SELECT 
	'ИФО', 
	value, 
	description, 
	created_at 
FROM 
	physical_volume_index_quarter_accum 
WHERE 
	region = 'РЕСПУБЛИКА КАЗАХСТАН' 
	AND created_at BETWEEN %s AND %s
UNION
SELECT 
	activity_type, 
	value, 
	description, 
	created_at 
FROM 
	physical_volume_index_industry_month_accum 
WHERE 
	region = 'РЕСПУБЛИКА КАЗАХСТАН' 
	AND activity_type IN %s
	AND periods_corellation = 'отчетный период к соответствующему периоду прошлого года' 
	AND created_at BETWEEN %s AND %s
UNION
SELECT 
	'растениеводство', 
	value, 
	description, 
	created_at 
FROM 
	physical_volume_index_crop_month_accum 
WHERE 
	region = 'РЕСПУБЛИКА КАЗАХСТАН' 
	AND agriculture_type = 'Все категории хозяйств' 
	AND periods_corellation = 'отчетный период к соответствующему периоду прошлого года' 
	AND created_at BETWEEN %s AND %s
UNION
SELECT 
	'животноводство', 
	value, 
	description, 
	created_at 
FROM 
	physical_volume_index_livestock_month_accum 
WHERE 
	region = 'РЕСПУБЛИКА КАЗАХСТАН' 
	AND agriculture_type = 'Все категории хозяйств' 
	AND periods_corellation = 'отчетный период к соответствующему периоду прошлого года' 
	AND created_at BETWEEN %s AND %s
UNION
SELECT 
	activity_type, 
	value, 
	description, 
	created_at 
FROM 
	physical_volume_index_activity_quarter_accum 
WHERE 
	region = 'РЕСПУБЛИКА КАЗАХСТАН' 
	AND activity_type IN %s 
	AND created_at BETWEEN %s AND %s
ORDER BY
	created_at;
'''