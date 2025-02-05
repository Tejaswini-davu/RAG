from qdrant_client import QdrantClient
from logger.log_config import setup_logging
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = setup_logging()

class QdrantSearcher:
    def __init__(self, url: str, collection_name: str):
        """
        Initializes the QdrantSearcher class with the necessary parameters.

        :param url: URL of the Qdrant instance.
        :param collection_name: Name of the Qdrant collection to search in.
        """
        self.client = QdrantClient(url=url)
        self.collection_name = collection_name

    def search_vector(self, query_vector: list, top_k: int = 2):
        """
        Perform a similarity search to retrieve the most similar vectors from the Qdrant collection.
        
        :param query_vector: The vector to search for similar vectors.
        :param top_k: The number of top results to return.
        :return: List of dictionaries containing ID, score, and metadata.
        """
        try:
            # Perform the similarity search
            search_results = self.client.search(
                collection_name=self.collection_name,
                query_vector=query_vector,
                limit=top_k  # Number of top results to retrieve
            )
            
            # Extract and format results
            similar_vectors = [
                {
                    "id": result.id,
                    "score": result.score,  # Cosine similarity score
                    "metadata": result.payload  # Retrieve associated metadata
                }
                for result in search_results
            ]
            
            logging.info(f"Found {len(similar_vectors)} similar vectors.")
            return similar_vectors

        except Exception as e:
            logging.error(f"Error during similarity search: {e}")
            return []
