FROM mrismanaziz/man-userbot:buster

RUN git clone -b Zee-Userbot https://github.com/Kykoubot/Zee-Userbot /home/manuserbot/ \
    && chmod 777 /home/manuserbot \
    && mkdir /home/manuserbot/bin/

WORKDIR /home/manuserbot/

CMD [ "bash", "start" ]
