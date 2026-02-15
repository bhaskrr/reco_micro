# RecoMicro — A Plug-and-Play Recommender API

A lightweight, local-first Recommendation Engine API built with Python and FastAPI. RecoMicro provides a minimal REST interface to collect user-item interactions and serve item recommendations.

## The Problem

Building a recommendation engine today usually forces developers into two extremes:

1. **The "Black Box" SaaS:** Services like AWS Personalize or Algolia are powerful but expensive, create vendor lock-in, and offer zero privacy for sensitive user data.
2. **The "Academic" Research:** Building from scratch using Jupyter Notebooks and heavy ML libraries is slow, hard to deploy, and difficult to integrate into a standard Web/Mobile stack.

Small-to-medium projects need a **middle ground**: a tool that is as easy as a SaaS but as private and customizable as an open-source library.

## The RecoMicro Solution

**RecoMicro** bridges the gap between raw data science and production-ready web engineering.

* Your data never leaves your server.
* Stop mixing ML logic with your business logic. RecoMicro handles the "Heavy Math" via a clean API.
* No need for Spark clusters or massive RAM. We optimize for efficiency, starting with a simple SQLite backend.

## Vision

To Make recommender systems easy to run locally and integrate into any product. Provide:

- A small API for tracking interactions and requesting recommendations.
- Simple SQLite-based storage so anyone can clone and run the project with no infra.
- Provide a bridge between a Jupyter Notebook and a Production API.
- A clear separation between API, storage, and the recommendation math so you can extend or swap components.

## Features

- Built on FastAPI for sub-millisecond overhead.
- Differentiate between "views," "likes," and "purchases" to fine-tune recommendation accuracy.
- Intelligent fallback to trending items for new, unknown users.
- Automatic Swagger/OpenAPI documentation.

## Storage

RecoMicro follows a **"Local-First, Cloud-Ready"** storage philosophy:

* SQLite3 for zero-latency local development.
* Uses **SQLAlchemy 2.0** (ORM).

## Quick Start

**RecoMicro** uses `uv` for ultra-fast dependency management. If you don't have it yet, [install uv first](https://github.com/astral-sh/uv).

### 1. Setup Environment

Clone the repository and sync the dependencies. `uv` will automatically create a virtual environment.

```sh
# Clone the repository
git clone https://github.com/bhaskrr/reco_micro.git

cd recomicro

# Sync dependencies and create .venv
uv sync
```

### 2. Run the API

Use uv run to ensure you are executing the code within the project's virtual environment.

```sh
uv run uvicorn src.main:app --reload --port 8000
```

### 3. Explore

* API Base: <http://127.0.0.1:8000/>
* Interactive Docs: <http://127.0.0.1:8000/docs>

## Future Roadmap

* Hybrid filtering support.
* Cold-start engine.
* Built-in A/B testing hooks.
* Real-time re-ranking and much more.

## Contributing

We welcome contributions of all sizes! Whether you are fixing a typo or implementing a new ML algorithm, your help makes RecoMicro better.

### Choose Your Track

Whether you're looking to sharpen your backend skills or dive deep into mathematical optimizations, we have a path for you. Pick a track below that matches your expertise and interests.

|Area|Focus|Skills|
|----|----|-----|
|Data & AI|New similarity metrics, ranking logic, or data validation|Python, NumPy|
|Core API|New endpoints, middleware, or database optimizations|FastAPI, SQLAlchemy|
|DevOps|Docker optimizations, CI/CD pipelines, or testing|Docker, GitHub Actions|

## License

 See the LICENSE file for more information.

## Contact & Support

* Found a bug? Open an issue.
* Want to brainstorm a new feature? Start a GitHub Discussion.
* Creator: @[bhaskrr](https://github.com/bhaskrr) — feel free to reach out!
