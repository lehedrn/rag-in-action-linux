from langchain_community.document_loaders import DirectoryLoader

# 指定要加载文档的目录
directory_path = '90-文档-Data/黑悟空'

# 创建DirectoryLoader对象，添加错误处理
try:
    loader = DirectoryLoader(
        directory_path,
        glob="**/*.md", # 指定要加载的文件类型
        use_multithreading=True, # 使用多线程
        show_progress=True, # 显示进度
    )

    # 加载目录中的所有文档
    documents = loader.load()

    # 打印加载的文档数量
    print(f"文档数： {len(documents)} ")
    print("-----------------")
    if documents:
        print(documents[0])
    else:
        print("没有成功加载任何文档")
except Exception as e:
    print(f"加载文档时发生错误: {str(e)}")
