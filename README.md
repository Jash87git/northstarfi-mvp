# NorthstarFI MVP

AI-powered FIRE planning MVP using Streamlit, FastAPI, PostgreSQL, and Groq.

## Run locally

1. Create virtual environment
```bash
python -m venv .venv
source .venv/bin/activate   # Mac/Linux
.venv\Scripts\activate      # Windows
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

3. Create `.env`
```bash
cp .env.example .env
```
Add your Groq API key.

4. Start PostgreSQL with Docker
```bash
docker compose up -d
```

5. Start backend
```bash
uvicorn backend.main:app --reload --port 8000
```

6. Start frontend in another terminal
```bash
streamlit run frontend/streamlit_app.py
```
