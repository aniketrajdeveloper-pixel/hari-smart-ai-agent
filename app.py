import streamlit as st
from google import genai

st.title("Hari Smart Products - Customer Support Agent")

client = genai.Client(api_key="AIzaSyArVQEP43AK4N1Q1MFPj3vMsej4CfGDZzM")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Aapki kya madad kar sakte hain?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    response = client.models.generate_content(
        model="gemini-1.5-flash",
        contents=prompt,
    )
    
    with st.chat_message("assistant"):
        st.markdown(response.text)
    st.session_state.messages.append({"role": "assistant", "content": response.text})
