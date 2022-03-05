FROM python:3.9.10-slim-buster
WORKDIR /app/
RUN apt-get update
RUN apt-get install -y --no-install-recommends \
    curl \
    git \
    ffmpeg
RUN curl -sL https://deb.nodesource.com/setup_16.x | bash - && \
    apt-get install -y nodejs && \
    npm i -g npm
COPY . .
RUN pip install -r requirements.txt
CMD [ "bash", "./start" ]
