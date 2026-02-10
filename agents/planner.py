from utils.llms import call_llm

def planner(topic):   # planner agent to break down the topic into research questions
    return call_llm(f"""
You are a research planner.

Topic:
{topic}

Break this into 3 important research questions.
Return numbered list.
""")
