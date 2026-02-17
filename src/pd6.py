import pandas as pd

companynames = ["A株式会社", "B株式会社", "C株式会社"]
companytype = "受託会社"

companies = []

# ---------------------------------------------------------
for name in companynames:
    # 核心：每次循环都创建一个全新的字典
    item = {
        "公司类型": companytype,
        "公司名字": name
    }
    companies.append(item)

print(companies)