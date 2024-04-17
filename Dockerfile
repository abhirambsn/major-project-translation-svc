FROM python:3.12-slim-bookworm
LABEL authors="abhiram.bsn"
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y gcc g++ linux-libc-dev
RUN pip install --upgrade pip

COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt

WORKDIR /app
COPY ./src /app
COPY ./download_and_convert_model.sh /tmp
RUN sh /tmp/download_and_convert_model.sh

ENTRYPOINT ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]