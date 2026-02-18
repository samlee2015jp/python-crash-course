text = "[A株式会社]"
# 移除头尾的 [ 和 ]
clean_text = text.strip("[]")

print(clean_text) 
# 输出: A株式会社