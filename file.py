import streamlit as st
st.set_page_config(layout="wide",page_title='Trance Dict', page_icon="🖖")
#st.markdown('<style>h1{background-color: red;}</style>', unsafe_allow_html=True)
with open('Ui_style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
with st.container():
    t1=st.header(" Trance Dict")
#with st.container():
cols1,cols2=st.columns([1,8.7])
       # with cols1:
cols1.button(label="Translate text")
       # with cols2:
cols2.button(label="Translate files")

col1,col2,col3=st.columns([600,70,600])
with col1:
     lang_label=st.text_input( "",placeholder=" detect language")
    # st.write("detect language")
     Txt_a=st.text_area("",height=374 ,placeholder="Type to translate",key="T_area_one")
   # components.html("<button> click here</button>", height=100,)
with col2:
    st.button(label="Click Here",on_click="")
with col3: 
   option = st.selectbox(
     'select language',
     ('malayalam', 'Hindi', 'kannada','Thamil'))
   Txt_a2=st.text_area("",height=374, placeholder=" translate",key="T_area_two")
# Remove whitespace from the top of the page and sidebar


