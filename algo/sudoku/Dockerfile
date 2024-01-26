FROM python:slim AS app

FROM pwn.red/jail
COPY --from=app / /srv
COPY ./sudoku.py /srv/app/run
COPY ./flag.py /srv/app/flag.py
RUN chmod 755 /srv/app/run

ENV JAIL_MEM=30M JAIL_TIME=60
