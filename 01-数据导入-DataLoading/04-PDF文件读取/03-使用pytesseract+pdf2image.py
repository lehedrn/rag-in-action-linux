# 扫描图片型 PDF，建议用 pytesseract + pdf2image  
# sudo apt-get install tesseract-ocr
# sudo apt-get install tesseract-ocr-chi-sim
# 这里可以通过tesseract --list-langs来查看安装了几种语言

from datetime import datetime
import os
import pdf2image
import pytesseract

# 确保output目录存在
output_dir = f"92-图片-Pic/output{datetime.now().strftime('%Y%m%d')}"
os.makedirs(output_dir, exist_ok=True)

# 将 PDF 转换为图片并保存
images = pdf2image.convert_from_path('90-文档-Data/黑悟空/黑神话悟空.pdf')
for i, image in enumerate(images):
    image.save(f'{output_dir}/page_{i+1}.png')

# 使用 pytesseract 提取文本
for i, image in enumerate(images):
    text = pytesseract.image_to_string(image, lang='chi_sim')
    print(f"第 {i+1} 页文本:")
    print(text)
    print("\n") 