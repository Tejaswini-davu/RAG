from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama



def chat(content,question):

# # Define content and question
# content = "The capital of France is Paris. It is known for the Eiffel Tower."
# question = "What is the capital of France?"

    # Define the prompt template
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful assistant. Answer the question based on the given content dont add any other information."),
        ("user", "Content: {content}\n\nQuestion: {question}")
    ])

    # Define the LLM model
    llm = Ollama(model="llama2")

    # Define the output parser
    output_parser = StrOutputParser()

    # Manually invoke each step instead of using | operator
    formatted_prompt = prompt.invoke({"content": content, "question": question})  # Format the input
    llm_response = llm.invoke(formatted_prompt)  # Pass formatted input to Llama 2
    final_output = output_parser.invoke(llm_response)  # Parse the output

    # Print the response
    print("Response:", final_output)
    return final_output