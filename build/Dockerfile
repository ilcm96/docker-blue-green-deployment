FROM bitnami/python:3.9 as builder
ENV PATH="/app/.venv/bin:${PATH}"
WORKDIR /app

RUN python -m venv .venv

# COPY /app/requirements.txt /app
# RUN pip install -r requirements.txt
RUN pip install --disable-pip-version-check gunicorn django django-crispy-forms environs whitenoise psycopg2-binary

COPY ./app /app

FROM bitnami/python:3.9-prod
ENV PATH="/app/.venv/bin:${PATH}"
WORKDIR /app

COPY --from=builder /app /app
COPY ./build/docker-entrypoint.sh /
RUN chmod +x /docker-entrypoint.sh

EXPOSE 8000
ENTRYPOINT [ "/docker-entrypoint.sh" ]