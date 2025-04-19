# 导入Document类，用于创建文档对象
from langchain_core.documents import Document 

# 创建文档对象列表，每个文档对象包含文本内容和元数据
documents = [
  Document(
    page_content="悟空是大师兄.",
    metadata={"source": "师徒四人.txt"}
  ),
  Document(
    page_content="八戒是二师兄.",
    metadata={"source": "师徒四人.txt"}
  ),
]

print(documents)