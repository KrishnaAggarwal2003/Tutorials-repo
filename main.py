import streamlit as st 
import os
import pandas as pd
import matplotlib.pyplot as plt   
import numpy as np

st.write("Website Maker") # Could write anything in the webpage

pressed = st.button("Press it")
print(pressed)  ## Any change done in application resulting in changing state, will make streamlit rerun the entire file.
## By pressing this button

# Some text elements of streamlit
st.title("Tutorial Website")
st.header("Tags in streamlit")
st.subheader("Subheader")
st.markdown("This is **Markdown** _tag_") # this could also take on html tags
st.caption("A sample caption text")

# For adding coding scripts
code_example = """
def add(x,y):
    return x + y
"""
st.code(code_example, language= "python" )

st.divider()

# Adding image in streamlit:
## Add images in folder named "static"
st.image(os.path.join(os.getcwd(), "static", "images.jpg"), caption="Friendly neighbourhood spidy")

# Data Elements
## Dataframes.
st.subheader("Dataframe & Tables")
dictio = {
    'Name': ['Alice','Bob','Daniel'],
    'Age': [24,25,26],
    'Gender': ['Female','Male','Male']
}
df = pd.DataFrame(dictio)

st.write('Static dataframe')
st.dataframe(df) # specifically for pandas dataframe.

st.write('Editable dataframe')
editable_df = st.data_editor(df)
print(editable_df)

st.write('Static Table')
st.table(editable_df)

## Metrics section
st.subheader("Metrics Section")
st.metric(label="No. of Rows", value=len(df))
st.metric(label="Average age",value=df['Age'].mean())

## JSON and Dict section
st.subheader("JSON and dictionary")
sample_dict = {
    'Name': 'Pastor Wilkins',
    'Age': 19,
    'Occupation': 'Interior designer'
}
st.json(sample_dict) # To display the contents in sample_dict as a json (key:value) format 

# Chart Elements
st.subheader("Plots in Streamlit")

chart_data = {
    'data':np.random.randn(20,3),
    'columns': ['A','B','C']
}

chart_df = pd.DataFrame(data=chart_data['data'], columns=chart_data['columns'])
st.write('Area Chart')
st.area_chart(chart_df)

st.write('Bar charts')
st.bar_chart(chart_df)

st.write('Line chart')
st.line_chart(chart_df)

scatter_data = {
    'x': np.random.randint(1,20, 100),
    'y': np.arange(100)
}
st.write('Scatter chart')
st.scatter_chart(pd.DataFrame(scatter_data))

# Pyplot section
st.write('Pyplot Section')
fig,ax = plt.subplots()
ax.plot(chart_df['A'], label='A')
ax.plot(chart_df['B'], label='B')
ax.plot(chart_df['C'], label='C')
ax.set_title('Pyplots of chart_data')
ax.legend()
st.pyplot(fig) # To display img of  matplotlib plots using streamlit, The plots get stored in 'fig'


## Form elements