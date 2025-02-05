import sys
sys.path.append('/home/tejaswini/Documents/VSCODE/Mine/GEN AI/RAG/pinecode')

from ..utilis.text_vects import vectors



import numpy as np

from constants.model import embedding_model
from database.retrive_data import QdrantSearcher 
import os # Import the class
 
# Initialize the QdrantSearcher with the URL and collection name
searcher = QdrantSearcher(url="http://localhost:6333", collection_name="my_collection_new" )

query = input("enter your text here")


vector_result = vectors(query, embedding_model)
query_vector = np.array(vector_result, dtype=np.float32).flatten().tolist()
top_k = 2
result = searcher.search_vector(query_vector, top_k)
metadata_list = [results['metadata']['file_name'] for results in result]
print(metadata_list)
 

# Folder containing the extracted data
extracted_folder = "/home/tejaswini/Documents/VSCODE/Mine/GEN AI/RAG/extracted_data"  # Replace with the correct folder path

# Function to match filenames and extract data from files in the extracted folder
def fun(metadata_list):
    extracted_data = {}  # A dictionary to store the extracted data
    
    # Loop through each metadata entry
    for metadata in metadata_list:
        file_name = metadata['file_name']
        
        # Construct the file path to search for the file in the extracted folder
        file_path = os.path.join(extracted_folder, file_name)
        
        # Check if the file exists in the folder
        if os.path.exists(file_path):
            # Read the file (assuming it's a text file for simplicity, adjust based on file types)
            with open(file_path, 'r', encoding='utf-8') as file:
                data = file.read()
                
            # Store the extracted data in the dictionary with filename as key
            extracted_data[file_name] = data
        else:
            extracted_data[file_name] = f"File '{file_name}' not found."
    
    # Return the extracted data
    return extracted_data

# Call the function and capture the result
result = fun(metadata_list)

# Print the result (you can remove this if you don't want to print the result)
print(result)



# main file akkada vundhi
# main file test.py
# andhukay nuvu lopathi file run chaysta inko file read avadu
# ooo okay
# Aadi comment chesi edi try cheyala
# nen adho try chesthuna main file em ledu 
# test.py work Avuthadhundhi chudu

# laydu edhi main_file iethay avutadhi this is normal file
