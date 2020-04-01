FROM python:3.7.6

ENV PIP_DEFAULT_TIMEOUT=100 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1 \
    POETRY_VERSION=1.0.2

RUN pip install -U pip
RUN pip install "poetry==$POETRY_VERSION"

COPY poetry.lock .
COPY pyproject.toml .
RUN poetry install --no-interaction --no-ansi --no-dev --no-root

WORKDIR /app
COPY . /app

EXPOSE 5000

CMD ["python", "-m", "gunicorn.app.wsgiapp", "app:app", "-w 2", "-b 0.0.0.0:5000"]