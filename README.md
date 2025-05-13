# Task-Verifier API

### Setup locally

```bash
cd task_verifier
cp .env.example .env      # insert BOT_TOKEN и AUTH_TOKEN
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
uvicorn task_verifier.app.main:create_app --factory --reload

http://localhost:8000/docs - Swagger UI.
