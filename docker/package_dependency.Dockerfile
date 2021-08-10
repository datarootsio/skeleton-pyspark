FROM python:3.8
RUN apt-get update && apt-get install -y zip python-dev libffi-dev build-essential
WORKDIR /app
COPY . /app
ENV PYTHONPATH=${PYTHONPATH}:${PWD}
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -

RUN ~/.poetry/bin/poetry install --no-dev

ENTRYPOINT (cd /root/.cache/pypoetry/virtualenvs/*/lib/python3.8/site-packages; zip -r /app/package.zip ./*)
