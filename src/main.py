from data_ingestion.arxiv_fetcher import fetch_arxiv_papers
from graph_db.connector import Neo4jConnector
from vector_db.connector import ChromaDBConnector

def main():
    """
    Main function to orchestrate the data ingestion pipeline.
    """
    print("Starting data ingestion pipeline...")

    # Fetch data from ArXiv
    print("\nFetching papers from ArXiv...")
    papers = fetch_arxiv_papers()

    if not papers:
        print("No papers fetched. Exiting.")
        return

    # Initialize database connectors
    print("\nInitializing database connectors...")
    try:
        neo4j_connector = Neo4jConnector()
        chroma_connector = ChromaDBConnector()
        print("Database connectors initialized successfully.")
    except Exception as e:
        print(f"Failed to initialize database connectors: {e}")
        return

    # Ingest data into databases
    print("\nIngesting data into Neo4j and ChromaDB...")
    for paper in papers:
        try:
            # Ingest into Neo4j
            neo4j_connector.add_full_paper_data(paper)
            print(f"Ingested paper {paper['arxiv_id']} into Neo4j.")

            # Ingest into ChromaDB
            chroma_connector.add_paper_embedding(paper)
            
        except Exception as e:
            print(f"Failed to ingest paper {paper.get('arxiv_id', 'N/A')}: {e}")

    # Clean up
    neo4j_connector.close()
    print("\nData ingestion pipeline finished.")
    print("Neo4j connection closed.")

if __name__ == '__main__':
    main() 