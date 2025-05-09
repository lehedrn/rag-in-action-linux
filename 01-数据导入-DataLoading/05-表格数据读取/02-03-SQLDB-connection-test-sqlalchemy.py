import os
from sqlalchemy import create_engine, text
import pandas as pd

# 确保使用 pymysql 作为驱动
sql_url = f"{os.getenv('SQL_SCHEME')}://{os.getenv('SQL_USER')}:{os.getenv('SQL_PASSWORD')}@{os.getenv('SQL_HOST')}:{os.getenv('SQL_PORT')}/{os.getenv('SQL_DB')}"
print(sql_url)
# engine = create_engine("mysql+pymysql://newuser:password@localhost:3306/example_db")
engine = create_engine(sql_url)

# 测试连接
try:
    with engine.connect() as connection:
        # 使用 text() 函数包装 SQL 语句
        result = connection.execute(text("SELECT * FROM game_scenes"))
        df = pd.DataFrame(result.fetchall(), columns=result.keys())
        print("查询结果：")
        print(df)
except Exception as e:
    print("数据库连接失败:", e)


