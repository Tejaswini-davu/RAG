from logger.log_config import setup_logging
import numpy as np


logger = setup_logging()


from sentence_transformers import SentenceTransformer

# def vectors(text, model_name):
#     # Initialize the model correctly
#     embedding_model = SentenceTransformer(model_name)
#     vector = embedding_model.encode(text)
#     logger.info("embedding are done")
#     return vector
# def vectors(text, model_name):
#     """
#     Converts the input text into vectors using the specified model.
#     :param text: The input text to be vectorized.
#     :param model_name: The name of the pre-trained Sentence Transformer model.
#     :return: The vectorized representation of the text.
#     """
#     global embedding_model
    
#     # Initialize the model only once
#     if embedding_model is None:
#         embedding_model = SentenceTransformer(model_name)
#         logger.info(f"Initialized SentenceTransformer model: {model_name}")
    
#     # Encode the text to vector
#     vector = embedding_model.encode(text)
    
#     # Log the process
#     logger.info(f"Embedding completed for the text. Vector shape: {len(vector)} elements.")
    
#     # Return the vector
#     return vector


def vectors(text, model_name):
    # Initialize the model correctly
    embedding_model = SentenceTransformer(model_name)
    
    # Encode the text
    vector = embedding_model.encode(text)
    
    # Ensure vector is 2D (even for single input, should return a 2D array)
    # if vector.ndim == 1:
    #     vector = np.expand_dims(vector, axis=0)  # Convert to 2D array if necessary
    print("Embeddings are done")
    # logger.info("Embeddings are done, vector shape: %s", vector.shape)
    
    return vector

