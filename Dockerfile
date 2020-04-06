FROM python:3

ADD requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

ADD read.py /app/read.py

CMD ["python", "/app/read.py"]
