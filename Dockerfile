FROM python:3.9.15-slim-bullseye

RUN mkdir -p /app
ENV APP_ROOT /app
WORKDIR ${APP_ROOT}

RUN apt-get update && \
    apt-get install --no-install-recommends --no-install-suggests -y \
    gcc \
    g++ \
    unzip

COPY resources/nwrfc750.zip ${APP_ROOT}
RUN  unzip nwrfc750.zip
ENV SAPNWRFC_HOME ${APP_ROOT}/nwrfcsdk
ENV LD_LIBRARY_PATH ${SAPNWRFC_HOME}/lib

RUN pip install poetry
RUN poetry config virtualenvs.create false
COPY pyproject.toml ${APP_ROOT}
COPY poetry.lock ${APP_ROOT}
RUN poetry install --only main --no-root

COPY ./.streamlit ${APP_ROOT}/.streamlit
COPY ./app ${APP_ROOT}

ENTRYPOINT ["streamlit","run","top.py","--"]