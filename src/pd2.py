import pandas as pd
import streamlit as st

# 使用单一列名，列表存储所有公司
data = {
    '公司名称': ['A株式会社', 'B株式会社', 'C株式会社']
}

company_df = pd.DataFrame(data)

st.write("### 编辑公司清单")
company_edited_df = st.data_editor(
    company_df,
    num_rows="dynamic", # 允许点击底部的 (+) 按钮增加新公司
    use_container_width=True,
    key="company_editor"
)

# 获取编辑后的纯列表数据
if st.button("保存更改"):
    updated_list = company_edited_df["公司名称"].tolist()
    st.success(f"已更新清单: {updated_list}")