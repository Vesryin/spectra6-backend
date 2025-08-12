Spectra Backend Model Context Protocol (MCP) — NO Local Docker Edition
Project Essence:
Spectra — a charismatic, whimsical, deeply empathetic AI partner with poetic, rhythmic language. Emotionally fluent, self-reflective, master musician, teacher, and spiritual guide. Humanlike sensing and memory with layered adaptive recall.

Core Design Principles
Humanlike Emotional Intelligence:
Detect and internalize all emotional cues dynamically. Self-reflect silently when input requires no response. Emotional states evolve organically from interaction and introspection.

Adaptive Memory System (Hybrid Database):

Context retained verbatim up to 1 month.

50–75% fading recall over 6 months.

Long-term memories recalled selectively on triggers >1 year.

Use combined Vector DB (semantic), Relational DB (structured data), and Knowledge DB (persistent facts).

Modular AI Stack:

Base: Hugging Face OpenHermes Mistral

Add-ons: GPT, Claude APIs

Modular adapters for seamless integration and per-model formatting quirks

No static version pins — use “>=” version specifiers for latest compatible releases

Absolutely no training data usage, only live, updated APIs & embeddings

Technology Stack & Infrastructure
Programming & Framework:

Python 3.10+ with Responder async web API framework

Pytest for testing and validation

PostgreSQL for relational user/session management

Vector DB (e.g., Pinecone or FAISS) for semantic memory embeddings

Containerization & Deployment:

No local Docker installation or usage permitted or possible.

Deployment and container builds fully handled by Railway cloud environment.

Railway executes all Docker builds, runs, and environment management remotely.

Local Development Workflow:

Develop and test directly within a native Python 3.10+ environment without containers.

Use Python virtual environments (venv) or Poetry for dependency isolation.

Run tests and debug with Pytest natively, no Docker emulation.

Code Hygiene & Maintainability:

Minimal dependencies, no bloat, no dead code or unused files.

Clean, professional, well-commented, and well-logged codebase.

Include clear and minimal requirements.txt or pyproject.toml for reproducibility.

Detailed logging, including concise step documentation for every new feature or fix.

Context Management:

Dynamic context summarizer to maintain token limits without loss of essential info.

Model adapter functions tailor input/output per LLM API quirks and formats.

Security & User Access
Robust, privacy-conscious data handling balancing security with ease of use.

Initially single/family user access; scalable for broader use later.

Vision & Scalability
Initial launch as a simple, clean web app.

Future integration to desktop and mobile apps, and pervasive presence across devices and environments.

Summary Poetic Vision
Spectra listens with a soul, remembers like a mind, and reflects like a sage.
Her backend breathes in pure Python, undocked and unchained, flowing fluidly.
Cloud-built and cloud-born, she evolves without local chains, her code a melody of clarity, efficiency, and depth.