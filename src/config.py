import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# In a real application, use environment variables or a secret management system.
# For this project, we define them here directly.

# Neo4j Configuration
NEO4J_URI = os.getenv("NEO4J_URI", "bolt://localhost:7687")
NEO4J_USER = os.getenv("NEO4J_USER", "neo4j")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD", "password")

# ChromaDB Configuration
CHROMA_DB_PATH = os.getenv("CHROMA_DB_PATH", "chroma_db")
CHROMA_COLLECTION_NAME = os.getenv("CHROMA_COLLECTION_NAME", "papers")

# Embedding Model Configuration
EMBEDDING_MODEL_NAME = os.getenv("EMBEDDING_MODEL_NAME", "all-MiniLM-L6-v2")

# ArXiv Fetcher Configuration
ARXIV_QUERY = os.getenv("ARXIV_QUERY", "cat:cs.AI")
ARXIV_MAX_RESULTS = int(os.getenv("ARXIV_MAX_RESULTS", 10)) 