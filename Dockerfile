FROM python:3.9.4-slim
ENV PYTHONUNBUFFERED 1
WORKDIR /app
RUN pip install poetry
COPY pyproject.toml* poetry.lock* .
RUN if [ -f pyproject.toml ]; then poetry install; fi
COPY . .