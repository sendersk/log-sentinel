FROM python:3.13-slim

WORKDIR /app

COPY pyproject.toml .
COPY src ./src
COPY logs ./logs

RUN pip install pydantic

CMD ["python", "-m", "log_sentinel.main"]