from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama

import os

## Prompt Template

content = "The capital of France is Paris. It is known for the Eiffel Tower."
question = "What is the capital of France?"
prompt= ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Answer the question based on the given content."),
        ("user", "Content: {content}\n\nQuestion: {question}")
    ]
)

# ollama LLAma2 LLm 
llm=Ollama(model="llama2")
output_parser=StrOutputParser()
chain=prompt|llm|output_parser
result = chain.invoke({"content": content, "question": question})
print("Response:", result)  # This will display the model's answer
