FROM  golang:1.16-buster as builder

WORKDIR /tmp/docker-blue-green-deployment
COPY ./app .

RUN go mod tidy \
    && go get -u -d -v ./...
RUN CGO_ENABLED=0 GOOS=linux GOARCH=amd64 go build -a -ldflags '-s -w' -o main main.go

FROM scratch
COPY --from=builder /tmp/docker-blue-green-deployment/main /
COPY --from=builder /usr/share/zoneinfo /usr/share/zoneinfo
ENV TZ=Asia/Seoul
CMD ["/main"]