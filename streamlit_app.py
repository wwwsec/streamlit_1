import streamlit as st

# 定义假数据
content_A = "这是菜单项 A 的内容。"
content_B = "这是菜单项 B 的内容。"
content_C = "这是菜单项 C 的内容。"
content_D = "这是菜单项 D 的内容。"

def showa():
    st.write(content_A)
    st.write(content_A)
    st.write(content_A)
    st.write(content_A)

def showb():
    st.write(content_B)

def showc():
    st.write(content_C)

def showd():
    st.write(content_D)

# 定义方法来显示不同菜单项的内容
def show_content(menu):
    if menu == 'A':
        showa()
    elif menu == 'B':
        showb()
    elif menu == 'C':
        showc()
    elif menu == 'D':
        showd()



# 在左侧栏添加菜单项
menu_selection = st.sidebar.radio("选择菜单项", ['A', 'B', 'C', 'D'])

# 在右侧页面显示相应内容
show_content(menu_selection)
