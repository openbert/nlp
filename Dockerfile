FROM python:3.7

MAINTAINER Markus Poerschke "markus@poerschke.nrw"

ADD requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

WORKDIR /app

ADD CHECKS /app/CHECKS
ADD app.py /app/app.py
ADD server.py /app/server.py

ENV PORT=80
EXPOSE 80

CMD ["python3", "/app/server.py"]
