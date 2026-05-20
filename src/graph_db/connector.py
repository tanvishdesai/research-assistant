from neo4j import GraphDatabase
from src import config

class Neo4jConnector:
    def __init__(self):
        self.driver = GraphDatabase.driver(config.NEO4J_URI, auth=(config.NEO4J_USER, config.NEO4J_PASSWORD))

    def close(self):
        self.driver.close()

    def _execute_query(self, query, parameters=None):
        with self.driver.session() as session:
            result = session.run(query, parameters)
            return [record for record in result]

    def add_paper(self, arxiv_id, title, summary, published_date):
        query = (
            "MERGE (p:Paper {arxiv_id: $arxiv_id}) "
            "ON CREATE SET p.title = $title, p.summary = $summary, p.published_date = $published_date"
        )
        self._execute_query(query, {"arxiv_id": arxiv_id, "title": title, "summary": summary, "published_date": published_date.isoformat()})

    def add_author(self, name):
        query = "MERGE (a:Author {name: $name})"
        self._execute_query(query, {"name": name})

    def add_keyword(self, term):
        query = "MERGE (k:Keyword {term: $term})"
        self._execute_query(query, {"term": term})

    def link_paper_to_author(self, arxiv_id, author_name):
        query = (
            "MATCH (p:Paper {arxiv_id: $arxiv_id}) "
            "MATCH (a:Author {name: $author_name}) "
            "MERGE (a)-[:AUTHORED_BY]->(p)"
        )
        self._execute_query(query, {"arxiv_id": arxiv_id, "author_name": author_name})

    def link_paper_to_keyword(self, arxiv_id, term):
        query = (
            "MATCH (p:Paper {arxiv_id: $arxiv_id}) "
            "MATCH (k:Keyword {term: $term}) "
            "MERGE (p)-[:HAS_KEYWORD]->(k)"
        )
        self._execute_query(query, {"arxiv_id": arxiv_id, "term": term})

    def add_full_paper_data(self, paper_data):
        self.add_paper(
            paper_data['arxiv_id'],
            paper_data['title'],
            paper_data['summary'],
            paper_data['published_date']
        )
        for author_name in paper_data['authors']:
            self.add_author(author_name)
            self.link_paper_to_author(paper_data['arxiv_id'], author_name)
        
        for keyword in paper_data['keywords']:
            self.add_keyword(keyword)
            self.link_paper_to_keyword(paper_data['arxiv_id'], keyword)

if __name__ == '__main__':
    # Example usage (and for testing connection)
    try:
        connector = Neo4jConnector()
        print("Successfully connected to Neo4j.")
        # You can add a test query here if you want
        # connector.add_author("Test Author")
        # print("Test data added.")
        connector.close()
    except Exception as e:
        print(f"Failed to connect to Neo4j: {e}") 