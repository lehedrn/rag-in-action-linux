import pymysql
from dotenv import load_dotenv
import os

load_dotenv()
try:
    connection = pymysql.connect(
        host=os.getenv("SQL_HOST"),
        user=os.getenv("SQL_USER"),
        password=os.getenv("SQL_PASSWORD"),
        database=os.getenv("SQL_DB"),
        port=3306
    )

    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM game_scenes")
        for row in cursor.fetchall():
            print(row)

    connection.close()

except Exception as e:
    print("数据库连接失败:", e)

