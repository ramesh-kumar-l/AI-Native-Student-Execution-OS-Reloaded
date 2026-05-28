# Architecture Summary

The AI-Native Student Execution OS is built on a highly modular, decoupled microservice architecture optimized for speed, AI integration, and production scalability.

## Tech Stack
- **Frontend**: Next.js 15 (App Router), React, Tailwind CSS, Lucide Icons.
- **Backend API**: FastAPI (Python 3.12).
- **Database**: PostgreSQL 16 (relational + JSONB structures).
- **Vector Database**: ChromaDB (Semantic search/RAG).
- **Caching & Rate Limiting**: Redis 7.
- **AI/LLM**: Google Gemini 1.5 Flash via `google-genai` SDK.
- **Infrastructure**: Docker & Docker Compose (Multi-stage builds).

## Core Systems
1. **Context Engine**: Ingests calendar and goal data via `calendar_service` and `goal_service`.
2. **Planning Engine**: Evaluates task fatigue and schedules `StudyBlock`s via `study_planner_service`.
3. **Knowledge Engine**: Parses PDFs (`document_parsing_service`), embeds vectors in ChromaDB (`vector_db_service`), and extracts Flashcards/Summaries via Gemini (`knowledge_extraction_service`).
4. **Agent Orchestrator**: Routes user chats to persistent LLM personas (`planner`, `revision`, `accountability`) managing context safely.
5. **Career System**: Parses resumes and generates targeted mock interviews (`interview_simulator_service`).
6. **Analytics Engine**: Aggregates a daily execution score and generates weekly AI reflections.

## Modularity Strategy
- **File Size Constraints**: All Python services are strictly kept under 300 lines of code. This ensures maximum LLM token efficiency when maintaining or extending the codebase.
- **Separation of Concerns**: FastAPI Routers (`/api/v1`) handle only HTTP/Validation. Complex logic is delegated entirely to the `/services/` layer.
