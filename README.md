<div align="center">
  <h1>🧠 AI-Native Student Execution OS</h1>
  <p><i>An autonomous, AI-driven operating system designed to manage academic execution, active recall, and career mobility—powered by Google Gemini 1.5 Flash.</i></p>

  <p>
    <a href="https://fastapi.tiangolo.com/"><img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI" /></a>
    <a href="https://nextjs.org/"><img src="https://img.shields.io/badge/Next.js-000000?style=for-the-badge&logo=next.js&logoColor=white" alt="Next.js" /></a>
    <a href="https://www.postgresql.org/"><img src="https://img.shields.io/badge/PostgreSQL-336791?style=for-the-badge&logo=postgresql&logoColor=white" alt="PostgreSQL" /></a>
    <a href="https://redis.io/"><img src="https://img.shields.io/badge/Redis-DC382D?style=for-the-badge&logo=redis&logoColor=white" alt="Redis" /></a>
    <a href="https://ai.google.dev/"><img src="https://img.shields.io/badge/Gemini-8E75B2?style=for-the-badge&logo=googlebard&logoColor=white" alt="Gemini" /></a>
  </p>
</div>

---

## 📖 Overview

The **AI-Native Student Execution OS** is not a simple "to-do list wrapper." It is an end-to-end, multi-agent operating system designed to ingest a student's entire digital life and autonomously optimize their execution.

Built on a highly modular Python/FastAPI backend and a glassmorphic Next.js frontend, the system handles algorithmic task fatigue planning, RAG-based knowledge extraction, mock interview generation, and continuous analytical reflections.

## ✨ Key Features

- 📅 **Autonomous AI Planning Engine**: Integrates with `.ics` calendar feeds. Gemini evaluates your task backlog, calculates mental fatigue, and autonomously schedules `StudyBlock`s into the blank spaces of your calendar.
- 🧠 **Knowledge Compression (RAG)**: Drag and drop PDF lectures. The system utilizes `ChromaDB` and `pypdf` to parse and vectorize the documents, allowing Gemini to instantly generate SuperMemo-spaced Flashcards and semantic mental models.
- 🤖 **Execution Agents**: Interact with distinct AI Personas ("The Planner", "Revision Master", "The Coach"). These agents route context securely and hold you accountable to your daily targets.
- 💼 **Career Mobility Simulator**: Track opportunities in a Kanban board. The OS parses your resume into a JSON schema and generates hyper-targeted technical and behavioral mock interview questions.
- 📊 **Execution Analytics**: Calculates a daily Execution Quality Score (0-100) based on task completion, deep work hours, and flashcard retention. The AI provides a harsh, analytical weekly review to ensure continuous improvement.

## 🏗️ Architecture

This project is built for production scalability. 

- **Frontend**: Next.js 15 (React 19), Tailwind CSS, Auth.js.
- **Backend**: FastAPI, SQLAlchemy 2.0 (asyncpg), Pydantic.
- **AI/Vector**: `google-genai` (Gemini 1.5 Flash), ChromaDB local persistence.
- **Infrastructure**: Redis (FastAPI rate-limiting), PostgreSQL (relational + JSONB), Docker Compose.
- **Strict Modularity**: All AI logic is confined to the `/services/` layer in files strictly under 300 lines to preserve LLM token context sizes.

## 🚀 Getting Started

Getting the OS running locally takes less than 5 minutes. 

Please refer to the [QuickStarterGuide.md](./QuickStarterGuide.md) for step-by-step instructions on setting up environment variables, booting Docker Compose, and running Alembic migrations.

## 📚 Blog Series & Deep Dives

To understand the engineering challenges, architectural trade-offs, and AI integrations utilized in this project, check out our Medium blog series:

1. [Architecting an AI-Native OS: Why Modularity Matters](./blogs/01-architecting-ai-os.md)
2. [Building an Autonomous AI Planning Engine with Gemini](./blogs/02-ai-planning-engine.md)
3. [RAG for Students: Compressing Lectures into Flashcards](./blogs/03-knowledge-compression-rag.md)
4. [Simulating Interviews: LLMs in Career Mobility](./blogs/04-career-mobility-llm.md)

## 🤝 Contributing

This project relies on strict modularity. If you intend to contribute, please review the `project-memory-bank/` directory—specifically `architecture-summary.md`—to understand the strict sub-300-line service layer constraints.

## 📄 License

This project is licensed under the MIT License.
