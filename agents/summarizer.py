from utils.llms import call_llm

def summarizer(text): # summarizer agent to condense the research findings into key points
    return call_llm(f"""
You are a summarizer.

Condense the following into key points:

{text}
""")