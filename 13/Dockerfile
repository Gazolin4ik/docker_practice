FROM python:3
RUN apt-get update && apt-get install -y \ 
    iputils-ping \
    iproute2 \
    net-tools \
    && rm -rf /var/lib/apt/lists/* && \
    chmod u+s /usr/bin/ping && \
    setcap cap_net_raw+p /usr/bin/ping

WORKDIR /
COPY app.py .
ENTRYPOINT ["python", "app.py"]