FROM python:3.7.3-alpine
ADD requirements.txt /tmp/requirements.txt
RUN \
 python3 -m pip install -r /tmp/requirements.txt --no-cache-dir && apk --purge del .build-deps
ENV PYTHONPATH=.
ADD . /app
WORKDIR /app
CMD python app.py
