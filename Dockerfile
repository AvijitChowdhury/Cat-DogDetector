FROM python:3.8.2-slim
EXPOSE 8501
WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .


# CMD streamlit run app.py
CMD streamlit run --server.port $PORT app.py