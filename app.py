import streamlit as st
from openai import OpenAI

st.title("Hari Smart Products - Customer Support Agent")

client = OpenAI(api_key="sk-proj-_OEmzGKRKDHglobbUPKXS7FGI")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Aapki kya madad kar sakte hain?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    
    bot_reply = response.choices[0].message.content
    with st.chat_message("assistant"):
        st.markdown(bot_reply)
    st.session_state.messages.append({"role": "assistant", "content": bot_reply})
