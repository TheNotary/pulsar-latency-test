FROM python:3.8.7-slim

RUN pip install --upgrade pip && \
    pip install --no-cache-dir pulsar-client==2.7.0

ADD consume.py /app/
ADD produce.py /app/
ADD entrypoint.sh /
ENTRYPOINT [ "/entrypoint.sh", "produce" ]

