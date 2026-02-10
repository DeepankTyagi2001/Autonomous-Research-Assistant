# 🧠 Autonomous Research Assistant (Multi-Agent System)

A modular **Multi-Agent System (MAS)** that autonomously plans research, gathers information, summarizes findings, critiques gaps, and generates a structured research report using local LLMs via Ollama.

This project is built from first principles (no agent frameworks) to demonstrate how real agentic systems work internally.

---

## 🚀 Features

- Hierarchical Multi-Agent Architecture
- Dedicated agents with clear roles:
  - Planner Agent
  - Research Agent
  - Summarizer Agent
  - Critic Agent
  - Writer Agent
- Central Manager (Orchestrator)
- Fully modular design
- Local LLM inference using Ollama (Mistral)
- Automatic report generation to file
- Easily extensible for:
  - RAG
  - Memory systems
  - Tool usage
  - Autonomous task planning

---

## 🏗 Architecture

```

User Topic
↓
Planner Agent
↓
Research Agent (per question)
↓
Summarizer Agent
↓
Critic Agent
↓
Writer Agent
↓
research_report.txt

```

This is a **centralized hierarchical Multi-Agent System**, where:

- Each agent has a single responsibility
- The manager controls execution flow
- Agents communicate through structured outputs

---

## 📁 Project Structure

```

ResearchAssistant/
│
├── main.py                # Orchestrator (Manager)
│
├── agents/
│   ├── planner.py
│   ├── researcher.py
│   ├── summarizer.py
│   ├── critic.py
│   └── writer.py
│
├── utils/
│   └── llm.py            # Ollama LLM wrapper
│
└── outputs/
└── research_report.txt

````

---

## ⚙️ Requirements

- Python 3.10+
- Ollama installed
- Mistral model pulled locally

### Install Ollama model:

```bash
ollama pull mistral
````

### Install Python dependency:

```bash
pip install ollama
```

---

## ▶️ How to Run

From the project root:

```bash
python main.py
```

The generated research report will be saved to:

```
outputs/research_report.txt
```

---

## ✏️ Customization

Change the research topic in `main.py`:

```python
TOPIC = "Agentic AI in Education"
```

Replace with any topic you like.

---

## 🧪 Example Topics

* Graph Neural Networks
* Linux Kernel Scheduling
* Blockchain Scalability
* Large Language Models
* Distributed Systems

---

## 🧠 Key Concepts Demonstrated

* Multi-Agent Systems (MAS)
* Agent role separation
* Hierarchical orchestration
* Prompt-based agent design
* Inter-agent communication
* Autonomous research pipelines
* Modular software architecture

---

## 📌 MAS Classification

This system is a:

> **Centralized Hierarchical Multi-Agent System**

All agents are autonomous logical entities coordinated by a central manager.

---

## 🔮 Planned Upgrades (Phase B)

* Retrieval-Augmented Generation (RAG)
* Vector memory
* Citations
* Self-reflection loops
* Tool routing
* Autonomous task queues
* Evaluation scoring

---

## ⭐ Acknowledgement

Built as part of a deep dive into Agentic AI and Multi-Agent Systems from first principles.

Framework-free by design.



Just tell me 👍
