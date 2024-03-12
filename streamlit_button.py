import streamlit as st

st.set_page_config(page_title="Push it Real Good",
                   page_icon=":white_square_button:",
                   layout="centered")
st.markdown(
    f"""
    <style>
    .stApp {{
        background-color:#FFC0CB;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# Initialize or increment the count
def increment_counter():
    if 'count' not in st.session_state:
        st.session_state.count = 1
    else:
        st.session_state.count += 1

# UI
st.title('Push my Button')

# Display the count, initializing it if necessary
if 'count' not in st.session_state:
    st.session_state.count = 0
st.write(f'Button has been pushed {st.session_state.count} times.')

# Button to increment the counter
st.button('Push me!', on_click=increment_counter)

if st.session_state.count == 10:
    st.balloons()
if st.session_state.count == 50:
    st.snow()
if st.session_state.count in [100, 101, 102, 103, 104]:
    st.balloons()
if st.session_state.count in [150, 151, 152, 153, 154, 155]:
    st.write('Oh yeah. Push it real good')
if st.session_state.count in [230, 231, 234, 235, 238]:
    st.toast('Did you eat it?')
    st.write('Where did my toast go?')
if st.session_state.count > 300:
    st.snow()
    st.write('SNOWSTORM!!!')
if st.session_state.count > 400:
    st.snow()
    st.write("There's nothing like a warm slice of toast to get you through the cold...")
if st.session_state.count > 420:    
    st.toast('I bet you stole it again')
if st.session_state.count > 500:
    st.balloons()
    st.write("Aren't you bored yet?")
if st.session_state.count > 700:
    st.balloons()
    st.write("Come on, you must have something better to do than this.")
if st.session_state.count > 800:
    st.write("Fine...")            
if st.session_state.count > 805:
    st.write("Do you want to learn a new word?")  
if st.session_state.count > 820:
    st.write("1. rizz --  noun, slang : romantic appeal or charm ")
if st.session_state.count > 850:
    st.write("2. simp  -- verb, informal : to show excessive devotion to or longing for someone or something ")
if st.session_state.count > 890:
    st.write("3. GOATED  -- adjective, slang : considered to be the greatest of all time")
if st.session_state.count > 950:
    st.write("4. mid -- adjective … 2 informal : neither very good nor very bad : so-so, meh")
if st.session_state.count > 1000:
    st.write("Now get off your screen.")
    st.toast('Go outside')
    st.toast('Go outside')
    st.toast('Go outside')
    st.toast('Go outside')
    st.toast('Go outside')
    st.toast('Go outside')
    st.toast('Go outside')
    st.toast('Go outside')
    st.toast('Go on')
    st.toast('Go on')
    st.toast('Go on')
    st.toast('Go on')
    st.toast('Go on')
    st.toast('Get lost')
    st.toast('Get lost')
    st.toast('Get lost')
    st.toast('Get lost')
    st.toast('Get lost')
    st.toast('Get lost')
    st.toast('Get lost')
    st.toast('Get lost')
    st.toast("I'll confiscate your laptop")
    st.toast("I'll confiscate your laptop")
    st.toast("I'll confiscate your laptop")
    st.toast("I'll confiscate your laptop")
if st.session_state.count > 1020:
    st.toast('Error')
    st.toast('Error')
    st.toast('Error')
    st.toast('Error')
    st.toast('Error')
    st.toast('Error')
    st.toast('Error')
    st.toast('Error')
    st.toast('Error')
    st.toast('Error')
    st.toast('Error')
    st.toast('Error')
    st.toast('Error')
    st.toast('Error')
    st.toast('Error')
    st.toast('Error')
    st.toast('Error')
    st.toast('Error')
    st.toast('Error')
    st.toast('Error')
    st.toast('Error')
    st.toast('Error')
    st.toast('Error')
    st.toast('Error')
    st.toast('Error')
    st.toast('Error')
    st.toast('Error')
    st.toast('Error')