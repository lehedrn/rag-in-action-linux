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
%pip install llama-index-llms-openai
pip install llama-index-readers-database

pip install torch transformers python-pptx Pillow
pip install "unstructured[all]"
pip install huggingface_hub[hf_xet]
pip install camelot-py
pip install opencv-python
pip install pdfplumber
pip install "unstructured[image]"
pip install "unstructured[pptx]"
pip install "unstructured[md]"
pip install jq
pip install pymupdf
pip install pytesseract
pip install PyMySQL
pip install pdfplumber
pip install mysqlclient
pip install ghostscript

conda install conda-forge::flagembedding
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
pip install jq
pip install pymupdf
pip install pytesseract
pip install PyMySQL
pip install camelot-py
pip install opencv-python
pip install pdfplumber
pip install ghostscript

conda install conda-forge::flagembedding

```

## MySQL建表语句
```sql
CREATE TABLE game_scenes (
  id INT AUTO_INCREMENT PRIMARY KEY,
  scene_name VARCHAR(100) NOT NULL,
  description TEXT,
  difficulty_level INT,
  boss_name VARCHAR(100),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO game_scenes (scene_name, description, difficulty_level, boss_name)
VALUES 
('花果山', '悟空的出生地，山清水秀，仙气缭绕', 2, '六耳猕猴'),
('水帘洞', '花果山中的洞穴，悟空的老家', 1, NULL),
('火焰山', '炙热难耐的火山地带，充满岩浆与烈焰', 4, '牛魔王'),
('龙宫', '东海龙王的宫殿，水下奇景', 3, '敖广'),
('灵山', '如来佛祖居住的圣地，佛光普照', 5, '如来佛祖');
```

## 需要下载到本地的模型

[bge-visualized-base-en-v1.5](https://huggingface.co/BAAI/bge-visualized/resolve/main/Visualized_base_en_v1.5.pth?download=true), [bge-visualized-m3](https://huggingface.co/BAAI/bge-visualized/resolve/main/Visualized_m3.pth?download=true)) 