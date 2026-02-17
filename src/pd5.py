import pandas as pd

dict = {}

companies = []
companytype = "受託会社"


# ---------------------------------------------------------
companynames = ["A株式会社", "B株式会社", "C株式会社"]
companytype = "受託会社"
for name in companynames:
    dict[companytype] = name
    companies.append(dict)
print(dict)