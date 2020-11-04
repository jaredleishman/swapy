FROM alpine:latest

WORKDIR /usr/src/app
RUN apk add python3 py3-pip
RUN pip3 install requests responses
COPY . .
RUN python3 test_swapy.py
CMD ["python3", "swapy.py"]