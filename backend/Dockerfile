FROM python:3.8.12-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH=/app

EXPOSE 8000
WORKDIR /app/

RUN apt-get update && \
    apt-get install -y --no-install-recommends netcat curl && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | POETRY_HOME=/opt/poetry python && \
    ln -s /opt/poetry/bin/poetry /usr/bin/poetry

COPY poetry.lock pyproject.toml /app/
RUN poetry install --no-dev

COPY ./alembic.ini /app/alembic.ini
COPY ./backend/ /app/backend/
COPY ./migrations/ /app/migrations/

CMD poetry run alembic upgrade head && poetry run uvicorn --host=0.0.0.0 backend.webapi:app 
