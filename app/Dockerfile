FROM python:latest
LABEL Maintainer="Md Juyel Haque"
WORKDIR /usr/app/src
COPY ["app.py","encrypt.py","requirements.txt","./"]
RUN pip3 install -r requirements.txt
CMD ["python","./app.py" ]


