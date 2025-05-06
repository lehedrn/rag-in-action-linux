from llama_index.core import SimpleDirectoryReader

documents = SimpleDirectoryReader("90-文档-Data", recursive=True).load_data()

print(f"文档加载完成, 共 {len(documents)} 个文档")

from llama_index.core import VectorStoreIndex
index = VectorStoreIndex.from_documents(documents)
print(f"索引创建完成:\n {vars(index)}")

# nodes = index.index_struct.nodes_dict
# for node in nodes:
#     print(f"节点: {node}")

    
from llama_index.core.node_parser import SentenceSplitter

text_splitter = SentenceSplitter(chunk_size=512, chunk_overlap=10)
nodes = text_splitter.get_nodes_from_documents(documents)
index = VectorStoreIndex(nodes) # 从nodes中生成Index
nodes = index.index_struct.nodes_dict
for node in nodes:
    print(f"节点: {node}")

print(f"索引创建完成, 共 {len(nodes)} 个节点")

# 保存索引到磁盘
index.storage_context.persist(persist_dir="04-向量存储-VectorDB/LlamaIndex/saved_index")