FROM python:3.10 as req-stage

WORKDIR /tmp

RUN pip install poetry

COPY ./pyproject.toml ./poetry.lock* /tmp/

RUN poetry export -f requirements.txt --output requirements.txt --without-hashes

FROM python:3.10-slim

WORKDIR /code

COPY --from=req-stage /tmp/requirements.txt /code/requirements.txt

RUN apt-get update \
    && apt-get install -y --no-install-recommends gcc build-essential libxml2-dev libxslt-dev python3-dev libffi-dev libssl-dev\
    && rm -rf /var/lib/apt/lists/* \
    && pip install cryptography \
    && pip install --no-cache-dir --upgrade -r /code/requirements.txt \
    && apt-get purge -y --auto-remove gcc build-essential libxml2-dev libxslt-dev python3-dev libffi-dev libssl-dev 

COPY ./app /code/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]