import chromadb
from sentence_transformers import SentenceTransformer
from src import config

class ChromaDBConnector:
    def __init__(self):
        self.client = chromadb.PersistentClient(path=config.CHROMA_DB_PATH)
        self.embedding_model = SentenceTransformer(config.EMBEDDING_MODEL_NAME)
        self.collection = self.client.get_or_create_collection(name=config.CHROMA_COLLECTION_NAME)

    def add_paper_embedding(self, paper_data):
        embedding = self.embedding_model.encode(paper_data['summary'])
        
        self.collection.add(
            embeddings=[embedding.tolist()],
            documents=[paper_data['summary']],
            metadatas=[{
                "title": paper_data['title'],
                "authors": ", ".join(paper_data['authors'])
            }],
            ids=[paper_data['arxiv_id']]
        )
        print(f"Added embedding for paper {paper_data['arxiv_id']} to ChromaDB.")

if __name__ == '__main__':
    # Example usage (and for testing connection)
    try:
        chroma_connector = ChromaDBConnector()
        print("Successfully connected to ChromaDB and collection is ready.")
        
        # Example of adding a paper
        # test_paper = {
        #     'arxiv_id': '2109.9430',
        #     'title': 'Test Paper for ChromaDB',
        #     'summary': 'This is a test summary for a paper to be added to ChromaDB.',
        #     'authors': ['Test Author 1', 'Test Author 2']
        # }
        # chroma_connector.add_paper_embedding(test_paper)
        # print("Test data added to ChromaDB.")

    except Exception as e:
        print(f"Failed to connect or add data to ChromaDB: {e}") 