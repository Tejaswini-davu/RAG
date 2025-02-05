# from qdrant_client import QdrantClient
# from qdrant_client.models import VectorParams
# import uuid



# class QdrantManager:
#     def __init__(self, api_url: str, collection_name: str, vector_size: int):
#         """
#         Initialize the QdrantManager with the Qdrant API URL.
#         :param api_url: The URL of the Qdrant instance.
#         :param collection_name: The name of the Qdrant collection to use.
#         :param vector_size: The dimensionality of the vectors.
#         """
#         self.api_url = api_url
#         self.collection_name = collection_name
#         self.vector_size = vector_size
#         self.client = QdrantClient(url=api_url)
#         self.initialize()

#     def initialize(self):
#         """
#         Initialize Qdrant by checking if the collection exists or creating it.
#         """
#         # Fetch collections metadata and extract collection names
#         collections = self.client.get_collections().collections
#         existing_collections = [col.name for col in collections]
        
#         if self.collection_name not in existing_collections:
#             # Create collection if not exists
#             self.client.create_collection(
#                 collection_name=self.collection_name,
#                 vectors_config=VectorParams(
#                     size=self.vector_size,  # Size of the vectors
#                     distance="Cosine"  # Similarity metric (Cosine)
#                 )
#             )
#             print(f"Qdrant collection '{self.collection_name}' created.")
#         else:
#             print(f"Qdrant collection '{self.collection_name}' already exists.")

#     def upsert_vector(self, vector_id: int, vector: list):
#         """
#         Upsert the vector into the Qdrant collection.
#         :param vector_id: The ID to associate with the vector.
#         :param vector: The vector to be inserted or updated.
#         """
#         # Ensure vector_id is positive or use UUID
#         if vector_id < 0:
#             vector_id = str(uuid.uuid4())  # Use UUID if ID is negative

#         # Upsert the vector
#         self.client.upsert(
#             collection_name=self.collection_name,
#             points=[{
#                 'id': vector_id,
#                 'vector': vector
#             }]
#         )
#         print(f"Vector with ID {vector_id} upserted to Qdrant.")
# import logging
# from qdrant_client import QdrantClient
# from qdrant_client.models import VectorParams
# import uuid

# logging.basicConfig(level=logging.INFO)

# class QdrantManager:
#     def __init__(self, api_url: str, collection_name: str, vector_size: int):
#         """
#         Initialize the QdrantManager with the Qdrant API URL.
#         :param api_url: The URL of the Qdrant instance.
#         :param collection_name: The name of the Qdrant collection to use.
#         :param vector_size: The dimensionality of the vectors.
#         """
#         self.api_url = api_url
#         self.collection_name = collection_name
#         self.vector_size = vector_size
#         self.client = QdrantClient(url=api_url)
#         self.initialize()

#     def initialize(self):
#         """
#         Initialize Qdrant by checking if the collection exists or creating it.
#         """
#         # Fetch collections metadata and extract collection names
#         collections = self.client.get_collections().collections
#         existing_collections = [col.name for col in collections]
        
#         if self.collection_name not in existing_collections:
#             # Create collection if not exists
#             self.client.create_collection(
#                 collection_name=self.collection_name,
#                 vectors_config=VectorParams(
#                     size=self.vector_size,  # Size of the vectors
#                     distance="Cosine"  # Similarity metric (Cosine)
#                 )
#             )
#             logging.info(f"Qdrant collection '{self.collection_name}' created.")
#         else:
#             logging.info(f"Qdrant collection '{self.collection_name}' already exists.")

#     def upsert_vector(self, vector_id: str, vector: list):
#         """
#         Upsert the vector into the Qdrant collection.
#         :param vector_id: The ID to associate with the vector.
#         :param vector: The vector to be inserted or updated.
#         """
#         try:
#             # Upsert the vector
#             self.client.upsert(
#                 collection_name=self.collection_name,
#                 points=[{
#                     'id': vector_id,
#                     'vector': vector
#                 }]
#             )
#             logging.info(f"Vector with ID {vector_id} upserted to Qdrant.")
#         except Exception as e:
#             logging.error(f"Error while upserting vector: {e}")

#     def get_vector(self, vector_id: str):
#         """
#         Retrieve a vector from the Qdrant collection by its ID.
#         :param vector_id: The ID of the vector to retrieve.
#         :return: The retrieved vector.
#         """
#         try:
#             # Retrieve the vector
#             response = self.client.get(
#                 collection_name=self.collection_name,
#                 ids=[vector_id]
#             )
#             return response.points[0].vector
#         except Exception as e:
#             logging.error(f"Error while retrieving vector: {e}")
#             return None
#     from qdrant_client.models import Filter


    
    # def search_vector(self, query_vector: list, top_k: int = 5):
    #     """
    #     Perform a similarity search to retrieve the most similar vectors from the Qdrant collection.
    #     :param query_vector: The vector to search for similar vectors.
    #     :param top_k: The number of top results to return.
    #     :return: List of (id, score) tuples representing the most similar vectors.
    #     """
    #     try:
    #         # Perform the search query
    #         search_results = self.client.search(
    #             collection_name=self.collection_name,
    #             query_vector=query_vector,
    #             top=top_k  # Limit the number of results
    #         )
            
    #         # Extracting the results: ID and score (similarity score)
    #         similar_vectors = [(result.id, result.score) for result in search_results]
    #         logging.info(f"Found {len(similar_vectors)} similar vectors.")
    #         return similar_vectors

    #     except Exception as e:
    #         logging.error(f"Error during similarity search: {e}")
    #         return []



import logging
from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, PointStruct
import uuid
from qdrant_client.models import ScoredPoint
logging.basicConfig(level=logging.INFO)

class QdrantManager:
    def __init__(self, api_url: str, collection_name: str, vector_size: int):
        """
        Initialize the QdrantManager with the Qdrant API URL.
        :param api_url: The URL of the Qdrant instance.
        :param collection_name: The name of the Qdrant collection to use.
        :param vector_size: The dimensionality of the vectors.
        """
        self.api_url = api_url
        self.collection_name = collection_name
        self.vector_size = vector_size
        self.client = QdrantClient(url=api_url)
        self.initialize()

    def initialize(self):
        """
        Initialize Qdrant by checking if the collection exists or creating it.
        """
        collections = self.client.get_collections().collections
        existing_collections = [col.name for col in collections]
        
        if self.collection_name not in existing_collections:
            self.client.create_collection(
                collection_name=self.collection_name,
                vectors_config=VectorParams(
                    size=self.vector_size,  # Size of the vectors
                    distance="Cosine"  # Similarity metric (Cosine)
                )
            )
            logging.info(f"Qdrant collection '{self.collection_name}' created.")
        else:
            logging.info(f"Qdrant collection '{self.collection_name}' already exists.")

    def upsert_vector(self, vector_id: str, vector: list, metadata: dict):
        """
        Upsert the vector into the Qdrant collection with metadata.
        :param vector_id: The ID to associate with the vector.
        :param vector: The vector to be inserted or updated.
        :param metadata: Additional metadata to store with the vector.
        """
        try:
            self.client.upsert(
                collection_name=self.collection_name,
                points=[
                    PointStruct(
                        id=vector_id,
                        vector=vector,
                        payload=metadata  # Storing metadata
                    )
                ]
            )
            logging.info(f"Vector with ID {vector_id} and metadata {metadata} upserted to Qdrant.")
        except Exception as e:
            logging.error(f"Error while upserting vector: {e}")

    

    