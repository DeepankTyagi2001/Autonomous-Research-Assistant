from utils.llms import call_llm

def writer(topic, summary, critique):  # writer agent to synthesize the summary and critique into a structured research report
    return call_llm(f"""
You are a technical writer.

Topic:
{topic}

Summary:
{summary}

Critique:
{critique}

Write a structured research report.
""")
