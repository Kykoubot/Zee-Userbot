FROM python:3.9-slim-buster
RUN apt-get update
RUN apt-get install -y --no-install-recommends \
    curl \
    git \
    ffmpeg
RUN curl -sL https://deb.nodesource.com/setup_current.x | bash - && \
    apt-get install -y nodejs && \
    npm i -g npm
RUN git clone -b Zee-Userbot https://github.com/Kykoubot/Zee-Userbot /home/Zee-Userbot/ \
    && chmod 777 /home/Zee-Userbot \
    && mkdir /home/Zee-Userbot/bin/
WORKDIR /home/Zee-Userbot/
COPY ./sample_config.env ./config.env* /home/Zee-Userbot/
RUN pip install -r requirements.txt
CMD [ "bash", "./start" ]
