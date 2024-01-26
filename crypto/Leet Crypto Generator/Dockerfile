FROM sagemath/sagemath:latest

RUN sudo apt-get update && sudo apt-get install socat -y

COPY --chown=sage:sage server.sage /home/sage/server.sage

USER sage

RUN sage --pip install pycryptodome

ENV PYTHONUNBUFFERED=1

EXPOSE 5000

CMD ["/usr/bin/socat", "tcp-listen:5000,reuseaddr,fork", "exec:\"/home/sage/sage/sage server.sage\""]
