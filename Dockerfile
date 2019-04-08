FROM python:3-alpine
WORKDIR /app
COPY requirements.txt /app/
RUN apk add python3-dev gfortran build-base
RUN pip3 install https://github.com/tensorflow/tensorflow/archive/v1.5.0.zip
RUN pip3 install -r requirements.txt
ENTRYPOINT ["/usr/bin/python3", "rct_predictor.py"]
