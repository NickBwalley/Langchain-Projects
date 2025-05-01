import streamlit as st
import openai
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
import io
from docx import Document
from fpdf import FPDF
import markdown

import os
from dotenv import load_dotenv
load_dotenv()

## Langsmith Tracking
os.environ["LANGSMITH_API_KEY"]=os.getenv("LANGSMITH_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_PROJECT"]="Simple Q&A Chatbot With OPENAI"

## Prompt Template
prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful massistant . Please  respond to the user's queries articulately. "),
        ("user","Question:{question}")
    ]
)

## Function to generate response from OpenAI API
## This function takes the user input, API key, model engine, temperature, and max tokens as parameters.
## It returns the generated response from the OpenAI API.
def generate_response(question,api_key,engine,temperature,max_tokens):
    openai.api_key=api_key

    llm=ChatOpenAI(model=engine)
    output_parser=StrOutputParser()
    chain=prompt|llm|output_parser
    answer=chain.invoke({'question':question})
    return answer

## #Title of the app
st.title("Enhanced Q&A Chatbot With OpenAI Models")
st.subheader("Ask any question and get instant responses from OpenAI's latest models")
st.write("This app uses OpenAI's GPT-4.1 models to provide accurate and articulate responses to your queries.")
st.write("You can adjust the model settings in the sidebar to customize your experience.")

## Sidebar for settings
st.sidebar.title("Settings")
api_key=st.sidebar.text_input("Enter your OpenAI API Key:",type="password")

## Select the OpenAI model
engine=st.sidebar.selectbox("Select OpenAI model",["gpt-4.1","gpt-4.1-mini","gpt-4.1-nano"])

## Adjust response parameter
temperature=st.sidebar.slider("Temperature",min_value=0.0,max_value=1.0,value=0.7)
max_tokens = st.sidebar.slider("Max Tokens", min_value=50, max_value=1000, value=300)


## Main interface for user input
st.write("Go ahead and ask any question")
user_input=st.text_input("You:")

if user_input and api_key:
    response=generate_response(user_input,api_key,engine,temperature,max_tokens)
    st.write(response)
    
    # Add download/copy options container
    st.write("---")
    st.write("Download or copy the response:")
    
    col1, col2, col3 = st.columns(3)
    
    # PDF Download
    with col1:
        if st.button("Download as PDF"):
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("helvetica", size=12)
            
            # Clean the response text to handle any special characters
            cleaned_response = response.encode('latin-1', 'replace').decode('latin-1')
            pdf.multi_cell(0, 10, text=cleaned_response)
            
            pdf_output = io.BytesIO()
            pdf.output(pdf_output)
            
            st.download_button(
                label="Click to Download PDF",
                data=pdf_output.getvalue(),
                file_name="response.pdf",
                mime="application/pdf"
            )
    
    # DOCX Download
    with col2:
        if st.button("Download as DOCX"):
            doc = Document()
            doc.add_paragraph(response)
            
            docx_output = io.BytesIO()
            doc.save(docx_output)
            
            st.download_button(
                label="Click to Download DOCX",
                data=docx_output.getvalue(),
                file_name="response.docx",
                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
            )
    
    # Markdown Copy
    with col3:
        if st.button("Copy as Markdown"):
            markdown_text = markdown.markdown(response)
            st.code(markdown_text, language='markdown')
            st.toast("Markdown code displayed above. You can now copy it!")

elif user_input:
    st.warning("Please enter the OpenAI API Key in the sidebar")
else:
    st.write("Please provide the user input")


