async def search_web_serper(query):
    """Search the web using Serper API for the given query."""
    import requests
    import os

    SERPER_API_KEY = os.getenv('SERPER_API_KEY')
    if not SERPER_API_KEY:
        raise ValueError('Missing the Serper API key. Please set it in the .env file.')

    url = "https://google.serper.dev/search"
    headers = {
        "X-API-KEY": SERPER_API_KEY,
        "Content-Type": "application/json"
    }
    payload = {
        "q": query
    }

    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()


tools = [{
    "name": "search_web_serper",
    "description": "Searches the web using the Serper API for the given query and returns the search results.",
    "parameters": {
        "type": "object",
        "properties": {
            "query": {
                "type": "string",
                "description": "The query to search the web for.",
            },
        },
        "required": ["query"],
        "additionalProperties": False,
        }
    }
]
