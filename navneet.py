import pandas as pd
import json
import pyodbc

import os
import urllib

# Initialiaze Database Properties
hostname = os.environ.get('hostname', 'mhrijhumber.database.windows.net')
db_server_port = urllib.parse.quote_plus(str(os.environ.get('db_server_port', '8080')))
db_name = os.environ.get('db_name', 'MHIRJ')
db_username = urllib.parse.quote_plus(str(os.environ.get('db_username', 'mhrij')))
db_password = urllib.parse.quote_plus(str(os.environ.get('db_password', 'KaranCool123')))
ssl_mode = urllib.parse.quote_plus(str(os.environ.get('ssl_mode','prefer')))
db_driver = "ODBC Driver 17 for SQL Server"


def insertData(bytes):
    data = bytes.decode('utf-8')
    df = pd.DataFrame(data,)
    # Connect to SQL Server
    conn = pyodbc.connect(driver=db_driver, host=hostname, database=db_name,
                              user=db_username, password=db_password)
    cursor = conn.cursor()

    # Create Table
    cursor.execute('CREATE TABLE people_info (Name1 nvarchar(50), Name2 nvarchar(50), Name3 nvarchar(50))')

    # Insert DataFrame to Table
    for index,row in df.iterrows():
        print(row[0])
        # cursor.execute('''
        #             INSERT INTO dbo.people_info ([Name1], [Name2], [Name3])
        #             VALUES (?,?,?)
        #             ''',
        #             row['0'], 
        #             row['Name2'],
        #             row['Name3']
        #             )
        # conn.commit()
    return {"message":"Success"}

# def parse_csv(df) : 
#     result = df.to_json(orient="records")
#     parsed = json.loads(result)
#     return parsed

    