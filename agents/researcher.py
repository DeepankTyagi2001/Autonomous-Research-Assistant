from utils.llms import call_llm


def researcher(question):  # researcher agent to answer each research question in detail
    return call_llm(f"""
You are a research agent.

Question:
{question}

Provide detailed explanation.
""")