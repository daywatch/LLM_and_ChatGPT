from google.adk.agents import Agent
from google.adk.tools import google_search
from google.adk.agents.callback_context import CallbackContext
from google.adk.models import LlmResponse, LlmRequest
from typing import Optional
from google.genai import types

def before_model_validator(
    callback_context: CallbackContext, llm_request: LlmRequest) -> Optional[LlmResponse]:
    """Inspects/modifies the LLM request or skips the call."""
    agent_name = callback_context.agent_name
    print(f"[Callback] Before model call for agent: {agent_name}")

    # Inspect the last user message in the request contents
    last_user_message = ""
    if llm_request.contents and llm_request.contents[-1].role == 'user':
         if llm_request.contents[-1].parts:
            last_user_message = llm_request.contents[-1].parts[0].text
    print(f"[Callback] Inspecting last user message: '{last_user_message}'")

    if "NEWS" not  in last_user_message.upper():
        print("[Callback] 'NEWS' keyword not  found. Skipping LLM call.")
        # Return an LlmResponse to skip the actual LLM call
        return LlmResponse(
            content=types.Content(
                role="model",
                parts=[types.Part(text="LLM call was blocked by before_model_callback.")],
            )
        )
    else:
        print("[Callback] Proceeding with LLM call.")
        # Return None to allow the (modified) request to go to the LLM
        return None

root_agent = Agent(
    name="google_news_agent",
    model="gemini-2.5-flash",
    instruction="Look for all the latest news in the internet and provide a crisp summary based on the topic",
    description="An agent that uses Google Search to fetch up-to-date news",
    tools=[google_search],
    before_model_callback=before_model_validator
)
