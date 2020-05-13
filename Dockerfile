FROM python:3.7

MAINTAINER Markus Poerschke "markus@poerschke.nrw"

ADD requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

ADD app.py /app/app.py

ENV FLASK_APP=/app/app.py
ENV FLASK_ENV=production

EXPOSE 80

CMD ["flask", "run", "--port=80", "--host=0.0.0.0"]
