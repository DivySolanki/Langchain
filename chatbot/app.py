from llamaapi import LlamaAPI
from langchain_experimental.llms import ChatLlamaAPI
import streamlit as st

import os
from dotenv import load_dotenv

load_dotenv()
SECRET_LLAMA_KEY = os.getenv('LLAMA_API_KEY')

def get_llama_response(question):
    llama = LlamaAPI(api_token=SECRET_LLAMA_KEY)
    llm = ChatLlamaAPI(client=llama)
    response = llm.invoke(question)
    return response.content

st.set_page_config(page_title="Q&A Demo")

st.header("Langchain Application")

input = st.text_input("Input: ", key="input")
response = get_llama_response(input)

submit = st.button("Ask the question")

if submit:
    st.subheader("The Response is")
    st.write(response)
