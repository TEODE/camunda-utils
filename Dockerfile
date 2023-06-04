FROM python:3.9-slim

ENV LOGGING_LEVEL 20
ENV HOSTNAME 0.0.0.0
ENV PORT 26500

WORKDIR /usr/src/app 

COPY requirements.txt index.py ./

RUN pip install -r requirements.txt

CMD ["python", "index.py"]