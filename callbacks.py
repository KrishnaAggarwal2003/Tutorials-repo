# a callback is a function that is passed as an argument to another function and is intended to be executed after some event or operation has occurred.

# Basically, In streamlit callback is that particular function which you would like to execute if any event like user input or button click happens.


# Callback function run before any other code on next rerun

import streamlit as st 

st.set_page_config(page_title="Callbacks Page")

st.header(body="Callbacks concept in Streamlit")

# Call-back functions
def step2(name): 
    st.session_state.info["name"] = name
    st.session_state.step = 2
    

def go_back():
    st.session_state.step = 1


# Initializing params
if "step" not in st.session_state: # Initialized the variable in the session
    st.session_state.step = 1

if "info" not in st.session_state:
    st.session_state.info = {}



if st.session_state.step == 1:
    st.header("Part 1: Info")
    
    name = st.text_input(label="Nmae: ", value=st.session_state.info.get("name",""))
    
    st.button(label="Next", on_click=step2, args=(name,)) # Callback triggered here             



if st.session_state.step == 2:
    st.header("Part 2: Review")
    st.subheader("Review this: ")
    st.write(f"**Name**: {st.session_state.info.get('name', '')}")
    
    if st.button("Submit"):
        st.success("Great!")
        st.balloons()
        
        st.session_state.info = {}
        
    st.button("Go back", on_click=go_back) # Callback triggered here     
               