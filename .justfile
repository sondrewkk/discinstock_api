dev:
    poetry run uvicorn --host 0.0.0.0 --port 8088 --reload app.main:app