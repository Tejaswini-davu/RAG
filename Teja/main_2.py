import sys
import streamlit as st
import numpy as np
import os

# Import necessary classes and functions
sys.path.append('/home/tejaswini/Documents/VSCODE/Mine/GEN AI/RAG/pinecode')
from chatbot_python import chat
from text_vects import vectors
from constants.model import embedding_model
from database.retrive_data import QdrantSearcher 

# Setup searcher
searcher = QdrantSearcher(url="http://localhost:6333", collection_name="my_collection_new")

# Folder containing the extracted data
extracted_folder = "/home/tejaswini/Documents/VSCODE/Mine/GEN AI/RAG/pinecode/extracted_data"

# Function to match filenames and extract data from files in the extracted folder
def fun(metadata_list):
    extracted_data = {}  #
    for metadata in metadata_list:
        file_name = metadata
        
        # Construct the file path to search for the file in the extracted folder
        file_path = os.path.join(extracted_folder, file_name)
        print(file_path)
        
        # Check if the file exists in the folder
        if os.path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as file:
                data = file.read()
                
            # Store the extracted data in the dictionary with filename as key
            extracted_data[file_name] = data
        else:
            extracted_data[file_name] = f"File '{file_name}' not found."
    
    # Return the extracted data
    return extracted_data

# Streamlit User Interface
def main():
    st.title("Text Query Search")

    # Input from the user
    query = st.text_input("Enter your query:")
    
    if query:
        # Vectorize the query
        vector_result = vectors(query, embedding_model)
        query_vector = np.array(vector_result, dtype=np.float32).flatten().tolist()
        top_k = 2
        
        # Search for similar vectors
        result = searcher.search_vector(query_vector, top_k)
        metadata_list = [results['metadata']['file_name'] for results in result]
        
        # Call the function to extract data
        extracted_data = fun(metadata_list)
        
        # Get the response from the chatbot
        output = chat(extracted_data, query)

        # Display the result
        st.write("Chatbot Response:")
        st.write(output)

# Run the Streamlit app
if __name__ == '__main__':
    main()
