import streamlit as st

# 定义选项
options = ["Gemini 1.5 Pro", "Azure GPT-5", "Claude 3.5 Sonnet"]

# 创建下拉菜单
# 参数 1: 标签文字; 参数 2: 选项列表
selected_model = st.selectbox("请选择要使用的 AI 模型:", options)

# 显示选中的结果
st.write(f"你当前选择的模型是: **{selected_model}**")