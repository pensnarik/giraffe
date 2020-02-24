FROM python:3

RUN mkdir /giraffe-build

COPY libgiraffe/ /giraffe-build/libgiraffe
COPY setup.py basic.yml /giraffe-build/
ADD giraffe /giraffe-build/

RUN cd /giraffe-build && python3 setup.py sdist
RUN ls /giraffe-build/dist/giraffe-watchdog*.tar.gz | xargs -n 1 pip install -U

CMD ["python", "/usr/local/bin/giraffe"]
