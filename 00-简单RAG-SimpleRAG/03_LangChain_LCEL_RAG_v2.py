import os
from dotenv import load_dotenv

load_dotenv()
os.environ["USER_AGENT"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"

# 1.加载文档
from langchain_community.document_loaders import WebBaseLoader

loader = WebBaseLoader(
  # 要加载的网页URL
  web_paths=("https://zh.wikipedia.org/wiki/黑神话：悟空",)
)
docs = loader.load()

# 2.分割文档
from langchain_text_splitters import RecursiveCharacterTextSplitter

text_splitter = RecursiveCharacterTextSplitter(
  # 每个文本块的最大字符数
  chunk_size = 1000, 
  # 相邻文本块之间的重叠字符数
  chunk_overlap = 200
)
all_splits = text_splitter.split_documents(docs)

# 3.设置嵌入模型
from langchain_openai import OpenAIEmbeddings

embeddings = OpenAIEmbeddings()

# 4.创建向量存储
from langchain_core.vectorstores import InMemoryVectorStore

vectorstores = InMemoryVectorStore(embeddings)
vectorstores.add_documents(all_splits)

# 5.构建检索器
retriever = vectorstores.as_retriever(search_kwargs={"k": 3})

# 6.创建提示模板
from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_template("""
  基于以下上下文，回答问题。如果上下文中没有相关信息，
  请说"我无法从提供的上下文中找到相关信息"。
  上下文: {context}
  问题: {question}
  回答:"""
)

# 7.设置语言模型和输出解析器
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

from langchain_deepseek import ChatDeepSeek

llm = ChatDeepSeek(
  api_key = os.getenv("DEEPSEEK_API_KEY"),
  model_name = "deepseek-chat",
)

# 8.构建LECL链
chain = (
  {
    "context": retriever | (lambda docs: "\n\n".join(doc.page_content for doc in docs)), 
    "question": RunnablePassthrough()
  }
  | prompt
  | llm 
  | StrOutputParser()
)

# 9.执行查询
# 查看每个阶段的输入输出
# question = "测试问题"

# # 1. 检索器阶段
# retriever_output = retriever.invoke(question)
# print("检索器输出:", retriever_output)

# # 2. 合并文档阶段
# context = "\n\n".join(doc.page_content for doc in retriever_output)
# print("合并文档输出:", context)

# # 3. 提示模板阶段
# prompt_output = prompt.invoke({"context": context, "question": question})
# print("提示模板输出:", prompt_output)

# # 4. LLM阶段
# llm_output = llm.invoke(prompt_output)
# print("LLM输出:", llm_output)

# # 5. 解析器阶段
# final_output = StrOutputParser().invoke(llm_output)
# print("最终输出:", final_output)

# 9. 执行查询
question = "黑悟空有哪些游戏场景？"
response = chain.invoke(question) # 同步，可以换成异步执行
print(response)