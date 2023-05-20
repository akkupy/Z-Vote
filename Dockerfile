FROM python:alpine

ADD Z-Vote/requirements.txt /app/requirements.txt

RUN apk update && apk upgrade
RUN apk add --no-cache bash\
                       libffi-dev \
                       musl-dev \
                       git \
                       gcc \
    && rm -rf /var/cache/apk/*

RUN set -ex \
    && python -m venv /env \
    && /env/bin/pip install --upgrade pip \
    && /env/bin/pip install --no-cache-dir -r /app/requirements.txt \
    && runDeps="$(scanelf --needed --nobanner --recursive /env \
        | awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \
        | sort -u \
        | xargs -r apk info --installed \
        | sort -u)" \
    && apk add --virtual rundeps $runDeps \
    && apk del rundeps

ADD Z-Vote /app
WORKDIR /app

ENV VIRTUAL_ENV /env
ENV PATH /env/bin:$PATH

EXPOSE 8100

CMD ["gunicorn", "--bind", ":8100", "--workers", "5", "--threads", "5", "blockchain_voting.wsgi:application"]
