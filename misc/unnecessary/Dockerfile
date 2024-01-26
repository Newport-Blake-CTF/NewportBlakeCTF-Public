FROM python:slim AS app

FROM pwn.red/jail
COPY --from=app / /srv
COPY server.py /srv/app/run
COPY flag.txt /srv/app/flag.txt

RUN chmod 777 /srv/app/run

ENV JAIL_MEM=20M JAIL_TIME=30
