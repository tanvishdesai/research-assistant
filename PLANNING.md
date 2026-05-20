# PLANNING.md

## 1. High-Level Vision

The Academic Research Assistant is a platform designed to accelerate the research process for academics. It will provide a unified interface to discover relevant research papers, identify potential collaborators, and explore the evolution of research topics. By leveraging a combination of graph database technology, vector search, and AI agents, the platform will offer a more intuitive and powerful way to navigate the complex landscape of academic literature. This student project aims to build a proof-of-concept demonstrating the core functionalities.

## 2. Architecture

The architecture is centered around a multi-layered approach, integrating a graph database for structured relationships, a vector database for semantic understanding, and a system of intelligent agents to perform complex tasks.

*   **Data Layer**:
    *   **Neo4j Graph Database**: This will be the core of our data model, storing entities such as `Authors`, `Papers`, `Institutions`, `Keywords`, and the relationships (`CITES`, `AUTHORED_BY`, `AFFILIATED_WITH`) that connect them. This is ideal for analyzing the network of academic collaborations and citations. [8, 15, 16]
    *   **Vector Database**: A vector database (e.g., ChromaDB, Weaviate) will store vector embeddings of paper abstracts, dataset descriptions, and potentially other textual data. [21, 22] This will power semantic search and similarity-based recommendations.

*   **Intelligence Layer**:
    *   **GraphRAG**: This technique will be implemented to combine the strengths of both the graph and vector databases. [1, 2] For instance, when a user asks for "seminal works in federated learning," we can traverse the citation graph in Neo4j to identify highly cited papers (graph walk) and then use semantic search on their abstracts to understand their content more deeply.
    *   **Google A2A (Agent-to-Agent) Protocol**: This protocol will define the communication standard for our specialized AI agents, allowing them to collaborate on complex user requests. [4, 7, 18]

*   **Agent Layer**:
    *   **Agent Development Kit (ADK)**: We will use Google's ADK to build and orchestrate our AI agents. [11, 13, 14] This framework will help us create specialized agents that are modular and can be composed into more complex workflows. [17]
    *   **Specialized Agents**:
        *   **Literature Survey Agent**: Responsible for finding relevant papers based on semantic queries and GraphRAG.
        *   **Data Discovery Agent**: Focuses on linking papers to the datasets they use or produce.
        *   **Collaboration Matchmaking Agent**: Identifies potential co-authors based on research interests and collaboration history.
    *   **Research Concierge Bot**: A single, user-facing bot that delegates tasks to the specialized agents. It will maintain a memory of user interactions for personalized suggestions.

*   **Presentation Layer**:
    *   A simple web-based user interface (e.g., using Streamlit or Flask) to interact with the Research Concierge Bot and visualize the results (e.g., timelines, collaboration graphs).

## 3. Constraints

*   **Student Project Scope**: This is not a production-scale system. The focus is on implementing the core functionalities with a limited dataset.
*   **Data Availability**: The project will rely on publicly available academic datasets (e.g., from ArXiv, Semantic Scholar, or other open sources). The size and quality of this data will be a limiting factor.
*   **Computational Resources**: Indexing and querying large vector databases, as well as running multiple LLM-powered agents, can be computationally intensive. We will need to be mindful of the resources available.
*   **API Costs**: The use of large language models through APIs will incur costs. A budget will need to be considered, or smaller, locally-run models might be explored.

## 4. Tech Stack & Tools

*   **Graph Database**: Neo4j [8]
*   **Vector Database**: ChromaDB (for its simplicity in a student project setting)
*   **AI Agent Framework**: Google's Agent Development Kit (ADK) [11]
*   **Inter-Agent Communication**: Google's A2A Protocol [4]
*   **Backend**: Python (Flask or FastAPI)
*   **Frontend**: Streamlit (for rapid UI development) or a simple HTML/CSS/JavaScript frontend.
*   **LLM**: A model from the Gemini family or another suitable model accessible via API.
*   **Data Ingestion**: Python scripts using libraries like `requests`, `beautifulsoup4`, and APIs from academic sources.