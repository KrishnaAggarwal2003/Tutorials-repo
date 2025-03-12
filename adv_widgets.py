import streamlit as st

st.header("Advanced Widgets") 
# A unique key or id is assigned to the widgets in streamlit, for accessing the widget
# Could also add the key ourselves to the widgets

st.button("Ok")
st.button("Ok", help="Different from previous one")

min_val = st.slider("Min-value:", 0, 50, 25, help="Setting up the min-value for next slider")

slider_value = st.slider(label="Set something: ", min_value=min_val, max_value=100, step=1)

# Using a checkbox
if "checkbox" not in st.session_state:
    st.session_state.checkbox = False

def toggle():
    st.session_state.checkbox = not st.session_state.checkbox

st.checkbox(label="Show Input", value=st.session_state.checkbox, on_change=toggle)

if st.session_state.checkbox:
    if "user_input" not in st.session_state:
        st.session_state.user_input = ""
    
    user_input = st.text_input(label="Enter Nmae: ", value=st.session_state.user_input)
    st.session_state.user_input = user_input
else:
    user_input = st.session_state.get("user_input","")

st.write(f"User Input: {user_input}")                