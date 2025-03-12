import streamlit as st  


st.set_page_config(page_title="Layout Page")
st.header(body="Layouts in Streamlit")

# Sidebar settings
st.sidebar.title(body="This is sidebar")
st.sidebar.write("Place some elements")

if "content_list" not in st.session_state:
    st.session_state.content_list = []

sidebar_input = st.sidebar.text_input(label="Enter in side-bar")

button_press = st.sidebar.button(label="Sidebar_input update")

#tabs layout
tab1, tab2, tab3 = st.tabs(['tab1', 'tab2', 'tab3'])

with tab1:
    st.write("You are in tab1")
    
with tab2:
    st.write("You are in tab2")

with tab3:
    st.write("You are in tab3")

# Columns layout
col1 , col2 = st.columns(2)
with col1:
    st.subheader("Column 1")
    st.write("Content for column 1")
with col2:
    st.subheader("Column 2")
    st.write("Content for column 2")

# Container example
with st.container(border=True):
    st.write("Hello People")
    
# Placeholder
placeholder = st.empty()
placeholder.write("Placeholder helpful for dynamic content")

if st.button("Update placeholder"):
    placeholder.write("Not empty anymore.")

# Expander
with st.expander("Expand for more details"):
    st.write("Additional Info could be given inside this expander as how developer wants to show contents to his user.")        
            
# Popover (Tooltip)
st.write("Hover over the button for tip")
st.button("Button having tooltip", help="A tooltip message")# A help pop-up message when cursor is on the button


if button_press:
    st.session_state.content_list.append(sidebar_input) 
    st.write(f"Contents in side-bar: {[content for content in st.session_state.content_list]}")             