import streamlit as st

# 示例数据
list1 = ["苹果", "西瓜", "草莓"]  # 数量较小
list2 = ["香蕉", "苹果", "葡萄", "西瓜", "芒果"]  # 数量较多

st.title("动态列表匹配选择器")

# 存储用户的选择结果
final_selections = {}

# 循环 list1
for i, item in enumerate(list1):
    # 为了保证 list2 在每次循环中互不干扰，我们复制一份 list2
    current_options = list(list2)
    
    if item in current_options:
        # 如果存在，计算它在 list2 中的索引位置
        default_index = current_options.index(item)
        status_msg = f"（已在列表中找到 '{item}'）"
    else:
        # 如果不存在，将其插入到 list2 的第一个位置
        current_options.insert(0, item)
        default_index = 0
        status_msg = f"（'{item}' 不在原列表中，已临时添加）"
    
    # 使用 selectbox 显示
    # 注意：在循环中创建组件，key 必须唯一，这里使用 item 和索引 i 组合
    selected_value = st.selectbox(
        f"选择项目 {i+1} {status_msg}:",
        options=current_options,
        index=default_index,
        key=f"select_{item}_{i}"
    )
    
    final_selections[item] = selected_value

st.divider()
st.write("### 最终确认的选择：")
st.json(final_selections)