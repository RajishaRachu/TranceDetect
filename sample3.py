import streamlit as st
col1, col2 = st.beta_columns([6,1])
            with col1:
                st.markdown(f"**{row['name']}**({row['short_name']})", unsafe_allow_html=True)
                st.markdown(row['description'])
            with col2:
                if st.button(label='Open',key=row['id']):
                    pass 
```

