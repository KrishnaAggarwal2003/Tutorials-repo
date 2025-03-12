# To avoid redundant computations or loading of functions in code which will occur beacuse of re-running the code file.

# Using caching, we can avoid re-running of some code functions that need not to run with every re-run in streamlit due to user interaction.

import streamlit as st 
import time

st.set_page_config(page_title="Caching Page")

# Cached_data decorator
@st.cache_data(ttl=60) # Cache this data for 60 seconds
def fetch_data():
    time.sleep(3) # Delayed it to mimic the long process 
    return {"data": "Example of an cached data"}

st.write("fetching data")
if st.button("Chaching on"):
 data = fetch_data()
 st.json(data)


# Cached_Resource decorator
@st.cache_resource
def get_file_handler(file_path):
    try:
        file = open(file_path, "a+")
        return file  # Now, rather than a particular data, I returned the file itself. Now user can do whatever he wants using this file_handler
    except Exception as e:
        st.error(f"Failed to open file: {e}")
        return None



if st.button(label="Write to file"):
    file_handler = get_file_handler(file_path="example.txt")
    file_handler.write("New line of text,everyone\n")
    file_handler.flush() # Ensure the content is written immediately
    st.success("Wrote a new line into the file!")
    
      