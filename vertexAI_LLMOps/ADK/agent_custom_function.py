from google.adk.agents import Agent

def add_numbers(a: float, b: float) -> float:
    """Add two numbers and return the result."""
    return a + b


def multiply_numbers(a: float, b: float) -> float:
    """Multiply two numbers and return the result."""
    return a * b

# Define the agent
root_agent = Agent(
    name="math_agent",
    model="gemini-2.5-flash",
    instruction="perform addition or multiplication based on user request. Use the tools provided based on user prompt. If no input given, ask for the input numbers",
    description="An agent that uses performs mathematical calculations based on input given",
    tools=[add_numbers, multiply_numbers],
)
