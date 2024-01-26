FROM python:3.10.12-slim AS deps
RUN pip install --no-cache-dir pycryptodome

RUN python3 -m pip install pycryptodome

FROM pwn.red/jail

COPY --from=deps / /srv/
# make sure remote.py has python shebang at the top
COPY remote.py /srv/app/run

RUN chmod +x /srv/app/run

ENV JAIL_ENV_TERM=xterm
ENV JAIL_MEM=32M
ENV JAIL_TIME=90