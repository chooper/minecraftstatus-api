FROM python:2-onbuild

ENV PATH            /app:$PATH
ENV LANG            en_US.UTF-8

RUN mkdir -p /app /app/.profile.d /app/bin
WORKDIR /app

# Add app code
COPY . /app/
