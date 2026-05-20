# TASK.md

## Active Work

*   **Milestone 1: Core Data Infrastructure Setup**
    *   [ ] **Task 1.1**: Set up and configure a Neo4j instance.
        *   [x] Sub-task: Define the graph schema (nodes: Paper, Author, Institution, Keyword; relationships: AUTHORED_BY, CITES, AFFILIATED_WITH, HAS_KEYWORD).
    *   [ ] **Task 1.2**: Set up a Vector Database (ChromaDB).
    *   [ ] **Task 1.3**: Develop data ingestion scripts.
        *   [ ] Sub-task: Write a script to fetch data from a source like ArXiv.
        *   [ ] Sub-task: Populate the Neo4j graph with the fetched data.
        *   [ ] Sub-task: Generate embeddings for paper abstracts and store them in ChromaDB.

*   **Milestone 2: Implementing the "Research Concierge" Bot and Agents**
    *   [ ] **Task 2.1**: Develop the "Literature Survey" Agent.
        *   [ ] Sub-task: Implement semantic search functionality using the vector database.
        *   [ ] Sub-task: Integrate basic GraphRAG to combine graph traversal with semantic search.
    *   [ ] **Task 2.2**: Develop the "Collaboration Matchmaking" Agent.
        *   [ ] Sub-task: Implement a function to find authors working on similar topics who have not co-authored papers.
    *   [ ] **Task 2.3**: Develop the "Data Discovery" Agent.
        *   [ ] Sub-task: Implement a feature to link papers to datasets (initially, this can be based on keyword matching in the text).
    *   [ ] **Task 2.4**: Set up the A2A communication protocol for the agents. [9, 12]
    *   [ ] **Task 2.5**: Build the "Research Concierge" bot using the Agent Development Kit to orchestrate the other agents.

## Backlog

*   [ ] **Feature: Timeline View of Topic Evolution**
    *   [ ] Sub-task: Extract publication years for papers.
    *   [ ] Sub-task: Group papers by topic and year.
    *   [ ] Sub-task: Use an LLM to generate summaries for topic evolution over time.
    *   [ ] Sub-task: Create a simple timeline visualization in the frontend.

*   [ ] **Enhancement: Advanced GraphRAG**
    *   [ ] Sub-task: Implement more complex graph traversal queries (e.g., finding paths between authors).
    *   [ ] Sub-task: Refine the combination of graph and vector search results.

*   [ ] **Enhancement: User Profiles and Session Memory**
    *   [ ] Sub-task: Implement a simple user session to store conversation history.
    *   [ ] Sub-task: Use past interactions to provide personalized suggestions.

*   [ ] **Enhancement: Frontend Improvements**
    *   [ ] Sub-task: Add more interactive visualizations for the graph data (e.g., using a library like `pyvis`).
    *   [ ] Sub-task: Improve the user interface for a better user experience.

*   [ ] **Documentation and Final Report**
    *   [ ] Sub-task: Document the code and architecture.
    *   [ ] Sub-task: Write a final project report summarizing the work and findings.
    *   [ ] Sub-task: Prepare a presentation of the project.