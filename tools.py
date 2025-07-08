from langchain_community.tools import WikipediaQueryRun, DuckDuckGoSearchRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.tools import Tool
from datetime import datetime

search = DuckDuckGoSearchRun()
search_tool = Tool(
    name="search",
    func=search.run,
    description="Use this tool to search the web for information"
)

api_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=100)
wiki_tool = WikipediaQueryRun(api_wrapper = api_wrapper)

def save_to_file(data: str, filename: str = "research_output.txt"):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    formatted_text = f"# Research Output - {timestamp}\n\n{data}"

    with open(filename, "a", encoding="utf-8") as f:
        f.write(formatted_text)

    return f"Research output saved to {filename}"

save_tool = Tool(
    name="save_to_file",
    func=save_to_file,
    description="Use this tool to save the research output to a file"
)
