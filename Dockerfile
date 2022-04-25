FROM docker.prod.nordnet.se/python:3.10.1-slim-buster

COPY . /app
WORKDIR /app

RUN pip install -r /app/requirements.txt

EXPOSE 4000:4000

CMD ["python", "pyranha-api.py"]