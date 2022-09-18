# app/Dockerfile

FROM python:3.9
EXPOSE 8501

COPY requirements.txt ./requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
WORKDIR /app
CMD streamlit run app.py
# CMD streamlit run --server.port $PORT app.py