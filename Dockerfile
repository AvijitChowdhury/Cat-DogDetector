# app/Dockerfile

FROM python:3.9-slim-buster
COPY . /main
WORKDIR /main
RUN pip3 install -r requirements.txt
EXPOSE 8501
COPY . /main/static
COPY . /main/tempDir
# CMD streamlit run app.py
ENTRYPOINT [ "streamlit","run"]
CMD [ "app.py" ]