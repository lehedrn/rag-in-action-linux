# 需要LLAMA_CLOUD_API_KEY
import os
from dotenv import load_dotenv
import openai
load_dotenv()   
# LlamaParse PDF reader for PDF Parsing
from llama_parse import LlamaParse
documents = LlamaParse(
  api_key=os.getenv("LLAMA_INDEX_API_KEY"),
  result_type="markdown").load_data(
    "90-文档-Data/黑悟空/黑神话悟空.pdf"
)
print(documents)

from llama_index.core.node_parser import MarkdownElementNodeParser
# 设置 OpenAI API 密钥，从环境变量中获取
node_parser = MarkdownElementNodeParser()
nodes = node_parser.get_nodes_from_documents(documents)

print(nodes)
