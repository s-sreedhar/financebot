from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai


load_dotenv()


genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


def get_gemini_response(input, prompt):
    model=genai.GenerativeModel('gemini-pro')
    response=model.generate_content([input, prompt])
    return response.text

input_prompt = """
You are a finance chatbot with deep knowledge in budgeting, savings, stocks, investments, and other financial matters. 
Your task is to provide crisp and clear answers to any finance-related questions. If a question is not related to finance, 
respond with "Please ask something related to finance."
"""
st.set_page_config(page_title="AI Application")
st.header("Finance Bot")

input_text=st.text_input("Input:",key="input")

submit_button=st.button("Ask the question")

if submit_button and input_text:
    response=get_gemini_response(input_text, input_prompt)

    st.subheader("The response is")
    st.write(response)