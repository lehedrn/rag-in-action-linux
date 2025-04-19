from langchain_community.document_loaders import DirectoryLoader
# import pytesseract

# 必须安装
# conda install conda-forge::unstructured
# pip install langchain-unstructured
# 需要安装tesseract-ocr
# 需要安装依赖包 conda install conda-forge::pytesseract
# 设置 Tesseract 路径（根据你的实际安装路径修改）
# 还需要配置环境变量，配置到tesseract.exe所在的根目录即可
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
# 需要安装tesseract-ocr
#sudo apt install tesseract-ocr

# 指定要加载文档的目录
directory_path = '90-文档-Data/黑悟空'

# 创建DirectoryLoader对象，添加错误处理
try:
    loader = DirectoryLoader(
        directory_path
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
