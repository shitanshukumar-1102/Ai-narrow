user_input = ""
command = ""
print("App started...")

import streamlit as st
from jarvis import process_command, speak, listen

st.set_page_config(page_title="Jarvis AI")
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(to right, #4facfe, #00f2fe);
    }
    </style>
    """,
    unsafe_allow_html=True
)


st.title("🤖 NARROW AI (an assistent you can always belive)")

option = st.radio("Choose Input Method:", ["Text", "Voice"])

# -------- TEXT MODE --------
if option == "Text":
    user_input = st.text_input("Enter your command:")

if user_input:
    response = process_command(user_input)

    if response == "exit":
        st.warning("Shutting down Jarvis...")
    else:
        st.success(response)
        speak(response)       
# -------- VOICE MODE --------
elif option == "Voice":
    if st.button("Start Listening"):
        st.info(" Listening... Speak clearly")

        command = listen()

if command:
    st.write(f"You said: {command}")
    response = process_command(command)

    if response == "exit":
        st.warning("Shutting down Jarvis...")
    else:
        st.success(response)
        speak(response)
else:
    st.error("Could not understand. Try again.")

with st.expander("show running instructions"):
    st.markdown("""
1. Select voice or text  
2. Type/Speak your command 
3. wait for response                 
4. Narrow will give answer
""")
