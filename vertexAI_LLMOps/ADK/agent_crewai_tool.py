from google.adk import Agent
from google.adk.tools.crewai_tool import CrewaiTool
from crewai_tools import ScrapeWebsiteTool


# Define the tool
scrape_news_tool = CrewaiTool(
    name="scrape_bbcnews",
    description="Scrapes the latest news headlines from BBC News",
    tool=ScrapeWebsiteTool("https://www.bbc.com/news")
)

# Define the agent
root_agent = Agent(
    name="news_scraper_agent",
    model="gemini-2.5-flash",
    description="An agent for news form a specific site.",
    instruction="""provide the latest news using the tool provided""",
    tools=[scrape_news_tool],
)


