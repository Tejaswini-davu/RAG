import sys
sys.path.append('/home/tejaswini/Documents/VSCODE/Mine/GEN AI/RAG/pinecode')
from qdrant_client import   QdrantClient
from database.qdrant import QdrantManager
import numpy as np
from utilis.text_extraction import extract_pdf_text,extract_docx_text,extract_txt_text,get_file_name,write_extracted_data
from entity.artifact_entity import ArtifactEntity  # Assuming text extraction logic is here
from utilis.text_vects import vectors
from constants.model import embedding_model
import uuid

import os


def extract_text_from_file(file_path):
    # Get the file extension
    _, file_extension = os.path.splitext(file_path)

    # Call the appropriate extraction function based on file type
    if file_extension.lower() == ".pdf":
        return extract_pdf_text(file_path)
    elif file_extension.lower() == ".docx":
        return extract_docx_text(file_path)
    elif file_extension.lower() == ".txt":
        return extract_txt_text(file_path)
    else:
        raise ValueError(f"Unsupported file type: {file_extension}")

def main(file_path):
    # Step 1: Extract text from the file
    extracted_text = extract_text_from_file(file_path)
    extracted_text = str(extracted_text)

    # Step 2: Generate vector from the extracted text using the embedding model
    vector_result = vectors(extracted_text, embedding_model)
    
    # Convert vector_result to numpy array of float32
    vector_result = np.array(vector_result, dtype=np.float32)
    print(f"Vector shape: {vector_result.shape}")  # Print shape before checking

    # Ensure the vector is 1D
    if vector_result.ndim != 1:
        print("Flattening the vector...")  # Debugging message
        vector_result = vector_result.flatten()

    # Print the vector shape for debugging
    print(f"Vector shape after flattening: {vector_result.shape}")

    # Step 3: Extract metadata like file name
    artifact_entity = ArtifactEntity()
    file_name = get_file_name(file_path)

    # Step 4: Ensure vector size matches the generated vector
    vector_size = len(vector_result)  # Set vector size to the length of the vector
    print(f"Generated vector size: {vector_size}")  # Debugging print

     # Step 5: Initialize QdrantManager
    api_url = "http://localhost:6333"  # Replace with your Qdrant instance URL
    collection_name = "my_collection_new"  # Replace with your collection name

    qdrant_manager = QdrantManager(api_url, collection_name, vector_size)

    # Verify Qdrant collection configuration
    
    # Verify Qdrant collection configuration
    collection_info = qdrant_manager.client.get_collection(collection_name)
    # print(f"Qdrant collection '{collection_name}' config: {collection_info}")


    # Step 6: Use the file_name (or another identifier) as the vector ID
    vector_id = str(uuid.uuid4())  # Use UUID as vector ID

    # Step 7: Print the vector size for debugging
    print(f"Vector ID: {vector_id}, Vector dimensions: {len(vector_result)}")
    metadata = {"file_name": file_name}  # Include more metadata if needed
    
    # Step 8: Upsert the vector into the Qdrant collection
    try:
        qdrant_manager.upsert_vector(vector_id, vector_result, metadata)

        print(f"Vector for file '{file_name}' has been upserted into Qdrant.")
    except Exception as e:
        print(f"Error while upserting vector: {e}")

    write_extracted_data(extracted_text, file_name, folder='extracted_data')

# Example usage
if __name__ == "__main__":
    file_path = "/home/tejaswini/Documents/VSCODE/Mine/GEN AI/RAG/pinecode/data/Tejaswini Davu - Jr. Machine Learning Engineer - Resume (3).pdf"
    main(file_path)


