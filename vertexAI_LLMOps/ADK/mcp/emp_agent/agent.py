from google.adk.agents import Agent
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset
from google.adk.tools.mcp_tool import StreamableHTTPConnectionParams

# Define the agent
root_agent = Agent(
    name="employee_agent",
    model="gemini-2.5-flash",
    instruction="You are a helpful AI agent who helps with the employee data as per tools available",
    description="An agent that helps with employee information",
    tools=[
        MCPToolset(
            connection_params=StreamableHTTPConnectionParams(
                url="<YOUR-MCP-URL-DEPLOYED-IN-RUN-OR-GKE>/mcp"
            ),
        )
    ],
)



