
from utils.llms import call_llm


def critic(summary): # critic agent to evaluate the summary and identify any gaps or weaknesses in the research
    return call_llm(f"""
You are a critical reviewer.

Here is the summary:

{summary}

Identify missing areas or weaknesses.
""")