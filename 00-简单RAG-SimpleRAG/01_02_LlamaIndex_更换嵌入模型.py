from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from dotenv import load_dotenv

load_dotenv()

embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-large-zh")

documents = SimpleDirectoryReader(input_files=["90-文档-Data/黑悟空/黑悟空设定.txt"]).load_data()

index = VectorStoreIndex.from_documents(
    documents,
    embed_model=embed_model,
)

query_engine = index.as_query_engine()

print(query_engine.query("黑神话悟空中有哪些战斗工具?"))