# fastapi-hello

Python **FastAPI** hello-world web app — minimal deployment template.

## Endpoints

| Path | Description |
|------|-------------|
| `/` | Hello World page (HTML) |
| `/api/hello` | `{"message": "Hello World", "backend": "FastAPI", "status": "ok"}` |
| `/health` | `{"status": "healthy"}` |

## Run locally

```bash
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
# open http://localhost:8000
```

## Deploy on Render

This repo includes `render.yaml` (Blueprint).

- **Option A — Blueprint:** New → Blueprint → select this repo → Apply.
- **Option B — Web Service:** New → Web Service → select this repo →
  - Runtime: `Python 3`
  - Build: `pip install -r requirements.txt`
  - Start: `uvicorn main:app --host 0.0.0.0 --port $PORT`
  - Instance: `Free`
