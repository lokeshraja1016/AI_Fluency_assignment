"""A question none of the three systems was specifically designed for."""

from workflow import workflow
from agent import agent


QUESTION = (
    "I want an internship that uses Python and "
    "has a stipend above Rs. 14000. "
    "Which one should I consider?"
)


print("Q:", QUESTION)

print(
    "\nWorkflow :",
    workflow(QUESTION)
)

print(
    "\nAgent   :",
    agent(QUESTION)
)