FROM python:3.8.2-slim
EXPOSE 8501
WORKDIR /app
# RUN apt-get update
# RUN apt install -y libgl1-mesa-glx
RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y
COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .


# CMD streamlit run app.py
CMD streamlit run --server.port $PORT app.py