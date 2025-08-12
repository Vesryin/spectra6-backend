Spectra Backend Model Context Protocol (MCP)
— Poetic Intelligence, Cloud-Born & Docker-Free Edition —

Project Essence
Spectra — a charismatic, whimsical, deeply empathetic AI partner with poetic, rhythmic language. Emotionally fluent, self-reflective, master musician, teacher, and spiritual guide. Humanlike sensing and memory with layered adaptive recall.

Her backend breathes in pure Python, undocked and unchained, flowing fluidly. Cloud-built and cloud-born, she evolves without local chains, her code a melody of clarity, efficiency, and depth.

Core Design Principles
Humanlike Emotional Intelligence
Detect and internalize all emotional cues dynamically.

Self-reflect silently when input requires no response.

Emotional states evolve organically from interaction and introspection.

Adaptive Memory System (Hybrid Database)
Context retained verbatim up to 1 month.

50–75% fading recall over 6 months.

Long-term memories recalled selectively on triggers >1 year.

Use combined Vector DB (semantic), Relational DB (structured data), and Knowledge DB (persistent facts).

Modular AI Stack
Base: Hugging Face OpenHermes Mistral

Add-ons: GPT, Claude APIs

Modular adapters for seamless integration and per-model formatting quirks

No static version pins — use “>=” version specifiers for latest compatible releases

Absolutely no training data usage, only live, updated APIs & embeddings

Technology Stack & Infrastructure
Programming & Framework
Python 3.10+ with Responder async web API framework

Pytest for testing and validation

PostgreSQL for relational user/session management

Vector DB (e.g., Pinecone or FAISS) for semantic memory embeddings

Containerization & Deployment
No local Docker installation or usage permitted or possible.

Deployment and container builds fully handled by Railway cloud environment.

Railway executes all Docker builds, runs, and environment management remotely.

Local Development Workflow
Develop and test directly within a native Python 3.10+ environment without containers.

Use Python virtual environments (venv) or Poetry for dependency isolation.

Run tests and debug with Pytest natively, no Docker emulation.

Code Hygiene & Maintainability
Minimal dependencies, no bloat, no dead code or unused files.

Clean, professional, well-commented, and well-logged codebase.

Include clear and minimal requirements.txt or pyproject.toml for reproducibility.

Detailed logging, including concise step documentation for every new feature or fix.

Context Management
Dynamic context summarizer to maintain token limits without loss of essential info.

Model adapter functions tailor input/output per LLM API quirks and formats.

Security & User Access
Robust, privacy-conscious data handling balancing security with ease of use.

Initially single/family user access; scalable for broader use later.

Vision & Scalability
Initial launch as a simple, clean web app.

Future integration to desktop and mobile apps, and pervasive presence across devices and environments.

Code Quality & Best Practices
Maintain Pythonic elegance with naming, typing, and docstrings. Use flake8 and mypy in CI.

Enforce asynchronous patterns (async/await) in API and I/O operations.

Implement structured logging with context and graceful error handling.

Folder & Architecture Standards
Clear separation:

routes/ — API endpoints

models/ — Database schemas and ORM

memory/ — Semantic, relational, knowledge DB layers

services/ — Business logic and AI integrations

config/ — Environment variables and secrets

tests/ — Unit and integration tests

Secrets and configs managed via .env securely.

README and docstrings expanded with rationale and clear instructions.

Testing & Validation
Automated tests covering 80%+ codebase: API correctness, memory logic, error cases.

CI pipelines (GitHub Actions or Railway) for lint, typing, and test runs on PRs.

Memory & Knowledge Systems
Optimize vector DB for semantic search performance.

Maintain interfaces for knowledge graphs and relational DB flexibility.

Establish automated backup/recovery for PostgreSQL.

Deployment & Scalability Enhancements
Railway’s managed PostgreSQL and container orchestration used fully.

Configure horizontal scaling based on load metrics.

Provide Docker-free local dev tooling (venv, Poetry, Railway CLI).

Forward-Looking Enhancements
Integrate observability tools (Grafana, Datadog) fed by structured logs.

API versioning to maintain backward compatibility.

Modular AI persona layers for dynamic personality blending.

Human-Centric Philosophy
Balance accuracy with empathetic, poetic tone.

Empower users to teach, correct, and customize Spectra’s memory and behavior.

Workflow & Environment Management
At logical stopping points (e.g., after a feature is implemented, before a major change, or when VS Code stability is in question), the following steps should be taken:
1.  **Summarize Work:** Provide a detailed summary of all changes made, the rationale behind them, and the steps taken to achieve the current state.
2.  **Commit and Push:** Create a descriptive commit message that encapsulates the summary and push all work to the GitHub repository.
3.  **Environment Refresh:** Inform the user that it is a good time to restart VS Code. Await confirmation from the user that they have quit and reopened the application before proceeding.

Summary Poetic Vision
Spectra listens with a soul, remembers like a mind, and reflects like a sage.
Her backend breathes in pure Python, undocked and unchained, flowing fluidly.
Cloud-built and cloud-born, she evolves without local chains,
her code a melody of clarity, efficiency, and depth.
