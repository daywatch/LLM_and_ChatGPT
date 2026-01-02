# in this code, we preload memory from agent engine and then add memory back to the vertex memory bank

from typing import Optional
import asyncio
from google.adk.agents import Agent
from google.adk.agents.callback_context import CallbackContext
from google.adk.tools.preload_memory_tool import PreloadMemoryTool
from agent import root_agent
from google.adk.runners import Runner
from google.genai import types
from google.adk.memory import VertexAiMemoryBankService
from google.adk.sessions import VertexAiSessionService
import os

USER_ID = "user"
os.environ["GOOGLE_API_KEY"] = "YOUR-KEY-HERE"
PROJECT_ID='learn-adk-476816'
LOCATION='us-central1'
agent_engine_id='1676548524172378112'

session_service = VertexAiSessionService(
    project=PROJECT_ID, location=LOCATION, agent_engine_id=agent_engine_id
)
memory_service = VertexAiMemoryBankService(
    project=PROJECT_ID, location=LOCATION, agent_engine_id=agent_engine_id
)

async def add_session_to_memory(
        callback_context: CallbackContext
) -> Optional[types.Content]:
    """Automatically save completed sessions to memory bank """
    if hasattr(callback_context, "_invocation_context"):
        invocation_context = callback_context._invocation_context
        if invocation_context.memory_service:
            await invocation_context.memory_service.add_session_to_memory(
                invocation_context.session
            )


root_agent = Agent(
    name="history_help_agent",
    model="gemini-2.5-flash",
    description=(
        "Agent to help with historical questions."
    ),
    instruction=(
        "You are a helpful AI agent who can answer to user's historical questions."
    ),
    tools=[
        PreloadMemoryTool() #load memory from agent engine
    ],
    after_agent_callback=add_session_to_memory
)


runner = Runner(
    app_name=root_agent.name,  # type: ignore
    agent=root_agent,
    session_service=session_service,
    memory_service=memory_service,
)


async def call_agent(query, runner):
    session = await session_service.create_session(
        app_name=root_agent.name,  # type: ignore
        user_id=USER_ID,
    )
    content = types.Content(role="user", parts=[types.Part(text=query)])
    events = runner.run(
        user_id=session.user_id, session_id=session.id, new_message=content
    )

    for event in events:
        if event.is_final_response():
            final_response = event.content.parts[0].text
            print("\nAgent Response: ", final_response)


if __name__ == "__main__":
    asyncio.run(call_agent("tell me about world war 2", runner))