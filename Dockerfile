FROM python:3.13.0a5-slim-bullseye
WORKDIR /app
COPY . .
RUN pip install py-mon  
