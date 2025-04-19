
from llama_index.core import SimpleDirectoryReader
import os

# 使用 SimpleDirectoryReader加载目录中的文件
# 指定要加载文档的目录
directory_path = '90-文档-Data/黑悟空'

# 使用 SimpleDirectoryReader 加载目录中的文件
documents = SimpleDirectoryReader(directory_path).load_data()

# 打印加载的文档数量
print(f"文档数： {len(documents)} ")
print("-----------------")
if documents:
    print(documents[0].text[:100])  # 打印第一个文档的前100个字符
else:
    print("没有成功加载任何文档")

# 仅加载某一个特定文件
dir_reader = SimpleDirectoryReader(input_files=[os.path.join(directory_path, "黑悟空设定.txt")])
documents = dir_reader.load_data()
print(f"文档数量: {len(documents)}")
print(documents[0].text[:100])  # 打印第一个文档的前100个字符