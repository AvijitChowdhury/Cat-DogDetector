# app/Dockerfile

FROM python:3.9-slim-buster
COPY requirements.txt /requirements.txt
RUN pip3 install -r requirements.txt
EXPOSE 8501
COPY . /static
COPY . /tempDir
COPY . /app
WORKDIR /app
# CMD streamlit run app.py
ENTRYPOINT [ "streamlit","run"]
CMD [ "app.py" ]