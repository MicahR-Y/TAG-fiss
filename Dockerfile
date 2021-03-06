FROM python:2.7.15-slim

COPY . /TAG-fiss

RUN set -ex \
    && apt-get update && apt-get install -y --no-install-recommends curl \
    && rm -rf /var/lib/apt/lists/* \
    && pip install --no-cache-dir -U --upgrade-strategy eager /TAG-fiss \
    && rm -rf /TAG-fiss

CMD ["fissfc"]
