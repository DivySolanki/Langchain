import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms.ctransformers import CTransformers
from langchain_experimental.llms import ChatLlamaAPI
from llamaapi import LlamaAPI
from dotenv import load_dotenv
import os

load_dotenv()

SECRET_KEY = os.getenv('LLAMA_API_KEY')

## Function to get response from Llama 2 model

def getLlamaResponse(input_text, no_words, blog_style):

    ## Llama2 model GGML model
    # llm = CTransformers(model='path/to/your/model',
    #                     model_type='llama',
    #                     config={'max_new_tokens': 256,
    #                             'temperature': 0.01})
    ## Using API
    llama = LlamaAPI(api_token=SECRET_KEY)
    llm = ChatLlamaAPI(client=llama)
    api_request_json = {
        "model": 'llama-70b-chat',
        "max_length": 256,
        "temperature": 0.01,
    }

    template = '''
                Write a blog for {blog_style} job profile for a topic {input_text} within {no_words} words.
                Don't specify what will you generate.
                '''

    prompt = PromptTemplate(input_variables=['blog_style', 'input_text', 'no_words'],
                            template=template)
    
    # Generate the response from the LLama 2 model
    response = llm.invoke(prompt.format(blog_style=blog_style,input_text=input_text,no_words=no_words)) # , config=api_request_json
    print(response.content)
    return response.content

st.set_page_config(page_icon='🤖',
                   page_title='Generate Blogs',
                   layout='centered',
                   initial_sidebar_state='collapsed')

st.header('Generate Blogs 🤖')

input_text = st.text_input('Enter the Blog Topic')

## Creating 2 more columns for additional 2 fields

col1, col2 = st.columns([5, 5])

with col1:
    no_words = st.text_input('No. of Words')
with col2:
    blog_style = st.selectbox('Writing the blog for',
                              ('Researchers', 'DataScientists', 'Common People'),
                              index=0)

submit = st.button('Generate')

## Final response 

if submit:
    st.write(getLlamaResponse(input_text, no_words, blog_style))