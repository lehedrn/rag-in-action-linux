from langchain_community.document_loaders import CSVLoader

file_path = "90-文档-Data/黑悟空/黑神话悟空.csv"

def get_records(loader, rows_number):
  data = loader.load()
  for record in data[:rows_number]:
      print(record)
      print("-"*100)

# 第 1 部分: 基本加载 CSV 文件并打印记录
def load_csv_basic():
  loader = CSVLoader(
    file_path=file_path
  )
  get_records(loader, 3)

# 第 2 部分: 跳过 CSV 文件的标题行并使用自定义列名
def load_csv_with_custom_column_names():
  loader = CSVLoader(
    file_path=file_path,
    csv_args={
      "delimiter": ",",
      "quotechar": '"',
      "fieldnames": ["种类", "名称", "说明", "等级"],
    }
  )
  get_records(loader, 3)

# # 第 3 部分: 指定 "Name" 列作为 source_column
def load_csv_with_source_column():
  loader = CSVLoader(
    file_path=file_path,
    autodetect_encoding=True,
    source_column="Name",
  )
  get_records(loader, 3)

# 第 4 部分: 使用 UnstructuredCSVLoader 加载 CSV 文件
def load_csv_with_unstructured():
  from langchain_community.document_loaders import UnstructuredCSVLoader
  loader = UnstructuredCSVLoader(
    file_path=file_path,
  )
  get_records(loader, 3)

if __name__ == "__main__":
  load_csv_basic()
  print("*" * 100)
  load_csv_with_custom_column_names()
  print("*" * 100)
  load_csv_with_source_column()
  print("*" * 100)
  load_csv_with_unstructured()