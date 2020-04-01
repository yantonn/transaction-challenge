FROM python:3.7.3-alpine
RUN apk add --no-cache bash
ADD requirements.txt /tmp/requirements.txt
RUN \
 python3 -m pip install -r /tmp/requirements.txt --no-cache-dir
ENV PYTHONPATH=.
ADD . /app
WORKDIR /app
CMD ["bash", "sh/start.sh"]
