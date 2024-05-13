from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai


load_dotenv()


genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


model = genai.GenerativeModel("gemini-pro") 
chat = model.start_chat(history=[])


def get_gemini_response(question):
    if "finance" in question.lower() or "budget" in question.lower() or "investment" in question.lower() or "trade" in question.lower():
        response = chat.send_message(question, stream=True)
        return response
    else:
        return ["Please ask something related to Finance."]


st.set_page_config(page_title="Q&A Demo")
st.header("Finance Chatbot")


if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []


input_text = st.text_input("Input: ", key="input")


submit_button = st.button("Ask the question")


if submit_button and input_text:
   
    response = get_gemini_response(input_text)
    
    
    st.session_state['chat_history'].append(("You", input_text))
    st.subheader("The Response is")
    
   
    for chunk in response:
        st.write(chunk) 


st.subheader("The Chat History is")
for role, text in st.session_state['chat_history']:
    st.write(f"{role}: {text}")
