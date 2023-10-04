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