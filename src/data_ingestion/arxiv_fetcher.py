import arxiv
from src import config

def fetch_arxiv_papers(query=config.ARXIV_QUERY, max_results=config.ARXIV_MAX_RESULTS):
    """
    Fetches paper data from ArXiv based on a query.
    """
    search = arxiv.Search(
        query=query,
        max_results=max_results,
        sort_by=arxiv.SortCriterion.SubmittedDate
    )

    papers = []
    for result in search.results():
        paper_data = {
            "arxiv_id": result.entry_id.split('/')[-1],
            "title": result.title,
            "summary": result.summary,
            "published_date": result.published,
            "authors": [author.name for author in result.authors],
            "keywords": result.categories
        }
        papers.append(paper_data)
        print(f"Fetched data for paper: {paper_data['title']}")

    return papers

if __name__ == '__main__':
    # Example usage
    print("Fetching papers from ArXiv...")
    fetched_papers = fetch_arxiv_papers()
    if fetched_papers:
        print(f"\nSuccessfully fetched {len(fetched_papers)} papers.")
        print("\nExample paper data:")
        print(fetched_papers[0])
    else:
        print("No papers were fetched.") 