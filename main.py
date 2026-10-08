from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(title="FastAPI Hello World")

PAGE = """<!doctype html>
<html lang="ko">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Hello World · FastAPI</title>
  <style>
    body { font-family: -apple-system, 'Segoe UI', 'Malgun Gothic', sans-serif;
           display: flex; min-height: 100vh; margin: 0; align-items: center;
           justify-content: center; background: #0f172a; color: #e2e8f0; }
    .card { text-align: center; padding: 48px 64px; border-radius: 20px;
            background: #1e293b; box-shadow: 0 20px 60px rgba(0,0,0,.5); }
    h1 { font-size: 2.6rem; margin: 0 0 8px; }
    p  { color: #94a3b8; margin: 4px 0; }
    code { background:#0f172a; padding:2px 8px; border-radius:6px; color:#7dd3fc; }
  </style>
</head>
<body>
  <div class="card">
    <h1>👋 Hello World!</h1>
    <p>Python <b>FastAPI</b> backend · running on Render</p>
    <p><code>GET /api/hello</code> → JSON</p>
  </div>
</body>
</html>"""


@app.get("/", response_class=HTMLResponse)
async def root():
    return PAGE


@app.get("/api/hello")
async def hello():
    return {"message": "Hello World", "backend": "FastAPI", "status": "ok"}


@app.get("/health")
async def health():
    return {"status": "healthy"}
