FROM python:3
RUN apt-get update && apt-get install -y iproute2
COPY ./app.py app.py
CMD python app.py