file_path = ("90-文档-Data/山西文旅/云冈石窟-en.pdf")
from langchain_unstructured import UnstructuredLoader
loader = UnstructuredLoader(
    file_path=file_path,
    strategy="hi_res",
    # partition_via_api=True,
    # coordinates=True,
)
docs = []


# lazy_load() 是一种延迟加载方法
# 它不会一次性将所有文档加载到内存中，而是在需要时才逐个加载文档
# 这对于处理大型PDF文件时可以节省内存使用
for doc in loader.lazy_load():
    docs.append(doc)

print(docs)
