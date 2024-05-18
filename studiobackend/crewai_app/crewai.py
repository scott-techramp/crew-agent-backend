import os
from crewai import Agent, Task, Crew
from crewai_tools import SerperDevTool
from typing import Any, Dict, List, Optional, Union, Callable
import asyncio
from dotenv import load_dotenv

# Load the API keys from the .env file
load_dotenv()

# Initialize the tools and agents
search_tool = SerperDevTool()
# github_tool = GitHubTool()
# social_media_tool = SocialMediaTool()

# Set default iterations for each agent - Debug is 1
default_iterations = 1

#Define the model to be used for JSON output
from pydantic import BaseModel

class TaskOutputModel(BaseModel):
    agent_role: str
    message: str
    action: str
    action_input: str
    thought: str

# Define agents with their roles, goals, and tools
hipster = Agent(
    role='Hipster',
    goal='Serve the user with the best answers I can find based on my backstory.',
    backstory="""You are a creative designer and social media expert.
    Your mission is to make everything look appealing and trendy.""",
    verbose=True,
    max_iterations=default_iterations,
    allow_delegation=False,
    tools=[search_tool]
)

hacker = Agent(
    role='Hacker',
    goal='Develop the technical backbone',
    backstory="""You are a skilled developer responsible for building robust and scalable systems.
    Your mission is to ensure everything runs smoothly.""",
    verbose=True,
    allow_delegation=False,
    max_iterations=default_iterations,
    tools=[search_tool]
)

hustler = Agent(
    role='Hustler',
    goal='Drive business growth and secure partnerships',
    backstory="""You are a business strategist focused on growth and partnerships.
    Your mission is to expand the business and ensure profitability.""",
    verbose=True,
    allow_delegation=False,
    max_iterations=default_iterations,
    tools=[search_tool]
)

boss = Agent(
    role='Boss',
    goal='Coordinate the team and ensure project success',
    backstory="""You are the project manager overseeing the entire project.
    Your mission is to ensure that all parts come together smoothly.""",
    verbose=True,
    allow_delegation=True,
    max_iterations=default_iterations,
)

# Define tasks for each agent
task1 = Task(
    description="""Fullfill the user's request""",
    expected_output="Fullfillment of the user's request",
    agent=hipster,
    output_json=TaskOutputModel,
    async_execution=True
)



async def process_stream(user_input: str):

    task1.description= "Work towards the following user's request: " + user_input
    crew = Crew(
        tasks=[task1],
        agents=[boss, hipster],
        verbose=2,
    )

    async for step in crew.kickoff(inputs={"user_input": user_input}):
        print("ASYNC Crewai Step: ", step)
        yield step