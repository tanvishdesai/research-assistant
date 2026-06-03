# Academic Research Assistant

The Academic Research Assistant is an intelligent platform designed to accelerate the research process by unifying academic discovery, collaboration matching, and topic evolution mapping.

## Core Architecture

This project leverages cutting-edge agentic workflows and hybrid database structures:
- **GraphRAG Foundation**: Combines **Neo4j** (Graph Database) for mapping academic entity relationships (citations, co-authors) with **ChromaDB** (Vector Database) for semantic understanding of paper abstracts.
- **Google ADK & A2A**: Orchestrates multiple specialized AI agents using Google's Agent Development Kit and Agent-to-Agent (A2A) protocol.
  - *Literature Survey Agent*: Discovers papers via semantic querying.
  - *Data Discovery Agent*: Maps papers to their underlying datasets.
  - *Collaboration Agent*: Recommends potential co-authors based on past network graphs.
- **Research Concierge**: The primary user-facing bot that delegates tasks among the specialized agents.

## Project Structure

- `src/`: Contains the core agent logic and database connection adapters.
- `config/`: Environment templates (`env.example`).
- `PLANNING.md` / `TASK.md`: Detailed architectural roadmap and ongoing task lists.

## Setup

1. Copy `config/env.example` to `.env` and configure your API keys and Neo4j connection strings.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Initialize the GraphRAG pipeline via the `src` modules.
