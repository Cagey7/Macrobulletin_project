from datetime import datetime
import time
import os
import psycopg2
import requests
from time import sleep


class Automation:
    def __init__(self, database, user=None, password=None, host=None, port=5432, create_logs=False):
        self.host = host
        self.port = port
        self.database = database
        self.user = user
        self.password = password
        self.create_logs = create_logs
        self.conn = None
        self.cur = None

        if self.create_logs:
            current_directory = os.path.abspath(os.getcwd())
            parent_directory = os.path.dirname(current_directory)
            current_datetime = datetime.now()
            formatted_date = current_datetime.strftime('%Y-%m-%d_%H-%M-%S')
            self.log_path = os.path.join(parent_directory, "logs", f"logs-{formatted_date}.log")

    def write_logs(self, msg, error_type):
        with open(self.log_path, "a") as file:
            current_datetime = datetime.now()
            formatted_datetime = current_datetime.strftime('%m/%d %H:%M:%S')
            
            if error_type == "INFO":
                file.write(f"{formatted_datetime}  {error_type}     :{msg}\n")
            elif error_type == "ERROR":
                file.write(f"{formatted_datetime}  {error_type}    :{msg}\n")
            elif error_type == "WARRING":
                file.write(f"{formatted_datetime}  {error_type}  :{msg}\n")
            
    def db_connection(self):
        if self.conn is None:
            try:
                self.conn = psycopg2.connect(
                    host=self.host,
                    port=self.port,
                    database=self.database,
                    user=self.user,
                    password=self.password
                )
                if self.create_logs:
                    self.write_logs("Подключено к базе данных.", "INFO")
                print("Подключено к базе данных.")
                self.cur = self.conn.cursor()
            except psycopg2.Error as e:
                if self.create_logs:
                    self.write_logs(f"Ошибка во время подключения: , {e}", "ERROR")
                print("Ошибка во время подключения: ", e)
        else:
            if self.create_logs:
                self.write_logs("Уже подлючено к базе данных.", "INFO")
            print("Уже подлючено к базе данных.")


    def get_response(self, url):
        response = requests.get(url)
        if response.status_code == 200:
            return response
        else:
            if self.create_logs:
                self.write_logs(f"Ошибка запроса: {response.status_code}", "ERROR")
            print(f"Ошибка запроса: {response.status_code}")
            sleep(5)
            return self.get_response(url)
    

    def get_latest_updated_date(self, table_name):
        self.cur.execute("SELECT MAX(updated_at) FROM {};".format(table_name))
        latest_date = self.cur.fetchone()[0]
        return latest_date if latest_date else datetime.strptime("1.1.1970", "%d.%m.%Y").date()


    def insert_data(self, table_name, index_name, index_period, url, *fields):
        start_time = time.time()
        try:
            response = self.get_response(url).json()
        except Exception as e:
            if self.create_logs:
                self.write_logs(f"Возникла ошибка при получении json: {e}", "ERROR")
                self.write_logs(f"{index_name} {index_period} требует повторной загрузки", "WARRING")
            print("Произошла ошибка:", str(e))
            print("Возникла ошибка при получении json")

        try:
            if self.create_logs:
                self.write_logs(f"Началась загрузка: {index_name}", "INFO")
            full_table_name = f"{table_name}_{index_period}"
            values_for_table = ""
            field_names = ""
            insert_values = ""
            for field in fields:
                field_names += f"{field},"

                if field == "created_at":
                    insert_values += "TO_DATE(%s, 'DD.MM.YYYY'),"
                else:
                    insert_values += "%s,"
                
                if field == "created_at":
                    values_for_table += f"{field} DATE,"
                elif field == "value":
                    values_for_table += f"{field} NUMERIC,"
                else:
                    values_for_table += f"{field} VARCHAR,"
            

            table = f"""
            CREATE TABLE IF NOT EXISTS {full_table_name} (
                id SERIAL PRIMARY KEY,
                {values_for_table}
                updated_at DATE
            );
            """
            self.cur.execute(table)
            insert_query = f"""
            INSERT INTO {full_table_name} ({field_names} updated_at) VALUES ({insert_values} CURRENT_DATE);
            """

            latest_date = self.get_latest_updated_date(full_table_name)

            insert_data = []

            for row in response:
                unit_data = []
                for period in row["periods"]:
                    if period["value"] == "x":
                        period["value"] = -1
                    date_object = datetime.strptime(period["date"], "%d.%m.%Y").date()
                    if date_object > latest_date:
                        unit_data = tuple(row["termNames"]) + (period["date"], period["value"], period["name"])
                        insert_data.append(unit_data)
            self.cur.executemany(insert_query, insert_data)
            
            self.conn.commit()
            end_time = time.time()
            if self.create_logs:
                self.write_logs(f"{index_name} загружен за {index_period} за {end_time - start_time:.2f} секунд.", "INFO")
            print(f"{index_name} загружен за {index_period} за {end_time - start_time:.2f} секунд.")
        except Exception as e:
            self.conn.rollback()
            if self.create_logs:
                self.write_logs(f"Возникла ошибка при загрузке данных: {e}", "ERROR")
            print("Произошла ошибка:", str(e))
            print("Возникла ошибка при загрузке данных")

    def db_disconnect(self):
        if self.conn is not None:
            self.conn.close()
            self.conn = None
            self.cur = None
            if self.create_logs:
                self.write_logs("Отключено от базы данных", "INFO")
            print("Отключено от базы данных.")
        else:
            if self.create_logs:
                self.write_logs("Уже отключено от базы данных.", "INFO")
            print("Уже отключено от базы данных.")
