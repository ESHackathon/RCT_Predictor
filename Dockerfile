FROM ubuntu:18.04
RUN apt-get update -y
RUN apt-get install python3.6 python3-pip python3-dev -y
RUN apt-get install curl -y
WORKDIR /app
COPY rct_predictor.py requirements.txt /app/
RUN pip3 install setuptools==41.0.0
RUN pip3 install -U pip wheel
RUN pip3 install -r requirements.txt
# RUN pip3 install https://github.com/ijmarshall/robotsearch/archive/master.zip
ENTRYPOINT ["/usr/bin/python3", "rct_predictor.py"]
