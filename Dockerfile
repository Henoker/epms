# Pull base image
FROM python:3.10.4-slim-bullseye
RUN apt-get update
RUN apt-get -y install python3-pip python3-cffi python3-brotli libpango-1.0-0 libpangoft2-1.0-0
ENV WEASYPRINT_VERSION 57.1
RUN pip install weasyprint==$WEASYPRINT_VERSION
# Set environment variables
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# Set work directory
WORKDIR /code

# Install dependencies
COPY ./requirements.txt .

RUN pip install -r requirements.txt
# Copy project
COPY . .
EXPOSE 8000