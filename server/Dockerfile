# docker run -d -name testUrl -p 8999:8000 

FROM python:3.8-alpine 

RUN apk -U upgrade 

COPY  . /app 

WORKDIR /app 

RUN pip3 install -r requirements.txt 

ENTRYPOINT ["python3"]

CMD ["flask_app.py"]
