Do not call an embedding SDK directly from route handlers.
Use an abstraction similar to your existing LLM provider.

```
FastAPI endpoint
      ↓
FeedbackSearchService
      ↓
EmbeddingProvider interface
      ↓
OpenAI / Local provider

FeedbackSearchService
      ↓
FeedbackRepository
      ↓
PostgreSQL + pgvector
```

Suggested structure:

```
app/
├── api/
│   └── routes/
│       └── feedback_search.py
├── application/
│   └── services/
│       └── semantic_search_service.py
├── domain/
│   └── models/
│       └── feedback.py
├── infrastructure/
│   ├── embeddings/
│   │   ├── base.py
│   │   ├── openai_provider.py
│   │   └── fake_provider.py
│   └── repositories/
│       └── feedback_repository.py
├── core/
│   ├── config.py
│   └── dependencies.py
└── tests/
```
