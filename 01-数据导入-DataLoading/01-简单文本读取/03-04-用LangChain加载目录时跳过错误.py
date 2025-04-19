from langchain_community.document_loaders import DirectoryLoader, TextLoader

directory_path = '90-文档-Data/黑悟空'

loader = DirectoryLoader(
    directory_path,
    loader_cls=TextLoader,
    loader_kwargs={"encoding": "utf-8"},
    silent_errors=True,
)

documents = loader.load()

print(f"加载的文档数：{len(documents)}")

for doc in documents:
  print(f"文档：{doc.metadata['source']}, 内容：{doc.page_content[:50]}")

