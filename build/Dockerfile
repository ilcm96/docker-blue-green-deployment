FROM ubuntu:rolling
ENV PYTHONUNBUFFERED=1
RUN apt update && \
    apt install --no-install-suggests --no-install-recommends --yes python3-pip && \
    pip install --upgrade pip && \
    apt clean && \
    rm -rf \
    /tmp/* \
    /var/lib/apt/lists/* \
    /var/tmp/*
RUN pip install --disable-pip-version-check gunicorn django django-crispy-forms environs whitenoise psycopg2-binary
COPY ./app /app
COPY ./build/docker-entrypoint.sh /
WORKDIR /app
EXPOSE 8000
ENTRYPOINT [ "/docker-entrypoint.sh" ]