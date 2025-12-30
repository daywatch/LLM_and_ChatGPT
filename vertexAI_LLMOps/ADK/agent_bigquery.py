from google.adk.agents import Agent
from dotenv import load_dotenv
from google.adk.tools.bigquery import BigQueryCredentialsConfig
from google.adk.tools.bigquery import BigQueryToolset
from google.adk.tools.bigquery.config import BigQueryToolConfig
from google.adk.tools.bigquery.config import WriteMode
from google.genai import types
import google.auth


#tool_config = BigQueryToolConfig(write_mode=WriteMode.ALLOWED)
tool_config = BigQueryToolConfig(write_mode=WriteMode.BLOCKED)

application_default_credentials, _ = google.auth.default()
credentials_config = BigQueryCredentialsConfig(
    credentials=application_default_credentials
)

# Instantiate a BigQuery toolset
bigquery_toolset = BigQueryToolset(
    credentials_config=credentials_config, bigquery_tool_config=tool_config
)

# Define the agent
root_agent = Agent(
    name="bq_agent",
    model="gemini-2.5-flash",
    instruction="""You are an agent with access to several BigQuery tools.
        Make use of those tools to answer the user's questions.""",
    description="Agent to answer questions about BigQuery data and models and execute",
    tools=[bigquery_toolset],
)
