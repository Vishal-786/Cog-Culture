from duckduckgo_search import DDGS


def search_claim(claim):

    evidence = ""

    try:

        with DDGS() as ddgs:

            results = ddgs.text(
                keywords=claim,
                max_results=10
            )

            for result in results:

                title = result.get("title", "")
                body = result.get("body", "")
                href = result.get("href", "")

                evidence += f"""
Title: {title}
Snippet: {body}
Source: {href}

"""

    except Exception as e:

        evidence = f"Search Error: {str(e)}"

    return evidence