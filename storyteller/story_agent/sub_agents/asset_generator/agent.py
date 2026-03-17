from google.adk.agents import ParallelAgent
from .prompt import ILLUSTRATOR_DESCRIPTION
from .image_generator.agent import image_generator_agent
from .voice_generator.agent import voice_generator_agent

illustrator_Agent = ParallelAgent(
    name="IllustratorAgent",
    description=ILLUSTRATOR_DESCRIPTION,
    sub_agents=[
        image_generator_agent,
        voice_generator_agent,
    ],
)