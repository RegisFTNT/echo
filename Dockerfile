FROM python:3.12.1-slim

WORKDIR /app

RUN python -m venv venv
    
ENV PATH="/app/venv/bin:/root/.local/bin:$PATH"

EXPOSE 80

COPY app/ /app

CMD ["python", "app.py"]