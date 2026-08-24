# Memory Engine Component — DFAI Platform

The **Memory Engine Component** is the primary evidence ingestion, integrity verification, and memory forensic parsing engine for the **DFAI (Digital Forensics AI)** platform. It provides a non-blocking, asynchronous processing pipeline capable of ingesting volatile memory dumps, verifying evidence integrity via cryptographic hashing, running Volatility 3 plugins in parallel, and streaming real-time status updates back to the client interface.

---

## 🏗️ Architecture & Structural Design

The Memory Engine Component is built following a strict **Layered (3-Tier) Architecture** combined with an **Event-Driven & Asynchronous Messaging Design**:

* **Presentation Layer (FastAPI & WebSockets):** Manages incoming REST endpoints, validates request payloads with Pydantic, and handles persistent WebSocket connections for real-time progress updates.
* **Application Layer (Business & Domain Logic):** Handles evidence file validation, computes SHA-256 integrity checks, decomposes extraction jobs into plugin-specific tasks, and aggregates real-time execution statistics.
* **Infrastructure Layer (Redis, Celery, Volatility 3, MongoDB):** Executes Volatility 3 CLI commands via Celery background workers, uses Redis as a message broker and state cache, and persists structured JSON artifacts into the centralized MongoDB database (`dfai_db`).

---

## ⚡ Key Features

* **Data Integrity & Chain of Custody:** Calculates local SHA-256 cryptographic hashes and verifies them against client-provided values before processing evidence.
* **Asynchronous & Non-Blocking Pipeline:** Offloads heavy volatile memory parsing from the main web server thread to a scalable Celery worker pool.
* **Domain Coverage:** Parses RAM dumps across **13 forensic domains** (processes, network connections, drivers, handles, registry hives, DLLs, services, etc.).
* **Schema-less NoSQL Ingestion:** Stores structured forensic artifacts directly inside **13 dedicated collections** within `dfai_db`.
* **Real-time Status Streaming:** Pushes job metrics (`total`, `pending`, `finished`, and `percentage completion`) directly to the UI via WebSockets.

---

## 🛠️ Technology Stack

* **Language & Framework:** Python 3.10+, FastAPI
* **Task Queue & Message Broker:** Celery, Redis
* **Forensic Engine:** Volatility 3
* **Database:** MongoDB (`dfai_db`)
* **Communication Protocols:** HTTP (REST) & WebSockets

---

## 📁 Repository Structure

```text
memory_engine/
├── app/
│   ├── api/                  # Presentation Layer (FastAPI Routers & WebSockets)
│   │   ├── endpoints/        # API route definitions
│   │   └── websockets/       # WebSocket connections & state push logic
│   ├── core/                 # Configurations, Redis, & MongoDB clients
│   ├── services/             # Application Layer (Hash verification, Task Orchestrator)
│   ├── tasks/                # Infrastructure Layer (Celery tasks & Volatility3 wrappers)
│   └── models/               # Pydantic schemas & Data Transfer Objects (DTOs)
├── tests/                    # Unit and integration tests
├── Dockerfile                # Container definitions
├── docker-compose.yml        # Service orchestration (FastAPI, Redis, Celery, MongoDB)
├── requirements.txt          # Python dependencies
└── README.md                 # Project documentation