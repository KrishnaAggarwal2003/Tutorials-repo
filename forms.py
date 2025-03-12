import streamlit as st  
import pandas as pd  
from datetime import datetime

st.markdown('<h1 style="text-align: center;">Streamlit Sample Form</h1>', unsafe_allow_html=True) # Title in the center position

# Making a sample form
st.set_page_config(page_title="Calls Page")

form_data = {
    'user_name': None,
    'User_age':None,
    'feedback': None,
    'date': None,
    'time':None,
    'Options': None,
    'Sex': None
} # Saving the contents of the form



# This with block will re-run once the submit button is pressed. It kinda holds to the re-run process such that it will re-run the code once submit is pressed.
with st.form(key="forms", clear_on_submit=True): # 'key' as in a unique identifier
    # user info
    st.subheader(body="User information")
    form_data['user_name'] = st.text_input("Enter your Name: ")
    form_data['User_age'] = st.number_input(label="Enter your age",min_value=1, max_value=80)
    form_data['feedback'] = st.text_area(label="Enter your feedback", height=200)
    
    
    # Date and Time inputs
    st.subheader(body="Enter date and time")
    form_data['date'] = st.date_input(label="Enter your B'day: ", min_value=datetime(1990,1,1), max_value=datetime.now())
    form_data['time'] = st.time_input(label="Enter the Time of your birth: ")
    
    # Selectors
    st.subheader(body="Choosing options")
    form_data['Options'] = st.radio(label="Select an option: ",options=['A','B','C']) # To give MCQ's
    form_data['Sex'] = st.selectbox(label="Select your gender: ",options=['Male','Female','Others']) # To give a box and options to select
    
    slide_viewer = st.select_slider(label="Select the range",options=[1,2,3,4,5])
    
    # Checkboxes
    st.write("Checkbox things")
    notify = st.checkbox(label="Recieved Notifications?", value=False)
    dark_mode = st.checkbox(label="Enable dark mode", value=True)
    
    submit = st.form_submit_button(label="Submit the form") # This submit button from web-page will allow the user to run this with block code from the UI.
    if submit:
        if not all(form_data.values()): # If anything got missed in form_data
            st.warning(body="Fill all the required fields") # Warning won't appear once all entries for form_data are attempted
        else:
            st.balloons() # Popping of balloons
            st.subheader(body="Data from the form")
            st.json(form_data) # Will display the contents of the form once clicked submit
                
            


