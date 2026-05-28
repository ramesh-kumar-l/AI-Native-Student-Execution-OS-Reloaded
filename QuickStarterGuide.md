# 🚀 Quick Starter Guide: AI-Native Student Execution OS

Welcome to the AI-Native Student Execution OS! This guide will get you from zero to a running local production cluster in under 5 minutes.

## 📋 Prerequisites
Before you begin, ensure you have the following installed on your machine:
- **Docker & Docker Compose**: The entire stack is containerized.
- **Git**: To clone the repository.
- **A Google Gemini API Key**: Grab one for free from Google AI Studio (needed for the AI execution engines).

---

## 🛠️ Step 1: Clone the Repository
```bash
git clone https://github.com/yourusername/ai-native-student-execution-os.git
cd ai-native-student-execution-os
```

## ⚙️ Step 2: Environment Variables
Create a `.env` file in the root of the project directory.

```bash
touch .env
```

Open the `.env` file and populate it with the following:
```env
# AI Integration
GEMINI_API_KEY=your_gemini_api_key_here

# Frontend Configuration
NEXT_PUBLIC_API_URL=http://localhost:8000/api/v1
AUTH_SECRET=generate_a_random_string_here

# (Optional) Google OAuth for Frontend Auth.js
AUTH_GOOGLE_ID=your_google_client_id
AUTH_GOOGLE_SECRET=your_google_client_secret
```

## 🚀 Step 3: Boot the OS
We use Docker Compose to orchestrate Next.js, FastAPI, PostgreSQL, and Redis simultaneously.

```bash
# Build and run the containers in detached mode
docker-compose up --build -d
```

*Note: The first build may take a few minutes as it compiles the multi-stage Dockerfiles and downloads the Python/Node base images.*

## ✅ Step 4: Verify the Installation
Check your Docker containers to ensure all 4 services (`frontend`, `backend`, `db`, `redis`) are running:
```bash
docker-compose ps
```

## 🗄️ Step 5: Run Database Migrations
Before you log in, initialize the database schemas (Profiles, Goals, Flashcards, Execution Metrics) by running Alembic inside the backend container:

```bash
docker-compose exec backend alembic upgrade head
```

## 🌐 Step 6: Access the Dashboard
You're all set! Open your browser and navigate to:

- **Web Dashboard**: [http://localhost:3000](http://localhost:3000)
- **Backend API Docs (Swagger)**: [http://localhost:8000/api/docs](http://localhost:8000/api/docs)

---

## 🧠 System Architecture Overview
If you want to dive into the codebase, here is where everything lives:
- `/frontend`: Next.js 15 App Router. UI components live in `src/components`.
- `/backend/app/api/v1`: FastAPI routers defining the HTTP endpoints.
- `/backend/app/services`: Where the magic happens. All AI logic (Gemini), vector database syncing (ChromaDB), and heavy computation is strictly isolated here in sub-300-line modular files.
- `/project-memory-bank`: The architectural documentation and state of the project.

For deep dives, check out the `README.md` and the `/blogs` directory!
