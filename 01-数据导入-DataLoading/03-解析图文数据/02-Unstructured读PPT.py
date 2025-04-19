# from unstructured.partition.auto import partition
from unstructured.partition.pptx import partition_pptx
# from unstructured.partition.ppt import partition_ppt

# 必须安装 - Install instructions: https://www.libreoffice.org/get-help/install-howto/

ppt_path = "90-文档-Data/黑悟空/黑神话悟空.pptx"

try:
    # 使用partition函数，它会自动检测文件类型
    # ppt_elements = partition(ppt_path)
    ppt_elements = partition_pptx(ppt_path)
    # ppt_elements = partition_ppt(ppt_path)
    
    print("ppt内容：")
    for element in ppt_elements:
        print(element.text)

    from langchain_core.documents import Document
    documents = [Document(page_content=element.text, metadata={"source": ppt_path}) for element in ppt_elements]
    print(documents[0:3])
except Exception as e:
    print(f"发生错误: {str(e)}")
