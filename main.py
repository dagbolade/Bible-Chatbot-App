import streamlit as st
st.title("Bible Chatbot")
query = st.text_input("Enter your question:")
if query:
    # code to handle the query and generate a response goes here
    response = "This is the chatbot's response to your query."
    st.write(response)

if query:
    response = chatbot_model.predict(query)
    st.write(response)
