import os

# 你的 PDF 文件目录
pdf_dir = "/Users/samli/books/toreadbooks/"
# 输出的 Markdown 文件路径
output_md = "/Users/samli/books/toreadbooks/books_list.md"

# 获取所有 PDF 文件
files = [f for f in os.listdir(pdf_dir) if f.endswith(".pdf")]
files.sort()  # 按字母排序

# 写入 Markdown 文件
with open(output_md, "w", encoding="utf-8") as md_file:
    md_file.write("# 待读书籍列表\n\n")
    for f in files:
        md_file.write(f"- {f}\n")

print(f"已生成 Markdown 文件：{output_md}")
