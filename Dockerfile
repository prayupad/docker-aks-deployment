FROM python:3.8

COPY requirements.txt ./requirements.txt
COPY hello.py ./hello.py

RUN pip install -r requirements.txt

ENV FLASK_APP=hello
ENV FLASK_ENV=development
ENV FLASK_DEBUG=0

CMD ["flask", "run","--host=0.0.0.0"]