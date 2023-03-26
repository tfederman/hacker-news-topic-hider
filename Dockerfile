FROM python:3.11-slim-bullseye

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONPYCACHEPREFIX /tmp/pycache

RUN pip3 --no-cache-dir --no-input install beautifulsoup4 requests && rm -rf /tmp/pycache

WORKDIR /app

COPY . /app

ENTRYPOINT ["python3", "-u", "/app/hn-topic-hider.py"]