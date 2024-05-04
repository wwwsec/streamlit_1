import streamlit as st

# 定义假数据
content_A = "这是菜单项 A 的内容。"
content_B = "这是菜单项 B 的内容。"
content_C = "这是菜单项 C 的内容。"
content_D = "这是菜单项 D 的内容。"

# 定义方法来显示不同菜单项的内容
def show_content(menu):
    if menu == 'A':
        st.write(content_A)
    elif menu == 'B':
        st.write(content_B)
    elif menu == 'C':
        st.write(content_C)
    elif menu == 'D':
        st.write(content_D)

# 在左侧栏显示传统的导航菜单
st.sidebar.title('菜单')
menu_selection = st.sidebar.radio(
    "",
    ['A', 'B', 'C', 'D']
)

# 在右侧页面显示相应内容
show_content(menu_selection)
