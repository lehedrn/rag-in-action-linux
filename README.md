# rag-in-action-linux

## 运行环境

- 操作系统: wsl2, ubuntu
- Python: 3.10
- conda: 24.11.0

## 虚拟环境配置

### llamaindex
```base
conda create -n rag-llamaindex-linux python=3.10

conda install conda-forge::llama-index
conda install conda-forge::python-dotenv

pip install llama-index-embeddings-huggingface
pip install llama-index-llms-deepseek

pip install torch transformers python-pptx Pillow
pip install "unstructured[all]"
pip install huggingface_hub[hf_xet]
```

### langchain
```base
conda create -n rag-langchain-linux python=3.10

pip install langchain langchain-community langchain-huggingface langgraph langchain-unstructured langchain-deepseek langgraph langsmith
pip install python-dotenv
pip install beautifulsoup4
pip install faiss-cpu
pip install huggingface_hub[hf_xet]
pip install unstructured
pip install "unstructured[image]"
pip install "unstructured[pptx]"
pip install "unstructured[md]"

```