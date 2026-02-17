import streamlit as st
import pandas as pd

# 1. 准备初始数据（长表格式）
# 每一行代表一个对应关系
data = [
    {"公司类型": "受託会社", "公司名字": "A株式会社"},
    {"公司类型": "受託会社", "公司名字": "B株式会社"},
    {"公司类型": "委託会社", "公司名字": "C株式会社"},
]

df = pd.DataFrame(data)

st.title("🏢 公司信息编辑器")

# 2. 使用 data_editor 展示并编辑
edited_df = st.data_editor(
    df,
    num_rows="dynamic",      # 允许动态增减行
    use_container_width=True, # 自动拉伸宽度
    column_config={
        "公司类型": st.column_config.SelectboxColumn(
            "公司类型",
            help="选择公司的类别",
            options=["受託会社", "委託会社", "其他"], # 限制输入范围，防止打错字
            required=True,
        ),
        "公司名字": st.column_config.TextColumn(
            "公司名字",
            # placeholder="请输入公司全称",
            required=True,
        )
    },
    key="company_editor"
)

# 3. 处理编辑后的数据
if st.button("💾 保存并更新"):
    # 将 DataFrame 转回你之前喜欢的字典格式
    # {'受託会社': ['A...', 'B...'], '委託会社': ['C...']}
    final_dict = {}
    for _, row in edited_df.iterrows():
        ctype = row["公司类型"]
        cname = row["公司名字"]
        if ctype not in final_dict:
            final_dict[ctype] = []
        final_dict[ctype].append(cname)
    
    st.success("数据已同步！")
    st.write(final_dict)