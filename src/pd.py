import pandas as pd
import streamlit as st

# 每一个 Value 都加上中括号 []
data = {
    '公司_1': ['A株式会社'], 
    '公司_2': ['B株式会社'], 
    '公司_3': ['C株式会社']
}

company_df = pd.DataFrame(data)

company_edited_df = st.data_editor(
    company_df,
    num_rows="dynamic",
    use_container_width=True,
    key="company_editor"
)