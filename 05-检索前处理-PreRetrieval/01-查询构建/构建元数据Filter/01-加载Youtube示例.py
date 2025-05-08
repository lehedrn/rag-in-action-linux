# from langchain_community.document_loaders import YoutubeLoader

# # 加载包含元数据的文档
# docs = YoutubeLoader.from_youtube_url(
#     "https://www.youtube.com/watch?v=zDvnAY0zH7U", add_video_info=True
# ).load()

# # 查看加载的第一个文档的元数据
# print(docs[0].metadata)

from langchain_yt_dlp.youtube_loader import YoutubeLoaderDL

# 需要安装google chrome浏览器
# 然后先在google chrome访问并登录youtube
# 然后利用ydl_p的cookiesfrombrowser功能获取cookie
# 然后修改/root/miniconda3/envs/rag-langchain-linux-02/lib/python3.10/site-packages/langchain_yt_dlp/youtube_loader.py文件
# 66行
# ydl_opts = {"quiet": True, "no_warnings": True, "skip_download": True}
# 替换成
# ydl_opts = {"quiet": True, "no_warnings": True, "skip_download": True, 'cookiesfrombrowser': ('chrome',),}
loader = YoutubeLoaderDL.from_youtube_url(
    "https://www.youtube.com/watch?v=zDvnAY0zH7U", 
    add_video_info=True,
)
docs = loader.load()
print(docs[0].metadata)