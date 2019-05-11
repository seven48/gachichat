FROM python:3.7.3-stretch

ENV BRANCH master

RUN git clone --branch ${BRANCH} https://github.com/seven48/gachichat \
 && cd gachichat/server/ \
 && pip install -r requirements.txt

WORKDIR /gachichat/server/

ADD backend/docker-entrypoint.sh /gachichat/server/entrypoint.sh

ENTRYPOINT "./entrypoint.sh"
