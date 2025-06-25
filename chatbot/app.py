from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

# First create system prompt
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system","You are a helpful assistant. please response to the user queries"
        ),
        (
            "user","Question {question}"
        )
    ]
)

# Setup llm
llm = ChatOpenAI(model="gpt-3.5-turbo")

# Output parser
output_parser = StrOutputParser()

# Connect chain
chains = prompt | llm | output_parser

# Setup streamlit
st.title("Langchain Demo")
input_text = st.text_input("Search the topic you want")

if input_text:
    st.write(chains.invoke({"question": input_text}))