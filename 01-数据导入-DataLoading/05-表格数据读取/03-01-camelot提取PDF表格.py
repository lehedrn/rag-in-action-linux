from datetime import datetime
import os
import camelot
import pandas as pd
# from ctypes.util import find_library
# find_library("gs")

pdf_path = "90-文档-Data/复杂PDF/billionaires_page-1-5.pdf"
import time

start_time = time.time()
tables = camelot.read_pdf(pdf_path, pages="all")
end_time = time.time()
print(f"PDF表格解析耗时: {end_time - start_time:.2f}秒")

output_dir = f"92-图片-Pic/output{datetime.now().strftime('%Y%m%d_%H%M%S')}"

# 1. PDF 转图片
if not os.path.exists(output_dir):
    os.makedirs(output_dir)


# 转换所有表格为 DataFrame
if tables:
    # 遍历所有表格
    for i, table in enumerate(tables, 1):
        # 将表格转换为 DataFrame
        df = table.df
        
        # 打印当前表格数据
        print(f"\n表格 {i} 数据:")
        print(df)
        
        # 显示基本信息
        print(f"\n表格 {i} 基本信息:")
        print(df.info())
        
        # 保存到CSV文件
        csv_filename = os.path.join(output_dir, f"billionaires_table_{i}.csv")
        df.to_csv(csv_filename, index=False)
        print(f"\n表格 {i} 数据已保存到 {csv_filename}")