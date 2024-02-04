from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np
from datetime import datetime
# import sqlite3


def extract(url_page, table_attributes):
    print('Initializing extract Process... \n')
    page = requests.get(url_page).text
    data = BeautifulSoup(page, 'html.parser')
    df = pd.DataFrame(columns=table_attributes)
    tables = data.findAll('tbody')
    rows = tables[2].find_all('tr')

    for row in rows:
        col = row.find_all('td')
        if len(col) != 0:
            if col[0].find('a') is not None and '—' not in col[2]:
                data_dict = {"Country": col[0].a.contents[0],
                             "GDP_USD_millions": col[2].contents[0]}
                df1 = pd.DataFrame(data_dict, index=[0])
                df = pd.concat([df, df1], ignore_index=True)
    return df


def transform(df):
    print("Initializing transform process... \n")
    gdp_list = df["GDP_USD_millions"].tolist()
    gdp_list = [float("".join(x.split(','))) for x in gdp_list]
    gdp_list = [np.round(x/1000, 2) for x in gdp_list]
    df["GDP_USD_millions"] = gdp_list
    df = df.rename(columns={"GDP_USD_millions": "GDP_USD_billions"})
    return df


def load_to_csv(df, csv_file):
    print("Initializing loading to CSV process...")
    df.to_csv(csv_file)
    print("Data saved to CSV file \n")


def load_to_db(df, sql_connection, table):
    print("SQL Connection initiated")
    df.to_sql(table, sql_connection, if_exists='replace', index=False)
    print("Data loaded to database as table. \n")


def run_query(query_statement, sql_connection):
    print("Running the query...")
    print(query_statement)
    query_output = pd.read_sql(query_statement, sql_connection)
    print(query_output + "\n")


def log_progress(message):
    timestamp_format = '%Y-%h-%d-%H:%M:%S'  # Year-Monthname-Day-Hour-Minute-Second
    now = datetime.now()
    timestamp = now.strftime(timestamp_format)
    with open("./etl_project_log.txt", "a") as f:
        f.write(timestamp + ' : ' + message + "\n")


url = 'https://web.archive.org/web/20230902185326/https://en.wikipedia.org/wiki/List_of_countries_by_GDP_%28nominal%29'
table_attribs = ["Country", "GDP_USD_millions"]
db_name = 'World_Economies.db'
table_name = "Countries_by_GDP"
csv_path = "./Countries_by_GDP.csv"


log_progress("Initializing ETL Process...")
dataframe = extract(url, table_attribs)

log_progress("Data Extraction complete. Initializing transform process...")
dataframe = transform(dataframe)

log_progress("Data Transformation complete. Initializing loading process...")
load_to_csv(dataframe, csv_path)

log_progress("Data saved to CSV file")

# sql_connection = sqlite3.connect("World_economies.db")
# log_progress("SQL Connection initiated")
# load_to_db(df, sql_connection, table_name)

# log_progress("Data loaded to database as table. Running the query...")
# query_statement = f"SELECT * from {table_name} WHERE GDP_USD_billions >= 100"
# run_query(query_statement, sql_connection)

log_progress("Process complete!")
# sql_connection.close()
print('Process complete!')
