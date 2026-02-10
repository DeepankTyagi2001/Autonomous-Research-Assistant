from agents.planner import planner
from agents.researcher import researcher
from agents.summarizer import summarizer
from agents.critic import critic
from agents.writer import writer

import os

TOPIC = "Agentic AI in Education"
OUTPUT_PATH = "outputs/research_report.txt"


def main():

    print("\n=== PLANNER ===")
    questions = planner(TOPIC)
    print(questions)

    research_results = []

    print("\n=== RESEARCHER ===")
    for line in questions.split("\n"):
        if line.strip():
            result = researcher(line)
            research_results.append(result)
            print("\n", result)

    combined_research = "\n".join(research_results)

    print("\n=== SUMMARIZER ===")
    summary = summarizer(combined_research)
    print(summary)

    print("\n=== CRITIC ===")
    critique = critic(summary)
    print(critique)

    print("\n=== WRITER ===")
    final_report = writer(TOPIC, summary, critique)
    print(final_report)

    # Ensure outputs folder exists
    os.makedirs("outputs", exist_ok=True)

    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(final_report)

    print(f"\n✅ Research report saved to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
