FROM python:3.9

ADD json-reciever.py .
ENTRYPOINT python -u json-reciever.py
EXPOSE 1234
