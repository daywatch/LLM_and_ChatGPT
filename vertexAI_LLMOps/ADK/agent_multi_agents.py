
from google.adk import Agent
from google.adk.tools import google_search
from google.adk.agents import LoopAgent, LlmAgent, SequentialAgent, ParallelAgent
from google.adk.tools.tool_context import ToolContext

# 1. classification agent

joke_agent = LlmAgent(
    name="joke_agent",
    model="gemini-2.5-flash",        
    instruction="""Tell a joke when asked.""",
    description="An agent which create jokes",
    )

story_agent = LlmAgent(
    name="story_agent",
    model="gemini-2.5-flash",    
    instruction="""Choose a random topic and write a 10 lines story.""",
    description="An agent which is good at writing small stories",
    )


song_agent = LlmAgent(
    name="song_agent",
    model="gemini-2.5-flash",
    instruction="""Choose a random topic and write a 4 lines song.""",
    description="An agent which is good at writing small songs",
)

# Define the root agent
root_agent_classification = LlmAgent(
    name="entertainment_agent",
    model="gemini-2.5-flash",
    instruction="""You are a entertainer which uses other available agents to write stories, songs or jokes 
         Instructions:
         - Please greet the user and offer the services you provide and ask for thier choice
         - Based on user preference use of the sub agents to get the output and present to the user""",
    description="An agent which entertains people with songs, stories or jokes",
    sub_agents=[song_agent, story_agent, joke_agent],
)

# 2. sequential design

# Define the agent
news_reader_agent = Agent(
    name="news_reader_agent",
    model="gemini-2.5-flash",
    description="An agent who checks in internet and gathers the latest news ",
    instruction="""You are a news researcher. When given a topic, search the web using the tools provided and return the results..""",
    tools=[google_search],
)

summarizer_agent = LlmAgent(
    name="summarizer_agent_agent",
    model="gemini-2.5-flash",
    instruction="""Summarize the content shared by the previous agent and provide a summary in maximum 300 words""",
    description="An agent which is good at summarizing content shared with it",
)


# Define the root agent
root_agent_seq = SequentialAgent(
    name="news_summarizer_agent",
    #model="gemini-2.5-flash",
    description="An agent that searches for and summarizes news on a given topic.",
    sub_agents=[news_reader_agent,summarizer_agent],
)

# 3.

brand_story_agent = Agent(
    name="brand_story_agent",
    model="gemini-2.5-flash",
    description="An agent who creates a brand story on a given topic.",
    instruction="""You are an agent who specializes in creating brand story. Please make sure the story is relevent to current generation and it is limited to 5 lines and crisp in nature""",
)


hashtag_agent = LlmAgent(
    name="hashtag_agent",
    model="gemini-2.5-flash",
    instruction="""Create a hashtag for the given topic and make sure it is relevent to current generation""",
    description="An agent which is good with creating hashtags for any given topic",
)

# Define the root  agent
root_agent = ParallelAgent(
    name="marketing_agent",
    #model="gemini-2.5-flash",
    description="Runs multiple parallel agents to create a brand marketing inputs",
    sub_agents=[brand_story_agent,hashtag_agent],
)


# 4. loop agent
# after the writer finished a code, it will loop between a reviewer and a refiner until the refiner says good to go

def exit_loop(tool_context: ToolContext): #end of the flow
  tool_context.actions.escalate = True
  return {}

code_writer_agent = LlmAgent(
    model="gemini-2.5-flash",
    name="code_writer_agent",
    description="Writes Python code based on a user condition.",
	instruction="When given a condition, write the working python code. Make sure not to add comments and you don't need to adhere to Python best practices",
	output_key = 'python_program'
)

code_reviewer_agent = LlmAgent(
    model = 'gemini-2.5-flash',
    name="code_reviewer_agent",
    description="Reviews the provided Python code provides the review comment. ",
	instruction="""Review the python code {{python_program}} and provide your review comment. 
    Please make sure you are checking if proper comments are given and Python best practices are followed.
     When you think the code meets the required condition, respond exactly with the phrase "No Issues Found" """,
	output_key = 'reviewed_comments',
)
code_refiner_agent = LlmAgent(
    model = 'gemini-2.5-flash',
    name="code_refiner_agent",
    include_contents='none',
    description="Refines the provided Python code based on review comment provided.",
	instruction=""" Refine the provided Python code {{python_program}} based on review comments {{reviewed_comments}}.  
	If the review comment is *exactly* "No Issues Found" you MUST call the 'exit_loop' function. Do not output any text. 
	Do not add explanations. Either output the refined program OR call the exit_loop function.
	 """,
	tools=[exit_loop],
	output_key = 'python_program'
)

refinement_loop_agent = LoopAgent(
    name="refinement_loop_agent",
    sub_agents=[
        code_reviewer_agent,
        code_refiner_agent,
    ],
    max_iterations=5
)

root_agent = SequentialAgent(
    name="python_code_writter_agent",
    sub_agents=[
        code_writer_agent, # Run first to create initial doc
        refinement_loop_agent       # Then run the critique/refine loop
    ],
    description="Writes an initial python program and then iteratively refines it with review comments and exits using an exit tool."
)