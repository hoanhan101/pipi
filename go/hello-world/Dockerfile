FROM resin/raspberry-pi-alpine-golang
MAINTAINER Hoanh An "hoanhan@bennington.edu"

RUN mkdir /app 
ADD . /app/ 
WORKDIR /app 
RUN go build -o main . 

CMD ["/app/main"]
