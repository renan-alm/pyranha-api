FROM docker.prod.nordnet.se/python:3.10.1-slim-buster

COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

EXPOSE 8080:8080

COPY pyranha-api.py /opt/pyranha-api.py
ENTRYPOINT ["/opt/pyranha-api.py"]