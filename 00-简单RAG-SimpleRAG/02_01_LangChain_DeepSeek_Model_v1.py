# 导入os模块，用于与操作系统进行交互，例如获取环境变量
import os
# 从dotenv模块导入load_dotenv函数，用于加载.env文件中的环境变量
from dotenv import load_dotenv

# 加载.env文件中的环境变量
load_dotenv()
os.environ["USER_AGENT"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"

# 从langchain_community.document_loaders模块导入WebBaseLoader类，用于从网页加载文档
from langchain_community.document_loaders import WebBaseLoader

# 创建一个WebBaseLoader实例，指定要加载的网页路径
# 需要安装
# conda install conda-forge::beautifulsoup4
loader = WebBaseLoader(
  # 要加载的网页URL
  web_paths=("https://zh.wikipedia.org/wiki/黑神话：悟空",)
)

# 调用loader的load方法，加载网页内容并存储为文档对象
docs = loader.load()

# 从langchain_text_splitters模块导入RecursiveCharacterTextSplitter类，用于将文档分割成小块
from langchain_text_splitters import RecursiveCharacterTextSplitter

# 创建一个RecursiveCharacterTextSplitter实例，设置每个文本块的大小和重叠部分
text_splitter = RecursiveCharacterTextSplitter(
  # 每个文本块的最大字符数
  chunk_size = 1000,
  # 相邻文本块之间的重叠字符数
  chunk_overlap = 200
)
# 调用text_splitter的split_documents方法，将文档分割成多个小块
all_splits = text_splitter.split_documents(docs)

# 从langchain_huggingface模块导入HuggingFaceEmbeddings类，用于生成文本的嵌入向量
from langchain_huggingface import HuggingFaceEmbeddings

# 创建一个HuggingFaceEmbeddings实例，指定使用的模型和相关参数
embeddings = HuggingFaceEmbeddings(
  # 使用的预训练模型名称
  model_name="BAAI/bge-small-zh-v1.5",
  # 模型运行的设备，这里使用CPU
  model_kwargs={'device': 'cpu'},
  # 编码时的参数，这里对嵌入向量进行归一化处理
  encode_kwargs={'normalize_embeddings': True}
)

# 从langchain_core.vectorstores模块导入InMemoryVectorStore类，用于在内存中存储向量数据库
from langchain_core.vectorstores import InMemoryVectorStore

# 创建一个InMemoryVectorStore实例，传入嵌入向量生成器
vector_store = InMemoryVectorStore(embeddings)
# 调用vector_store的add_documents方法，将分割后的文本块添加到向量数据库中
vector_store.add_documents(all_splits)

# 定义一个问题，用于在向量数据库中进行相似性搜索
question = "黑悟空有哪些游戏场景？"

# 调用vector_store的similarity_search方法，根据问题在向量数据库中搜索最相似的文档，返回前3个结果
retrieved_docs = vector_store.similarity_search(question, k=3)
# 将检索到的文档内容拼接成一个字符串，用两个换行符分隔
docs_content = "\n\n".join(doc.page_content for doc in retrieved_docs)

# 从langchain_core.prompts模块导入ChatPromptTemplate类，用于创建聊天提示模板
from langchain_core.prompts import ChatPromptTemplate

# 创建一个ChatPromptTemplate实例，使用模板字符串定义提示内容
prompt = ChatPromptTemplate.from_template("""
  基于以下上下文，回答问题。如果上下文中没有相关信息，
  请说"我无法从提供的上下文中找到相关信息"。
  上下文: {context}
  问题: {question}
  回答:"""
)

# 从langchain_deepseek模块导入ChatDeepSeek类，用于与DeepSeek模型进行交互
from langchain_deepseek import ChatDeepSeek

# 创建一个ChatDeepSeek实例，指定使用的模型、温度、最大生成令牌数和API密钥
llm = ChatDeepSeek(
    # 使用的DeepSeek模型名称
    model="deepseek-chat",
    # 生成文本时的随机性，值越大越随机
    temperature=0.7,
    # 生成文本的最大令牌数
    max_tokens=2048,
    # 从环境变量中获取DeepSeek的API密钥
    api_key=os.getenv("DEEPSEEK_API_KEY")
)
# 调用llm的invoke方法，根据提示模板填充问题和上下文，生成回答
answer = llm.invoke(prompt.format(question=question, context=docs_content))
# 打印生成的回答
print(answer)