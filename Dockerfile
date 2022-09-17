# app/Dockerfile

FROM python:3.9-slim

EXPOSE 8501



RUN apt-get update && apt-get install -y \
    build-essential \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*


COPY . .
RUN pip install -r requirements.txt
COPY . .
WORKDIR /main

ENTRYPOINT ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]
