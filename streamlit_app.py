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

# 在左侧栏添加链接形式的菜单项
menu_selection = st.sidebar.radio(
    "",
    [
        '<a href="#A" style="text-decoration: none; color: inherit;">A</a>',
        '<a href="#B" style="text-decoration: none; color: inherit;">B</a>',
        '<a href="#C" style="text-decoration: none; color: inherit;">C</a>',
        '<a href="#D" style="text-decoration: none; color: inherit;">D</a>'
    ],
    format_func=lambda x: "",
    unsafe_allow_html=True  # 允许在 Markdown 中使用 HTML
)

# 在右侧页面显示相应内容
if menu_selection == '<a href="#A" style="text-decoration: none; color: inherit;">A</a>':
    show_content('A')
elif menu_selection == '<a href="#B" style="text-decoration: none; color: inherit;">B</a>':
    show_content('B')
elif menu_selection == '<a href="#C" style="text-decoration: none; color: inherit;">C</a>':
    show_content('C')
elif menu_selection == '<a href="#D" style="text-decoration: none; color: inherit;">D</a>':
    show_content('D')
