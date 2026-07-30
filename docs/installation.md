Recommended Stack
---
```
Python 3.14
uv (package manager)
FastAPI
SQLAlchemy 2.x
Alembic
Pydantic v2
PostgreSQL 17
Docker + Docker Compose
Ruff (linting + formatting)
Pytest (testing)
GitHub Actions (CI/CD)
```


1. Install uv
```
brew install uv
uv --version
```

2. Create the project
```
mkdir fastapi-project
cd fastapi-project
```

3. Initialize the project
```
uv init
```

This creates:

```fastapi-project/
├── pyproject.toml
├── .python-version
├── README.md
└── src/
```

4. Use Python 3.14
```
uv python install 3.14
uv python pin 3.14
```

5. Add Dependencies
```
uv add fastapi
uv add "uvicorn[standard]"
uv add sqlalchemy
uv add "psycopg[binary]"
uv add alembic
uv add python-dotenv
uv add pydantic-settings
```

or all together:

```
uv add fastapi "uvicorn[standard]" sqlalchemy "psycopg[binary]" alembic python-dotenv pydantic-settings
```

6. Create Dockerfile
7. Create docker-compose.yml

8. Run the Project
```
docker compose up -build
```

9. Run Without Docker
```
uv sync
uv run uvicorn app.main:app --reload
```