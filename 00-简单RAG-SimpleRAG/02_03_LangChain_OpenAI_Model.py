import os
from dotenv import load_dotenv

load_dotenv()
os.environ["USER_AGENT"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"

# 1. 加载文档
from langchain_community.document_loaders import WebBaseLoader
loader = WebBaseLoader(
  web_paths=("https://zh.wikipedia.org/wiki/黑神话：悟空",)
)
docs = loader.load()

# 2. 文档分块
from langchain_text_splitters import RecursiveCharacterTextSplitter
text_splitter = RecursiveCharacterTextSplitter(
  # 每个文本块的最大字符数
  chunk_size = 1000,
  # 相邻文本块之间的重叠字符数
  chunk_overlap = 200
)
all_splits = text_splitter.split_documents(docs)

# 3. 设置嵌入模型
from langchain_openai import OpenAIEmbeddings
embeddings = OpenAIEmbeddings()

# 4. 创建向量存储
from langchain_core.vectorstores import InMemoryVectorStore
vector_store = InMemoryVectorStore(embeddings)
vector_store.add_documents(all_splits)

# 5. 构建用户查询
question = "黑悟空有哪些游戏场景？"

# 6. 在向量存储中搜索相关文档，并准备上下文内容
retrieved_docs = vector_store.similarity_search(question, k=3)
print(f"retrieved_docs: {retrieved_docs}")
docs_content = "\n\n".join(doc.page_content for doc in retrieved_docs)
print(f"docs_content: {docs_content}")

# 7. 构建提示模板
from langchain_core.prompts import ChatPromptTemplate
prompt = ChatPromptTemplate.from_template("""
  基于以下上下文，回答问题。如果上下文中没有相关信息，
  请说"我无法从提供的上下文中找到相关信息"。
  上下文: {context}
  问题: {question}
  回答:"""
)

# 8. 使用大语言模型生成答案
from langchain_openai import ChatOpenAI
# llm = ChatOpenAI(model="gpt-3.5-turbo", api_key=os.getenv("OEPNAI_API_KEY"))
llm = ChatOpenAI(model="gpt-4o")
answer = llm.invoke(prompt.format(question=question, context=docs_content))

print(f"answer: {answer.content}")