FROM ubuntu:latest
ENV APP_ROOT /app
WORKDIR $APP_ROOT

COPY . /$APP_ROOT/
