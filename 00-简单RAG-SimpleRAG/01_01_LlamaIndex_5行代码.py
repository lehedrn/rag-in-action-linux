# 导入 VectorStoreIndex 和 SimpleDirectoryReader 类，用于构建向量存储索引和读取文档
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
# 导入 load_dotenv 函数，用于从.env 文件中加载环境变量
from dotenv import load_dotenv

# 从.env 文件中加载环境变量
load_dotenv()

# 使用 SimpleDirectoryReader 从指定文件中读取文档数据
files = ["90-文档-Data/黑悟空/黑悟空设定.txt"]
documents = SimpleDirectoryReader(input_files=files).load_data()

# 基于读取的文档数据创建向量存储索引
index = VectorStoreIndex.from_documents(documents)

# 将索引转换为查询引擎，以便进行查询操作
query_engine = index.as_query_engine()

# 执行查询操作，询问“黑神话悟空中有哪些战斗工具?”并打印结果
print(query_engine.query("黑神话悟空中有哪些战斗工具?"))