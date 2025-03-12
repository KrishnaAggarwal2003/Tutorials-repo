import streamlit as st  

# While pressing the button, the code file will automatically re-run, and information isn't getting stored from one to next re-run. Therefore, with pressing the button to run the "def before()", the counter value and counter incremented will always be stuck at 0 & 1. 

st.set_page_config(page_title="Session states")
def before_session_state():
 counter = 0
 st.write(f"Counter value: {counter}")
 print(f"Counter value: {counter}")

 button = st.button(label="Increment Counter")
 if button:
    counter+=1
    st.write(f'Counter incremented at {counter}')
    print(f'Counter incremented at {counter}')
 else:
    st.write(f'counter stays at {counter}')    

def after_session_state():
    
    if "counter" not in st.session_state: # This enables storing the value of counter variable in session_state, which enables persisting of the value of counter variable
     st.session_state.counter = 0
    
    button = st.button(label="Counter incref")
    if button:
        st.session_state.counter+=1
        st.write(f'Counter increased {st.session_state.counter}')
        print(f'Counter increased {st.session_state.counter}')
    
    if st.button("Reset"):
        st.session_state.counter = 0
    else:
        st.write("Counter not zero")
    
    st.write(f'Counter value : {st.session_state.counter}')   
    print(f'Counter value : {st.session_state.counter}')         

after_session_state()    