## streamlit is used to create the web app for the chatbot
import streamlit as st
## openai is used to create the LLM object for the OpenAI model
import openai
## this is for the OpenAI API key
from langchain_openai import ChatOpenAI
## StrOutputParser is used to parse the output of the LLM
from langchain_core.output_parsers import StrOutputParser
## ChatPromptTemplate is used to create the prompt template for the LLM
from langchain_core.prompts import ChatPromptTemplate
## Ollama is used to create the LLM object for the OpenAI model
from langchain_community.llms import Ollama
## os is used to get the environment variables
import os

import os
from dotenv import load_dotenv
load_dotenv()

## Langsmith Tracking
os.environ["LANGSMITH_API_KEY"]=os.getenv("LANGSMITH_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_PROJECT"]="Simple Q&A Chatbot With OLLAMA"

## Prompt Template
prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful massistant . Please  resond to the user's queries articulately. "),
        ("user","Question:{question}")
    ]
)

def generate_response(question,llm,temperature,max_tokens):
    llm=Ollama(model=llm)
    output_parser=StrOutputParser()
    chain=prompt|llm|output_parser
    answer=chain.invoke({'question':question})
    return answer

## #Title of the app
st.title("Enhanced Q&A Chatbot With Ollama Open-Source Model")
st.subheader("Ask any question and get instant responses from llama3.2-3B model")


## Select the OpenAI model
llm=st.sidebar.selectbox("Select Open Source model",["llama3.2"])

## Adjust response parameter
temperature=st.sidebar.slider("Temperature",min_value=0.0,max_value=1.0,value=0.7)
max_tokens = st.sidebar.slider("Max Tokens", min_value=50, max_value=300, value=150)

## Main interface for user input
st.write("Go ahead and ask any question")
user_input=st.text_input("You:")



if user_input :
    response=generate_response(user_input,llm,temperature,max_tokens)
    st.write(response)
else:
    st.write("Please provide the user input")


