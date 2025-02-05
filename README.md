# RAG Project

## Description
The **RAG (Retriever-Augmented Generation)** project leverages **Qdrant** for efficient vector storage, **Llama2** for chatbot functionality, and **Cosine Similarity** for document retrieval. 
The project is designed to handle PDF data extraction, generate embeddings, and perform similarity search, providing meaningful answers via a conversational AI model.

### Key Components:
- **test.py**: Extracts data from the provided PDF path, saves it, and generates embeddings.
- **main_2.py**: Hosts a web application using **Streamlit**. You can enter any query, and it generates embeddings for the entered question, performs a similarity search, and passes relevant results to the chatbot,
 which returns appropriate answers to the user.

## Technologies Used:
- **Qdrant**: For efficient vector storage and retrieval.
- **Llama2**: For building a conversational AI chatbot.
- **Cosine Similarity**: For measuring similarity between query embeddings and stored documents.
- **Streamlit**: For hosting the interactive web application.
